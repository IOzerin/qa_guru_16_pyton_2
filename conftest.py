import pytest
from selene import browser


@pytest.fixture(scope="session")
def browser_for_fixtures():
    print("Браузер!")

    yield

    print("Закрываем браузер!")

@pytest.fixture(scope="session")
def setting_browser():
    browser.config.window_height = 600
    browser.config.window_width = 800

    yield

    browser.quit()