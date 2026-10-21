import pytest

from pages.login_page import LoginPage
from tools import DriverTools


@pytest.fixture(scope="function")
def login_page():
    # yield后面是返回值,这个函数有返回值，
    driver=DriverTools().get_driver()
    page=LoginPage(driver)
    yield page
    DriverTools.quit_driver()