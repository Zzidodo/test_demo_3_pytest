"""
作  者:周小丽
文件名:
日  期:
"""
import pytest


def setup_function():
    print("打开浏览器,输入地址")


def teardown_function():
    print("关闭浏览器")


@pytest.mark.run(order=2)
def test_shopping():
    print("购物测试用例")


@pytest.mark.run(order=1)
def test_login():
    print("登录测试用例")


@pytest.mark.run(order=4)
def test_order():
    print("下单测试用例")


@pytest.mark.run(order=3)
def test_add_cart():
    print("添加购物车")
