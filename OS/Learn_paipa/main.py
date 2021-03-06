import paipa
import requests


def download_url(url):
    resp = requests.get(url)
    return resp


def process_response(resp):
    print(("== Fetched %s =" % resp.url) + "=" * 50)
    print(resp.content)
    # We have no subsequent step, so we don't really need to return
    # anything, but returning the response for further processing could
    # be interesting.
    return resp


pipeline = paipa.Pipeline([
    (paipa.funcstep(download_url), 3),
    # Only one thread because that way the console printout is
    # nicely readable. Try to tune this and see what it does.
    (paipa.funcstep(process_response), 1),
])
pipeline.put("http://example.com/2")
pipeline.put("http://example.com/4")
pipeline.put("http://example.com/6")
pipeline.finish()
pipeline.run()
# Observe that the order in which the URLs are printed may vary due to
# runtime differences in the requests.

# https://github.com/stylight/python-paipa/blob/master/doc/introduction.rst
