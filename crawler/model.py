# -*- coding:utf-8 -*-


class Item:

    def __init__(self, item_id, seller_id, title, is_crawled):
        self.item_id = item_id
        self.seller_id = seller_id
        self.title = title
        self.is_crawled = is_crawled

    def dict(self):
        return {
            'item_id': self.item_id,
            'seller_id': self.seller_id,
            'title': self.title,
            'is_crawled': self.is_crawled
        }


class Rate:

    def __init__(self, rate_id, size_info, rate_content):
        self.rate_id = rate_id
        self.size_info = size_info
        self.rate_content = rate_content

    def dict(self):
        return {
            'rate_id': self.rate_id,
            'size_info': self.size_info,
            'rate_content': self.rate_content
        }

class FailedUrl:

    def __init__(self, url):
        self.url = url

    def dict(self):
        return {'url': self.url}

