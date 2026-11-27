from playwright.sync_api import Playwright
import pytest


@pytest.fixture(scope="session", autouse=True)
def use_saucedemo_test_ids(playwright: Playwright) -> None:
    playwright.selectors.set_test_id_attribute("data-test")
