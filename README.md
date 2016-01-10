# 📬 Posts

Posts is a Python library for send 📧mail easily.

## Installation

- ``GitHub:`` https://github.com/importcjj/Posts
- ``PyPi`` https://pypi.python.org/pypi/posts

```sh
pip install posts
```
## Examples

Here is the first one to send a mail in **text**:

```python

from posts import Posts

mail = Posts('smtp-server', 'your-username', 'your-passwd')

with mail() as box:
	box.text('to_address', subject='Subject', content='Content')
```

Posts does not only support mail in **text** type, but also support **html**:

```python
box.html('to_address', subject='Subject', content='Content')
```

Next, we can send a mail with **attachments**:

```python
with mail() as box:
	box.attach({'example.jpg': './example.jpg})
	box.text('to_address')
```

Finally, we can send the Html mail with image:

```python
with mail(alias='alias') as box:
	box.attach({
			'example.jpg': './example.jpg'})
	box.html(
		recipient='to_address', 
		subject='subject', 
		content='<img src="cid:example.jpg">')
``` 

Maybe you need to send mail by ssl, don't worry:

```python

with mail(ssl=True) as box:
	box.text('to_address')
```
## Chain

Just try like this:

```python
box.attach(**kwargs).\
	attach(**kwargs).\
	text(**kwargs)
```
	
## Contibute

### License

Is **BSD2**, see LICENSE for more details.