# -*- coding: utf-8 -*-

import smtplib
import socket
from contextlib import contextmanager
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


class PostSMTP(smtplib.SMTP):

    def __init__(self, sender, alias=None, host='', port=0, local_hostname=None,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        smtplib.SMTP.__init__(self, host, port, local_hostname, timeout)
        self._sender = sender
        self._sender_alias = alias if alias else sender
        self._attachments = {}

    def attach(self, attachments):
        """Add attachments.

        Args:
            attachments (dict): attachments
                example: {'alias_name': 'path/to/filename'}
        Returns:
            obj to support chain calling.
        """
        for k, v in attachments.iteritems():
            self._attachments[k] = v
        return self

    def _pay_load(self, msg):
        for k, v in self._attachments.iteritems():
            with open(v, 'rb') as f:
                part = MIMEApplication(f.read())
            part.add_header('Content-Disposition', 'attachment', filename=k)
            part.add_header('Content-ID', '<{}>'.format(k))
            msg.attach(part)
        return msg

    def _header(self, msg, recipient, subject):
        msg['Subject'] = subject
        msg['From'] = '{} <{}>'.format(self._sender_alias, self._sender)
        msg['To'] = ', '.join(recipient) if isinstance(recipient, list) else recipient
        return msg

    def text(self, recipient, subject, content, charset='us-ascii'):
        _msg = MIMEMultipart()
        _msg = self._header(_msg, recipient, subject)
        _text = MIMEText(content, _subtype='plain', _charset=charset)
        _msg.attach(_text)
        _msg = self._pay_load(_msg)
        self.sendmail(self._sender, recipient, _msg.as_string())

    def html(self, recipient, subject, content, charset='utf-8'):
        _msg = MIMEMultipart()
        _msg = self._header(_msg, recipient, subject)
        _html = MIMEText(content, _subtype='html', _charset=charset)
        _msg.attach(_html)
        _msg = self._pay_load(_msg)
        self.sendmail(self._sender, recipient, _msg.as_string())


class Posts(object):

    def __init__(self, host, usermame, password, port=25):
        self._host = host
        self._port = port
        self._username = usermame
        self._password = password

    @contextmanager
    def __call__(self, sender=None, alias=None, ssl=False):
        sender = sender if sender else self._username
        self._smtp = PostSMTP(sender, alias)
        self._smtp.connect(self._host)
        if ssl:
            self._smtp.ehlo()
            self._smtp.starttls()
            self._smtp.ehlo()
        self._smtp.login(self._username, self._password)
        try:
            yield self._smtp
        finally:
            self._smtp.quit()
