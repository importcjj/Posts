======
 Posts
======

Posts is a Python library for send mail easily.


 Examples
~~~~~~~~~

Here is the first one to send a mail which just contains text:

.. code:: python

	from posts import Posts

	mail = Posts('smtp.qq.com', 'your-username', 'your-passwd')

	with mail() as box:
		box.text('to_address', subject='Subject', content='Content')


Posts does not only support Text mail, but also Html mail

.. code:: python
	
	box.html('to_address', subject='Subject', content='Content')


Next, we can send a Text mail with attachments:

.. code:: python

	with mail() as box:
		box.attach({'example.jpg': './example.jpg})
		box.text('to_address')


Finally, we can send the Html mail with image:

.. code:: python

	with mail(alias='alias') as box:
		box.attach({
				'example.jpg': './example.jpg'})
		box.html(
			recipient='to_address', 
			subject='subject', 
			content='<img src="cid:example.jpg">')


Maybe you need to send mail by ssl, don't worry:

.. code:: python

	with mail(ssl=True) as box:
		box.text('to_address')

 Chain
~~~~~~~

Just try like this:

	**box.attach(\*\*kwargs).attach(\*\*kwargs).text(\*\*kwargs)**
	
 Contibute
~~~~~~~~~~

 License
----------

Posts is **BSD**, see LICENSE for more details.