from dotenv import find_dotenv, load_dotenv
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

load_dotenv(find_dotenv())
LOGIN = os.getenv('LOGIN')
PSWRD = os.getenv('PSWRD')

driver = webdriver.Chrome()
driver.get("https://arminastudy.com/wp-login.php")
time.sleep(2)

login_input = driver.find_element(By.ID, 'user_login')
login_input.send_keys(LOGIN)

pswrd_input = driver.find_element(By.ID, 'user_pass')
pswrd_input.send_keys(PSWRD)

log_in = driver.find_element(By.ID, 'wp-submit')
log_in.click()
time.sleep(2)

profile_link = driver.find_element(By.CLASS_NAME, 'user-name')
profile_link.click()
time.sleep(2)

courses = driver.find_element(By.LINK_TEXT, 'Курсы')
courses.click()
time.sleep(2)

needed_course = driver.find_element(By.LINK_TEXT, 'Корейский | Интенсив')
needed_course.click()
time.sleep(2)

start_lesson = driver.find_element(By.CSS_SELECTOR, '.ld-item-name.ld-primary-color-hover')
start_lesson.click()
time.sleep(2)

lessons = driver.find_elements(By.CSS_SELECTOR, '.bb-lesson-head.flex')
for i in range(len(lessons)):
    lessons = driver.find_elements(By.CSS_SELECTOR, '.bb-lesson-head.flex')
    current_lesson = lessons[i]

    # # Прокрутка к текущему уроку
    # # driver.execute_script("arguments[0].scrollIntoView(true);", current_lesson)
    # driver.execute_script("arguments[0].click();", current_lesson)
    # #
    # # actions = ActionChains(driver)
    # # actions.move_to_element(current_lesson).click().perform()
    # time.sleep(1)

    current_lesson.click()
    time.sleep(2)

    title = driver.find_element(By.TAG_NAME, 'h1')
    none_symbols = ['/', ':', '<', '>', '*', '?', '"', '|']
    file_name = title.text
    for symb in none_symbols:
        if symb in file_name:
            file_name = file_name.replace(symb, '_')

    text_page = driver.find_element(By.CSS_SELECTOR, '.learndash-wrapper')

    with open(f'{file_name}.doc', 'w', encoding='UTF-8') as f:
        f.write(text_page.text)

    # driver.back()
    # time.sleep(2)  # Подождать некоторое время для обновления списка элементов
# new_page = driver.find_element(By.CSS_SELECTOR, '.next.ld-primary-color-hover')
# new_page.click()
