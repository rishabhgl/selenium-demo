from utils import load_driver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

num_clicks = 5000

try:
    driver = load_driver(60, "https://orteil.dashnet.org/cookieclicker/")

    english_selector = driver.find_element(By.ID, "langSelect-EN")
    accept_cookies = driver.find_element(By.LINK_TEXT, "Got it!")

    accept_cookies.click()
    english_selector.click()

    cookie = driver.find_element(By.ID, "bigCookie")
    cookie_count = driver.find_element(By.ID, "cookies")
    products = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(2)]


    for i in range(num_clicks):
        cookie.click()
        count = int(cookie_count.text.split(" ")[0])
        for product in products:
            if ( count >= int(product.text)):
                buy_action = ActionChains(driver).move_to_element(product).click(product).perform()

finally:
    driver.quit()

