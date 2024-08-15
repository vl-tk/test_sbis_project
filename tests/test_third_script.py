from selenium.webdriver.common.by import By
from pathlib import Path
from pages.home_page import HomePage
from utils.locators import HomePageLocators, DownloadPageLocators


def test_third_script(browser):
    home_page = HomePage(browser)
    home_page.open("https://sbis.ru/")

    menu_button = home_page.find(HomePageLocators.DOWNLOAD_LOCAL_LINK)
    menu_button.click()

    download_link = home_page.find(DownloadPageLocators.DOWNLOAD_LINK)
    download_link.click()

    filename = download_link.get_attribute("href").split("/")[-1]
    home_page.wait_for_file(Path.cwd(), filename)

    file_path = Path.cwd() / filename

    assert Path(file_path).exists()
    assert round(Path(file_path).stat().st_size / 1048576, 2) == 11.05
