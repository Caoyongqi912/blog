import random
import urllib.request


class Base_spider():

    def __init__(self):
        self.ua_list = [
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) "
            "Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 "
            "Safari/534.50",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"
        ]

    def ua(self):
        ua = random.choice(self.ua_list)
        data = {
            'User-Agent': ua
        }
        return data

    def get_content(self, url):

        request = urllib.request.Request(url=url, headers=self.ua())
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        return content
