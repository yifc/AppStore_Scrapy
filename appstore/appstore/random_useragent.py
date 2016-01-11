import random
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class RandomUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, settings, user_agent='Scrapy'):
        super(RandomUserAgentMiddleware, self).__init__()
        self.user_agent = user_agent

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)

        print "*************Current UserAgent:%s***********"%ua

        request.headers.setdefault('User-Agent', ua)

    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F",
    ]
