"""
编写pytest相关的测试用例
pytest单元测试用例 函数名必须以 test_ 开头
"""

from page.useraction import UserAction

user = UserAction()
def test_user_register():
    """
    测试注册接口
    :return:
    """

    # 拿到服务器返回的结果
    r = user.user_register()
    # 添加断言 预期结果
    # 状态码为200
    assert r.status_code == 200
    # 期望注册成功
    # 对服务器返回结果进行断言
    print(r.json())
    assert r.json()["resultCode"] == 200
    assert r.json()["message"] == "SUCCESS"


def test_login():
    r = user.user_login()
    assert r.status_code == 200
    assert r.json()["resultCode"] == 200
    assert r.json()["message"] == "SUCCESS"