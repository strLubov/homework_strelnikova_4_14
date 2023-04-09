"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
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


def test_github_desktop(setup_browser):
    if setup_browser == 'desktop':
        browser.element('[href="/login"]').click()
    if setup_browser == 'mobile':
        pytest.skip()


def test_github_mobile(setup_browser):
    if setup_browser == 'mobile':
        browser.element('.Button-content div:nth-child(1)').click()
        browser.element('[href="/login"]').click()
    if setup_browser == 'desktop':
        pytest.skip()
