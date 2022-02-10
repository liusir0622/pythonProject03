"""
用户相关的操作
"""
from config.baseconfig import BaseConfig
import requests
import hashlib
class UserAction:

    def user_register(self):
        """
        注册用户
        :return:
        """
        url = BaseConfig.BASEURL+"api/v1/user/register"
        body_data = {
            "loginName":BaseConfig.PHONE, #通过函数 生成手机号码
            "password":"123456"
        }
        # print(f'现在进行注册：用户名{BaseConfig.PHONE}，密码为123456')
        # 发送 json 格式 post 请求
        r = requests.post(url,json=body_data)
        # 装态码
        # print(r.status_code)
        # print(r.json())
        # 将结果返回出去
        return r

    def user_login(self):
        """
        用户登录
        :return:
        """
        passwd = hashlib.md5('123456'.encode()).hexdigest()

        url = f"{BaseConfig.BASEURL}api/v1/user/login"
        body_data = {
            "loginName":BaseConfig.PHONE,
            "passwordMd5":passwd  #使用md5 加密之后的密文进行登录
        }
        # print(f'现在进行登录:用户名为{BaseConfig.PHONE},加密之后的密码{passwd}')
        r = requests.post(url,json=body_data)
        # print(r.status_code)
        # print(r.json())
        # print("登录成功的token值:",r.json()["data"])
        # 将登录成功的token值更新到类变量中
        BaseConfig.TOKEN = r.json()['data']
        return r

    def user_search(self):
        """
        搜索商品
        :return:
        """
        url = "http://49.233.108.117:28019/api/v1/search"
        qury_data = {
            "keyword":"iphone"
        }
        header = {
            # 使用类变量 获取最新的token值
            "token":BaseConfig.TOKEN
        }
        print(f'现在搜索商品，使用信息头：{header}')

        r = requests.get(url,params=qury_data,headers=header)
        print('搜索结果',r.json())
        return r
