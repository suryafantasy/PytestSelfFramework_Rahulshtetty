import pytest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver=None

@pytest.fixture(scope="class")
def setup(request):
    global driver
    service_obj = Service("C:/Users/0035BI744/Documents/Pycharm/chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    request.cls.driver=driver #assigning driver to cls in test_e2e file where cls.driver belongs to e2e file.
    yield  #tear down method execute at end
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)


