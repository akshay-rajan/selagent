from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_chrome_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def get_title(url):
    driver = get_chrome_driver()
    driver.get(url)
    title = driver.title
    driver.quit()
    return title


def get_links(url):
    driver = get_chrome_driver()
    driver.get(url)
    links = [a.get_attribute('href') for a in driver.find_elements('tag name', 'a') if a.get_attribute('href')]
    driver.quit()
    return links


def get_meta_description(url):
    driver = get_chrome_driver()
    driver.get(url)
    desc = ''
    metas = driver.find_elements('tag name', 'meta')
    for meta in metas:
        name = meta.get_attribute('name')
        if name and name.lower() == 'description':
            desc = meta.get_attribute('content') or ''
            break
    driver.quit()
    return desc


def get_h1_texts(url):
    driver = get_chrome_driver()
    driver.get(url)
    h1s = [h1.text for h1 in driver.find_elements('tag name', 'h1')]
    driver.quit()
    return h1s


def get_images(url):
    driver = get_chrome_driver()
    driver.get(url)
    imgs = [img.get_attribute('src') for img in driver.find_elements('tag name', 'img') if img.get_attribute('src')]
    driver.quit()
    return imgs


def get_text_content(url):
    driver = get_chrome_driver()
    driver.get(url)
    body = driver.find_element('tag name', 'body')
    text = body.text
    driver.quit()
    return text
