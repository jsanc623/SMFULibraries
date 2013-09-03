SMFULibraries
=============

A collection of libraries for the SMFU.in web service

This library provides Python 3 bindings to SMFU.in

Example Usage:
```python
from smfu import Shortener

short = Shortener(url='htttp://www.google.com', key=APIKEY)

return_json = short.shorten(full_url_only=True)
return_json2 = short.shorten(full_url_only=False)
```

Specifying `full_url_only=True` returns
```json
Request Response:
[
    {
        "id": "9",
        "urlkey": "http://smfu.in/7OtnKD",
        "url": "http://www.google.com",
        "time": "1377799950"
    }
]
```
while `full_url_only=False` returns
```json
Request Response:
[
    {
        "id": "9",
        "urlkey": "7OtnKD",
        "url": "http://www.google.com",
        "time": "1377799950"
    }
]
```
