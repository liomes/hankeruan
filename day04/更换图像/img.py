from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:8080/HKR")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("linhaiwang")
driver.find_element_by_xpath("//*[@id='password']").send_keys("Lhw04030601")
driver.find_element_by_xpath("//*[@id='submit']").click()

path = driver.find_element_by_xpath('//*[@id="img"]').click()



driver.quit()