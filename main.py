from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/hamza/AppData/Local/Google/Chrome/User Data")

driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver,10)

ContactNoAskingList=[]
boolCheck=True

while boolCheck is True:
 ContactNoAsking=input("Enter the contact name: ")
 ContactNoAskingList.append(ContactNoAsking)
 if ContactNoAsking=="end":
     boolCheck=False





for contact in ContactNoAskingList:
 target=f'"{contact}"'



 text=input("Enter the Text Message: ")



 contact_path='//span[contains(@title,'+ target +')]'
 contact = wait.until(EC.element_to_be_clickable((By.XPATH, contact_path)))

 contact.click()
 message_box_XPATH='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
 message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_XPATH)))
 message_box.send_keys(text+Keys.ENTER)

 time.sleep(7)

driver.quit()