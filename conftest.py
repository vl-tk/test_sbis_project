import pytest
from selenium import webdriver
from pathlib import Path
import os


@pytest.fixture()
def browser():
    download_dir = str(Path.cwd().absolute())

    options = webdriver.ChromeOptions()

    prefs = {}
    prefs["profile.default_content_settings.popups"] = 0
    prefs["download.default_directory"] = download_dir
    options.add_experimental_option("prefs", prefs)

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    browser.maximize_window()
    yield browser
    browser.quit()
    downloaded_files = [f for f in os.listdir(download_dir) if f.endswith(".exe")]
    for f in downloaded_files:
        Path(f).unlink()
