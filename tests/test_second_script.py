from selenium.webdriver.common.by import By
from pages.home_page import HomePage


def test_second_script(browser):
    home_page = HomePage(browser)
    home_page.open("https://sbis.ru/")

    menu_button = home_page.find(By.LINK_TEXT, "Контакты")
    menu_button.click()

    region_chooser = home_page.find(
        By.CSS_SELECTOR,
        "span[class='sbis_ru-Region-Chooser ml-16 ml-xm-0'] span[class='sbis_ru-Region-Chooser__text sbis_ru-link']",
    )
    assert region_chooser.text == "Омская обл."

    partners_list = home_page.find_elements(
        By.CLASS_NAME,
        "sbisru-Contacts-List__item",
    )
    assert partners_list != []

    region_chooser.click()

    new_link = home_page.find(By.CSS_SELECTOR, "span[title='Камчатский край'] span")
    new_link.click()

    home_page.wait_element(
        By.XPATH,
        "//*[@id='city-id-2' and contains(text(),'Петропавловск-Камчатский')]",
    )

    # список партнеров стал для Камчатки
    partners_list = home_page.find_elements(
        By.CLASS_NAME,
        "sbisru-Contacts-List__item",
    )
    assert partners_list != []
    assert "Камчатка" in partners_list[0].text

    assert home_page.url == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"
    assert home_page.title == "СБИС Контакты — Камчатский край"
