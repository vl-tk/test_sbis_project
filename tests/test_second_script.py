from pages.home_page import HomePage
from utils.locators import HomePageLocators, ContactsPageLocators


def test_second_script(browser):
    home_page = HomePage(browser)
    home_page.open("https://sbis.ru/")

    menu_button = home_page.find(HomePageLocators.CONTACTS_LINK)
    menu_button.click()

    region_selector = home_page.find(ContactsPageLocators.REGION_LINK)
    assert region_selector.text == "Омская обл."

    partners_list = home_page.find_elements(ContactsPageLocators.CONTACTS_LIST)
    assert partners_list != []

    region_selector.click()

    new_link = home_page.find(ContactsPageLocators.KAMCHATKA_ITEM)
    new_link.click()

    home_page.wait_element(ContactsPageLocators.KAMCHATKA_TITLE)

    # список партнеров стал для Камчатки
    partners_list = home_page.find_elements(ContactsPageLocators.CONTACTS_LIST)
    assert partners_list != []
    assert "Камчатка" in partners_list[0].text

    assert home_page.url == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"
    assert home_page.title == "СБИС Контакты — Камчатский край"
