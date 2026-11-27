from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
PRODUCT = "Sauce Labs Backpack"


def login(page: Page, password: str = PASSWORD) -> None:
    page.goto(f"{BASE_URL}/")
    page.get_by_test_id("username").fill(USERNAME)
    page.get_by_test_id("password").fill(password)
    page.get_by_test_id("login-button").click()


def test_login_page_is_displayed(page: Page) -> None:
    page.goto(f"{BASE_URL}/")
    for field in ("username", "password", "login-button"):
        expect(page.get_by_test_id(field)).to_be_visible()


def test_successful_login(page: Page) -> None:
    login(page)
    expect(page).to_have_url(f"{BASE_URL}/inventory.html")
    expect(page.get_by_test_id("title")).to_have_text("Products")


def test_catalog_is_displayed(page: Page) -> None:
    login(page)
    expect(page.get_by_test_id("inventory-list")).to_be_visible()
    product_name = page.get_by_test_id("inventory-item-name").filter(has_text=PRODUCT)
    expect(product_name).to_have_text(PRODUCT)


def test_add_product_to_cart(page: Page) -> None:
    login(page)
    page.get_by_test_id("add-to-cart-sauce-labs-backpack").click()
    expect(page.get_by_test_id("shopping-cart-badge")).to_have_text("1")
    page.get_by_test_id("shopping-cart-link").click()
    expect(page).to_have_url(f"{BASE_URL}/cart.html")
    item = page.get_by_test_id("inventory-item").filter(has_text=PRODUCT)
    expect(item.get_by_test_id("inventory-item-name")).to_have_text(PRODUCT)
    expect(item.get_by_test_id("item-quantity")).to_have_text("1")


def test_login_with_wrong_password(page: Page) -> None:
    login(page, password="wrong_password")
    expect(page.get_by_test_id("error")).to_contain_text(
        "Username and password do not match"
    )
    expect(page).to_have_url(f"{BASE_URL}/")
