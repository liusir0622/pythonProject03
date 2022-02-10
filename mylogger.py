"""
定义日志文件
"""
import logging

# 配置logging
logger = logging.getLogger("apitesting")

# 配置logger的级别
logger.setLevel(logging.DEBUG)

# 配置通用的数据格式              时间         日志级别     记录器名字   日志信息
format = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')

# 配置控制台打印
sh = logging.StreamHandler()

# 设置日志级别
sh.setLevel(logging.DEBUG)
# 设置日志格式
sh.setFormatter(format)

# 将控制台打印 添加到logger中
logger.addHandler(sh)

# 配置文件存储
fh = logging.FileHandler(filename="utils/mylogger.txt", encoding='utf8')
# 日志文件的级别
fh.setLevel(logging.DEBUG)
# 日志文件的内容格式
fh.setFormatter(format)

# 将日志配置添加到logger
logger.addHandler(fh)

if __name__ == '__main__':
    logger.debug('这是debug信息')
    logger.info('这是info信息')
