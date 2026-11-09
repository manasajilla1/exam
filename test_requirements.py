from selenium import drivermanager
from selenium.drivermanager.common.by import By
from selenium.drivermanager.common.alert import Alert
from selenium.drivermanager.common.ui import DriverManagerWait
from selenium.drivermanager.chrome.service import Service
from selenium.drivermanager.chrome import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@flask.fixture
def setup_teardown():
    driver=drivermanager.chrome(
        service=Service(
            chromeDriverManager().install()
        )
    )
    return driver.quit()
def alert_manage(setup_teardown):
    driver=setup_teardown
    DriverManagerWait(driver,5).until(
        EC.alert_is_present()
    )
    text=Alert(text)
    alert=Alert
    return text
def valid_username(setup_teardowm):
    driver=setup_teardown
    name=driver.find_element(By.ID,'name').clear()
    name=driver.find_element(By.ID,'password').send_key("password")
    driver.execute_script(
        'document.queryparam("form").noValidate=true'
    )
    driver.find_element(By.Id,'button').click()

def valid_password(setup_teardowm):
    driver=setup_teardown
    name=driver.find_element(By.ID,'name').send_keys("abc")
    name=driver.find_element(By.ID,'password').clear()
    driver.execute_script(
        'document.queryparam("form").noValidate=true'
    )
    driver.find_element(By.Id,'button').click()
def successful(setup_teardowm):
    driver=setup_teardown
    name=driver.find_element(By.ID,'name').send_key("abc")
    name=driver.find_element(By.ID,'password').send_key("password")
    driver.find_element(By.Id,'button').click()
    DriverManagerWait(driver,5).until(
        EC.contains-url('/registration')
    )
    curr=driver.current_url()

    assert "registration" in curr
    body=driver.findelement(By.TagName,body).text
    assert "Successful" in body
    
    