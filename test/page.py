class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class Main(BasePage):

    def title_matches(self):
        return "Python" in self.driver.title
    
    