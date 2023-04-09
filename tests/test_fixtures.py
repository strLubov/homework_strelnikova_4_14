import pytest
from selene import browser


@pytest.fixture()
def setup_desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://github.com/')


@pytest.fixture()
def setup_mobile():
    browser.config.window_width = 540
    browser.config.window_height = 960
    browser.open('https://github.com/')


def test_github_desktop(setup_desktop):
    browser.element('[href="/login"]').click()
    browser.element('[.main-header]')


def test_github_mobile(setup_mobile):
    browser.element('.Button-content div:nth-child(1)').click()
    browser.element('[href="/login"]').click()
