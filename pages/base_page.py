from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, locator):
        return self.browser.find_element(*locator)

    def find_elements(self, locator):
        return self.browser.find_elements(*locator)

    def open(self, url):
        self.browser.get(url)

    @property
    def title(self):
        return self.browser.title

    @property
    def url(self):
        return self.browser.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.browser).move_to_element(element)
        hover.perform()

    def wait_element(self, locator):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.browser.quit()

    def switch_to_opened_tab(self):
        self.browser.switch_to.window(self.browser.window_handles[-1])

    def wait_for_file(self, download_dir, filename):
        try:
            WebDriverWait(self.browser, 30).until(
                lambda d: [f for f in os.listdir(download_dir) if f == filename]
            )
        except TimeoutException:
            assert False, "no files were downloaded within 30 seconds"
