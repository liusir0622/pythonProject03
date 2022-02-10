import requests
from mylogger import logger

class MyRequests:

    def __init__(self):
        self.logger = logger

    def do_requests(self, method, url, params=None, data=None, json=None, **kwargs):
        """
        自定义请求
        :param method: 请求方法
        :param url: 请求的url
        :param params: get请求参数
        :param data: post请求参数
        :param json: post 请求参数
        :param kwargs: 其他参数
        :return:
        """
        if method == 'get':
            # 添加日志
            self.logger.debug(f"发送get请求,请求地址:{url},请求参数: {params}")
            # 调用requests get 请求
            r = requests.get(url, params=params, **kwargs)
            # 添加日志
            self.logger.debug(f"服务器返回结果:{r.text}")
            return r
        elif method == "post":
            self.logger.debug(f'发送post请求,请求地址:{url},请求数据：{json}, {data}')
            r = requests.post(url, data=data, json=json, **kwargs)
            self.logger.debug(f'服务器返回结果:{r.text}')
            return r


if __name__ == '__main__':
    # 模拟发送请求
    req = MyRequests()
    req.do_requests(method='get', url="http://47.100.175.62:3000/api/v1/topics")
