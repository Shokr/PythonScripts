import urllib
from urllib.request import urlopen


def is_internet():
    """
    Query internet using python
    :return:
    """
    try:
        urlopen('https://www.google.com', timeout=1)
        return True
    except urllib.error.URLError as Error:
        print(Error)
        return False


if is_internet():
    print("Internet is active")
else:
    print("Internet disconnected")
