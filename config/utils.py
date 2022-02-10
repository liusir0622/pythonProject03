"""
定义常用的工具类
"""
import random
def get_phone():
    """
        生成随机的11位手机号码
        手机号的前缀； ['13','17','18','15']
        后面需要随机生成 9位数。
        :return:
        """
    # 手机号码前缀  从列表中随机选择其中的一个值
    pre_phone = random.choice(['13', '17', '18', '15'])
    # 随机的一个值
    nums = ""
    for i in range(9):
        # 每次随机的时候 生成 0-9 之间的一个数字
        num = random.randint(0, 9)
        # 每次生成一个新的随机值 做一次拼接
        nums = nums + str(num)
    # 前缀和后面的值拼接在一起 组成手机号
    return pre_phone + nums
