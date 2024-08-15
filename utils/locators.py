from selenium.webdriver.common.by import By


class HomePageLocators:
    CONTACTS_LINK = (By.LINK_TEXT, "Контакты")
    DOWNLOAD_LOCAL_LINK = (By.LINK_TEXT, "Скачать локальные версии")


class ContactsPageLocators:
    BANNER = (By.CLASS_NAME, "sbisru-Contacts__logo-tensor")
    REGION_LINK = (
        By.CSS_SELECTOR,
        "span[class='sbis_ru-Region-Chooser ml-16 ml-xm-0'] span[class='sbis_ru-Region-Chooser__text sbis_ru-link']",
    )
    CONTACTS_LIST = (By.CLASS_NAME, "sbisru-Contacts-List__item")
    KAMCHATKA_ITEM = (By.CSS_SELECTOR, "span[title='Камчатский край'] span")
    KAMCHATKA_TITLE = (
        By.XPATH,
        "//*[@id='city-id-2' and contains(text(),'Петропавловск-Камчатский')]",
    )


class TensorPageLocators:
    STRENGTH_IN_PEOPLE = (By.CLASS_NAME, "tensor_ru-Index__card-title")
    STRENGTH_IN_PEOPLE_MORE_LINK = (
        By.CSS_SELECTOR,
        "div[class='tensor_ru-Index__block4-content tensor_ru-Index__card'] a[class='tensor_ru-link tensor_ru-Index__link']",
    )


class TensorAboutPageLocators:
    IMAGES = (By.CSS_SELECTOR, "div[class='tensor_ru-About__block3-image-wrapper'] img")


class DownloadPageLocators:
    DOWNLOAD_LINK = (By.CSS_SELECTOR, ".sbis_ru-DownloadNew-loadLink__link")
