import pytest


@pytest.fixture()
def setup1():
    print("open brower")
    print("login")
    yield
    print("logout")
    print("close brower")


#@pytest.fixture(autouse=True)
#def setup():
# """it will call this function without passing setup name as parent class"""
#    print("open brower")
#    print("login")
#    yield
#    print("logout")
#    print("close brower")

#@pytest.fixture(scope='session')
#def setup():
#    """all the test cases will be executed first then yield function will be executed
#    scopes = function/session/class/module/package"""
#    print("open brower")
#    print("login")
#    yield
#    print("logout")
#    print("close brower")



######################### type 3 #########################################3

# conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use: chrome or firefox"
    )

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope='session', autouse=True)
def setup(browser):
    if browser == "chrome":
        print("\n[SETUP] launching chrome")
    elif browser == "firefox":
        print("\n[SETUP] launching firefox")
    else:
        print(f"\n[SETUP] Unknown browser: {browser}")
    yield
    print("\n[TEARDOWN] closing browser")