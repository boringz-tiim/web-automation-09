import pytest

from scripts import log
from tools import read_json


class TestLogin:
    arg_names="phone,pwd,code,expect_result"
    arg_values=read_json("login_data.json")
    @pytest.mark.parametrize(arg_names,arg_values)
    def test_01_login_success(self, login_page,phone,pwd,code,expect_result):
        """登录成功"""
        try:
            login_page.login(phone, pwd, code)
            if expect_result == "安全退出":
                result = login_page.get_success_result()
            else:
                result = login_page.get_failure_result()
            log.info(f"执行结果:{result}")
            assert expect_result in result
            login_page.get_shot("登录结果截图")
        except Exception as e:
            log.info(f"执行异常:{e}")
    # def test_02_login_fail(self, log):
    #     """手机格式不对"""
    #     log.login("1515425", "123456", "8888")
    #     result = log.get_failure_result()
    #     print("实际弹窗文字：", result)
    #     assert "账号格式不匹配" in result
    #     log.click_dialog_confirm()
    #
    # def test_03_login_fail(self, log):
    #     """使用未注册手机号"""
    #     log.login("13800000000", "123456", "8888")
    #     result = log.get_failure_result()
    #     print("实际弹窗文字：", result)
    #     assert "账号不存在" in result
    #     log.click_dialog_confirm()
    #
    # def test_04_login_fail(self, log):
    #     """密码错误"""
    #     log.login("15154251600", "654321", "8888")
    #     result = log.get_failure_result()
    #     print("实际弹窗文字：", result)
    #     assert "密码错误" in result
    #     log.click_dialog_confirm()
