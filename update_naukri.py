from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import traceback

# ==== Setup Chrome Options ====
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: Remove for debugging
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)

# ==== Initialize Driver ====
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15)

try:
    print("Opening Naukri login page...")
    driver.get("https://www.naukri.com/nlogin/login")

    # ==== Wait and login ====
    print("Waiting for login fields...")
    wait.until(EC.presence_of_element_located((By.ID, "usernameField")))

    username = os.getenv("NAUKRI_EMAIL")
    password = os.getenv("NAUKRI_PASSWORD")

    if not username or not password:
        raise ValueError("❌ Naukri credentials not set in environment variables.")

    driver.find_element(By.ID, "usernameField").send_keys(username)
    driver.find_element(By.ID, "passwordField").send_keys(password)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()

    time.sleep(5)  # Wait for redirect
    print("✅ Logged in successfully.")

    # ==== Navigate to Profile Page ====
    profile_url = "https://www.naukri.com/mnjuser/profile"
    driver.get(profile_url)
    time.sleep(5)
    print("📄 Navigated to Profile Page.")

    # ==== Upload Resume ====
    resume_path = os.path.join(os.getcwd(), "Lokesh_Resume.pdf")
    if not os.path.exists(resume_path):
        raise FileNotFoundError(f"❌ Resume file not found at {resume_path}")

    # print(f"Current URL: {driver.current_url}")
    print("Till Here")
    upload_button = driver.find_element(By.XPATH, "//input[@id='attachCV']")
    upload_button.send_keys(resume_path)
    print("Then Here")
    #upload_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="attachCV"]')))
    #upload_input.send_keys(resume_path)

    time.sleep(5)
    print("📤 Resume uploaded successfully!")

except Exception as e:
    print("❌ Error occurred:")
    traceback.print_exc()

finally:
    driver.quit()
    print("🔚 Browser closed.")



