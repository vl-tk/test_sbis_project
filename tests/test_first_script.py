from selenium.webdriver.common.by import By

from pages.home_page import HomePage


def test_first_script(browser):
    home_page = HomePage(browser)
    home_page.open("https://sbis.ru/")

    menu_button = home_page.find(By.LINK_TEXT, "Контакты")
    menu_button.click()

    banner = home_page.find(
        By.CLASS_NAME,
        "sbisru-Contacts__logo-tensor",
    )
    banner.click()

    home_page.switch_to_opened_tab()

    home_page.wait_element(
        By.CLASS_NAME,
        "tensor_ru-Index__card-title",
    )
    index_card = home_page.find(
        By.CLASS_NAME,
        "tensor_ru-Index__card-title",
    )
    assert index_card.is_displayed()

    more_link = home_page.find(
        By.CSS_SELECTOR,
        "div[class='tensor_ru-Index__block4-content tensor_ru-Index__card'] a[class='tensor_ru-link tensor_ru-Index__link']",
    )
    browser.execute_script("arguments[0].click();", more_link)
    assert home_page.url == "https://tensor.ru/about"

    images = home_page.find_elements(
        By.CSS_SELECTOR,
        "div[class='tensor_ru-About__block3-image-wrapper'] img",
    )

    assert images[0].get_attribute("height") == images[1].get_attribute("height")
    assert images[0].get_attribute("width") == images[1].get_attribute("width")

    assert images[1].get_attribute("height") == images[2].get_attribute("height")
    assert images[1].get_attribute("width") == images[2].get_attribute("width")

    assert images[2].get_attribute("height") == images[3].get_attribute("height")
    assert images[2].get_attribute("width") == images[3].get_attribute("width")
