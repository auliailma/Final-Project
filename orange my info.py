import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):  # TEST SCENARIO

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_change_personal_detail(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(8)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(8)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span").click() # klik menu My Info
        time.sleep(8)
        browser.find_element(By.NAME,"firstName").send_keys(Keys.HOME,Keys.SHIFT,Keys.END) # clear first name field
        time.sleep(1)
        browser.find_element(By.NAME,"firstName").send_keys("Peach") # isi first name
        time.sleep(1)
        browser.find_element(By.NAME,"middleName").send_keys(Keys.HOME,Keys.SHIFT,Keys.END) # clear middle name field
        time.sleep(1)
        browser.find_element(By.NAME,"middleName").send_keys("John") # isi middle name
        time.sleep(1)
        browser.find_element(By.NAME,"lastName").send_keys(Keys.HOME,Keys.SHIFT,Keys.END) # clear last name field
        time.sleep(1)
        browser.find_element(By.NAME,"lastName").send_keys("John") # isi last name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input").send_keys(Keys.HOME,Keys.SHIFT,Keys.END) # clear nickname field
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input").send_keys("PJJ") # isi nickname
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click() # klik tombol Save
        time.sleep(8)

        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text

        self.assertIn('PIM', text_atas)
        self.assertEqual(text_bawah, 'Personal Details')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
