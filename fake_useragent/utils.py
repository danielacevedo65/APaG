from __future__ import absolute_import, unicode_literals

import codecs
import json
import os
import re
from threading import Lock

try:  # Python 2
    from urllib2 import urlopen, Request, URLError
    from urllib import quote_plus
except ImportError:  # Python 3
    from urllib.request import urlopen, Request
    from urllib.parse import quote_plus
    from urllib.error import URLError

try:
    import socket
    import gevent.socket

    if socket.socket is gevent.socket.socket:
        from gevent import sleep
    else:
        from time import sleep
except (ImportError, AttributeError):
    from time import sleep


def get(url):
    with get.lock:
        request = Request(url)

        attempt = 0

        while attempt < settings.HTTP_RETRIES:
            attempt += 1

            try:
                return urlopen(request, timeout=settings.HTTP_TIMEOUT).read()
            except (URLError, OSError):
                if attempt == settings.HTTP_RETRIES:
                    raise FakeUserAgentError
                else:
                    sleep(settings.HTTP_TIMEOUT)
get.lock = Lock()


def get_browsers():
    """
    very very hardcoded/dirty re/split stuff, but no dependencies
    """
    html = get(settings.BROWSERS_STATS_PAGE)
    html = html.decode('windows-1252')
    html = html.split('<table class="w3-table-all notranslate">')[1]
    html = html.split('</table>')[0]

    browsers = re.findall(r'\.asp">(.+?)<', html, re.UNICODE)

    browsers = [
        settings.OVERRIDES.get(browser, browser) for browser in browsers
    ]

    browsers_statistics = re.findall(
        r'td\sclass="right">(.+?)\s', html, re.UNICODE
    )

    return list(zip(browsers, browsers_statistics))


def get_browser_versions(browser):
    """
    very very hardcoded/dirty re/split stuff, but no dependencies
    """
    html = get(settings.BROWSER_BASE_PAGE.format(browser=quote_plus(browser)))
    html = html.decode('iso-8859-1')
    html = html.split('<div id=\'liste\'>')[1]
    html = html.split('</div>')[0]

    browsers_iter = re.finditer(r'\?id=\d+\'>(.+?)</a', html, re.UNICODE)

    browsers = []

    for browser in browsers_iter:
        if 'more' in browser.group(1).lower():
            continue

        browsers.append(browser.group(1))

        if len(browsers) == settings.BROWSERS_COUNT_LIMIT:
            break

    return browsers


def load():
    browsers_dict = {}
    randomize_dict = {}

    try:
        for item in get_browsers():
            browser, percent = item

            browser_key = browser

            for value, replacement in settings.REPLACEMENTS.items():
                browser_key = browser_key.replace(value, replacement)

            browser_key = browser_key.lower()

            browsers_dict[browser_key] = get_browser_versions(browser)

            for _ in range(int(float(percent) * 10)):
                randomize_dict[str(len(randomize_dict))] = browser_key
    except Exception:
        server_cached_data = get(settings.CACHE_SERVER)

        try:
            return json.loads(server_cached_data.decode('utf-8'))
        except (UnicodeDecodeError, TypeError, ValueError):
            raise FakeUserAgentError
    else:
        return {
            'browsers': browsers_dict,
            'randomize': randomize_dict
        }


def write(data):
    with codecs.open(settings.DB, encoding='utf-8', mode='wb+',) as fp:
        json.dump(data, fp)


def read():
    with codecs.open(settings.DB, encoding='utf-8', mode='rb',) as fp:
        return json.load(fp)


def exist():
    return os.path.isfile(settings.DB)


def rm():
    if exist():
        os.remove(settings.DB)


def update():
    if exist():
        rm()

    write(load())


def load_cached():
    if not exist():
        update()

    return read()


from fake_useragent import settings  # noqa # isort:skip
from fake_useragent.errors import FakeUserAgentError  # noqa # isort:skip
