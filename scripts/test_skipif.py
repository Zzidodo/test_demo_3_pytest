"""
作  者:周小丽
文件名:
日  期:
"""
import pytest
import random

num = random.randint(1, 10)


@pytest.mark.skipif(condition=num % 2 == 0, reason="女生跳过")
def test_browser_electronic():
    """浏览电子产品"""
    print("浏览电子产品")


@pytest.mark.skipif(condition=num % 2 == 1, reason="男生跳过")
def test_browser_maquillage():
    """浏览化妆品"""
    print("浏览化妆品")
