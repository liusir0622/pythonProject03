"""
项目运行的常见配置
"""
from config.utils import get_phone
class BaseConfig:
    BASEURL = "http://49.233.108.117:28019/"
    PHONE = get_phone()
    TOKEN = None
