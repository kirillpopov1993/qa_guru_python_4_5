from selene.support.shared import browser
import pytest


@pytest.fixture(scope='session')
def browser_config():
    browser.config.hold_browser_open = True
    browser.config.window_width = 1920
    browser.config.window_height = 1080


