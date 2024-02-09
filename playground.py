from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from utils import load_driver
import time

driver = load_driver(2, "https://www.github.com/rishabhgl")

# try:
#     result = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "SDkEP")))
#     search = result[0]
#     search.send_keys("selenium")
#     search.send_keys(Keys.RETURN)
#     time.sleep(5)
# finally:
#     driver.quit()

# nav_link = driver.find_element(By.LINK_TEXT, "Documentation")
# nav_link.click()

# nav_link2 = driver.find_element(By.LINK_TEXT, "Books")
# nav_link2.click()

# books = driver.find_element(By.TAG_NAME, "tr")
# print(books.text)

# driver.back()
# driver.forward()

elem = driver.find_element(By.CLASS_NAME, "repo")
print(elem.text)

actions = ActionChains(driver)
actions.scroll_to_element(elem).perform()


time.sleep(10)
driver.quit()

