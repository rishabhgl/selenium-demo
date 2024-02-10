from locator import *
from element import SearchBarElement



class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    search_bar = SearchBarElement()

    def title_matches(self):
        return "Python" in self.driver.title
    
    def click_goto_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()
    
class SearchResultsPage(BasePage):

    def found_results(self):
        return "No results found." not in self.driver.page_source   