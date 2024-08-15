from pages.home_page import HomePage
from utils.locators import (
    HomePageLocators,
    ContactsPageLocators,
    TensorPageLocators,
    TensorAboutPageLocators,
)


def test_first_script(browser):
    home_page = HomePage(browser)
    home_page.open("https://sbis.ru/")

    menu_button = home_page.find(HomePageLocators.CONTACTS_LINK)
    menu_button.click()

    banner = home_page.find(ContactsPageLocators.BANNER)
    banner.click()

    home_page.switch_to_opened_tab()

    home_page.wait_element(TensorPageLocators.STRENGTH_IN_PEOPLE)
    index_card = home_page.find(TensorPageLocators.STRENGTH_IN_PEOPLE)
    assert index_card.is_displayed()

    more_link = home_page.find(
        TensorPageLocators.STRENGTH_IN_PEOPLE_MORE_LINK,
    )
    browser.execute_script("arguments[0].click();", more_link)
    assert home_page.url == "https://tensor.ru/about"

    images = home_page.find_elements(TensorAboutPageLocators.IMAGES)

    assert images[0].get_attribute("height") == images[1].get_attribute("height")
    assert images[0].get_attribute("width") == images[1].get_attribute("width")
    assert images[1].get_attribute("height") == images[2].get_attribute("height")
    assert images[1].get_attribute("width") == images[2].get_attribute("width")
    assert images[2].get_attribute("height") == images[3].get_attribute("height")
    assert images[2].get_attribute("width") == images[3].get_attribute("width")
