# Send Email with Selenium RPA
from selenium import webdriver

path = 'C:\Python projects\email-selenium\chromedriver.exe'

driver = webdriver.Chrome(path)
url = 'https://account.proton.me/login'
driver.get(url)

# Input email
driver.implicitly_wait(5)
email = 'automatizacion.python@proton.me'
email_account = driver.find_element("xpath",'//*[@id="username"]')
email_account.send_keys(email)

# Wait time
driver.implicitly_wait(5)

# Input password
password = 'mechavarria'
password_input = driver.find_element("xpath",'//*[@id="password"]')
password_input.send_keys(password)

# Next button
button_next = driver.find_element("xpath",'/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/button')
button_next.click()

# Wait load time (Proccess for the login sesion)
driver.implicitly_wait(60)

compose_button = driver.find_element("xpath",'/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div[2]/button')
compose_button.click()

# Wait load time (for compose section)
driver.implicitly_wait(5)

# Destination Email
to = driver.find_element("xpath",'/html/body/div[1]/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div/input')
to.send_keys('automatizacion.python@proton.me')

# Subject
subject = driver.find_element("xpath",'/html/body/div[1]/div[4]/div/div/div/div/div/div[3]/div/div/input')
subject.send_keys('Email con bot RPA')

# Send button
button_send = driver.find_element("xpath",'/html/body/div[1]/div[4]/div/div/div/footer/div/div[1]/button')
button_send.click()

button_re = driver.find_element("xpath",'/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div[4]/nav/div/ul/li[1]/a')
button_re.click()

div = driver.find_element("xpath",'/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div/main/div/div[1]/div/div[2]')
div.click()