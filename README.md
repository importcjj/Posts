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

mail = Posts('smtp-server', your-username', 'your-passwd', port=25)

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
	box.text('to_address', subject='Subject', content='Content')
```

Finally, we can send the Html mail with image. and
in the example, we also use a **alias** for the sender:

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
	box.text('to_address', subject='Subject', content='Content')
```
## Chain

Just try like this:

```python
box.attach({
		'name1': '/path/to/file1',
		'name2': '/path/to/file2'}).\
	attach({'name3': '/path/to/file3'}).\
	text('to_address', 'subject', 'content').\
	html(['to_address1', 'to_address2'], 'subject', 'content')
```

The text mail with attachment 1, 2, 3 will send to [address](),
and then the html mail with attachment 1, 2, 3 will be sent ot
[address1](), [address2]() together.

## Contibute

### License

**BSD2**, see [LICENSE]() for more details.

## TODO

* add **alias** for **recipient**.
* add **carbon copy**.
* add usage without **with**.