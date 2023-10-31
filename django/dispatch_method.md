The dispatch method takes in the request and ultimately returns the response. Normally, it returns a response by calling (ie, dispatching to) another method like get. Think of it as a middleman between requests and responses.

Normally, it simply decides what method in the class (e.g. get(),post(), etc) should be used (ie, dispatched) based on the HTTP method that was used in the request. Something like

```python
def dispatch(self, request, *args, **kwargs):
    if request.method == 'GET':
        return self.get(*args, **kwargs)
    elif request.method == 'POST':
        return self.post(*args, **kwargs)
    elif #... and so on
```

You can use your own dispatch method to change this behavior to call whatever methods you want that should return the HTTP response or even 'intercept' and modify the arguments that ultimately reach those methods. For example, you might use this to block/filter certain kinds of requests or even inject arguments...

```python
def dispatch(self, request, *args, **kwargs):
    """Updates the keyword args to always have 'foo' with the value 'bar'"""
    if 'foo' in kwargs:
        # Block requests that attempt to provide their own foo value
        return HttpResponse(status_code=400)
    kwargs.update({'foo': 'bar'}) # inject the foo value
    # now process dispatch as it otherwise normally would
    return super().dispatch(request, *args, **kwargs)
```
But the key concept is that it's the entry point for requests and ultimately responsible for returning the response.