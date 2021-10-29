from selenium import webdriver
import time
#创建Goolg
driver = webdriver.Chrome()
#打开HKR
driver.get("http://localhost:8080/HKR")
driver.maximize_window()
#登录账户
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("jason")
driver.find_element_by_xpath("//*[@id='password']").send_keys("1234567")
driver.find_element_by_xpath("//*[@id='submit']").click()
#点击图片
driver.find_element_by_xpath("//*[@id='img']").click()
driver.find_element_by_xpath('//*[@id="ul_pic"]').click()
#更换图片
driver.find_element_by_xpath('//*[@id="ul_pic"]/li[8]/img').click()
#退出系统
time.sleep(5)
driver.quit()






