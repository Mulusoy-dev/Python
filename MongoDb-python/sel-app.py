
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome('C:/Users/melih/Desktop/Python/MongoDb-python/chromedriver.exe')

url="https://github.com/"
driver.get(url)


searchInput=driver.find_element(By.NAME, "q")
searchInput.clear()
time.sleep(2)
searchInput.send_keys("python")
#searchInput.send_keys(Keys.RETURN)


searchInput.send_keys(Keys.ENTER)
time.sleep(2)




# result=driver.page_source
# print(result)



result_page=driver.find_elements(By.XPATH, "//*[@id='js-pjax-container']/div/div[3]/div/ul/li[1]/div[2]/div[1]/div[1]/a")
print(result_page[0].text)
# for element in result_page:
#     print(element.text)


driver.close()

