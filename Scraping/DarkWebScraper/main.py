# https://justhackerthings.com/post/building-a-dark-web-scraper/

import sys


def main():
    # Disable SSL warnings
    try:
        import requests.packages.urllib3

        requests.packages.urllib3.disable_warnings()
    except:
        pass

    START = sys.argv[1]


if __name__ == "__main__":
    main()
