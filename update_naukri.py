from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

# Read credentials from environment variables
naukri_email = os.getenv('NAUKRI_EMAIL')
naukri_password = os.getenv('NAUKRI_PASSWORD')
resume_file_path = os.getenv('RESUME_PATH', 'resume.pdf')

options = Options()
options.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(options=options)

try:
    # Open Naukri Login Page
    driver.get('https://www.naukri.com/nlogin/login')

    # Login
    driver.find_element(By.ID, 'usernameField').send_keys(naukri_email)
    driver.find_element(By.ID, 'passwordField').send_keys(naukri_password)
    driver.find_element(By.XPATH, '//button[text()="Login"]').click()

    time.sleep(5)

    # Go to Profile Page
    driver.get('https://www.naukri.com/mnjuser/profile')

    time.sleep(5)

    # Click on the 'Upload' or 'Update' resume button
    upload_btn = driver.find_element(By.XPATH, '//input[@type="file"]')
    upload_btn.send_keys(os.path.abspath(resume_file_path))

    time.sleep(5)
    print("Resume uploaded successfully!")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
