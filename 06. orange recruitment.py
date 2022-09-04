import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):  # TEST SCENARIO

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_add_candidates(self): 
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
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span").click() # klik menu Recruitment
        time.sleep(5)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click() # klik Add
        time.sleep(5)
        browser.find_element(By.NAME,"firstName").send_keys("Mito") #isi first name
        time.sleep(1)
        browser.find_element(By.NAME,"middleName").send_keys("") #isi middle name
        time.sleep(1)
        browser.find_element(By.NAME,"lastName").send_keys("Tsukino") #isi last name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input").send_keys("mito@2434.com") #isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[8]/button[2]").click() #klik tombol Save
        time.sleep(5)
        
        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
        text_bawah = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div[1]/form/h6").text

        self.assertIn('Recruitment', text_atas)
        self.assertEqual(text_bawah, 'Application Leave')
    
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
