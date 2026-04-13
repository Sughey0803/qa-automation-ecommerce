from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_product_to_cart():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    # Instancias de páginas
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # 🔐 1. Login
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # 🛒 2. Agregar producto al carrito
    inventory_page.add_product_to_cart()

    # 🧭 3. Ir al carrito
    inventory_page.go_to_cart()

    # ✅ 4. Validar
    assert cart_page.is_product_in_cart()

    driver.quit()