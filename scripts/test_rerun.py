"""
作  者:周小丽
文件名:
日  期:
"""
import random


class TestCart:

    def test_cart(self):
        print("这是添加购物车测试用例")
        assert True

    def test_cart_list(self):
        print("这是查看购物车列表测试用例")
        num = random.randint(0, 1)
        if num == 0:
            assert False
        else:
            assert True

    def test_cart_updata(self):
        print("这是更新购物车测试用例")
        assert True

    def test_cart_delete(self):
        print("这是删除购物车测试用例")
        assert True
