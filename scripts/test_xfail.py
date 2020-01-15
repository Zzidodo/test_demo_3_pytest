"""
作  者:周小丽
文件名:
日  期:
"""
import pytest


# 当条件为真时,用例执行失败
@pytest.mark.xfail(condition=True, reason="")
def test_1():
    print("当条件为真时,用例执行失败")
    assert False


# 当条件为真时,用例执行成功
@pytest.mark.xfail(condition=True, reason="")
def test_2():
    print("当条件为真时,用例执行成功")
    assert True


# 当条件为假时,用例执行成功
@pytest.mark.xfail(condition=False, reason="")
def test_3():
    print("当条件为假时,用例执行成功")
    assert True


# 当条件为假时,用例执行失败
@pytest.mark.xfail(condition=False, reason="")
def test_4():
    print("当条件为假时,用例执行失败")
    assert False
