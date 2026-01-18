
import os
import time
from datetime import datetime

import pytest
from selenium import webdriver


import pytest
import os
from datetime import datetime

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            reports_dir = "reports"
            screenshots_dir = os.path.join(reports_dir, "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join(screenshots_dir, screenshot_name)

            driver.save_screenshot(screenshot_path)

            # 🔑 RELATIVE path for HTML report
            relative_path = os.path.join("screenshots", screenshot_name)

            pytest_html = item.config.pluginmanager.getplugin("html")
            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.image(relative_path))
            report.extra = extra



# conftest.py
def pytest_configure(config):
    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    config.option.htmlpath = f"reports/report_{timestamp}.html"


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:100")
    time.sleep(3)
    yield driver
    driver.quit()
