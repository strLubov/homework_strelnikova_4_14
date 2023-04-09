import pytest
from selene import browser


@pytest.fixture(params=['desktop', 'mobile'])
def setup_browser(request):
    if request.param == "desktop":
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        browser.open('https://github.com/')
    if request.param == "mobile":
        browser.config.window_width = 540
        browser.config.window_height = 960
        browser.open('https://github.com/')


@pytest.mark.parametrize("setup_browser", ['desktop'], indirect=True)
def test_github_desktop(setup_browser):
    browser.element('[href="/login"]').click()


@pytest.mark.parametrize("setup_browser", ['mobile'], indirect=True)
def test_github_mobile(setup_browser):
    browser.element('.Button-content div:nth-child(1)').click()
    browser.element('[href="/login"]').click()

