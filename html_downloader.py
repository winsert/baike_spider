#coding:utf8

import urllib2

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)

        if response.getcode() == 200:
            return response.read()
        elif response.getcode() == 303:
            print "303 重定向"
            return None
        elif response.getcode() == 400:
            print "400 请示错误"
            return None
        elif response.getcode() == 401:
            print "401 未授权"
            return None
        elif response.getcode() == 403:
            print "403 禁止访问"
            return None
        elif response.getcode() == 404:
            print "404 文件未找到"
            return None
        elif response.getcode() == 500:
            print "500 服务器错误"
            return None
        else:
            return None

        return response.read()
