import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select  # Add this import statement for Select class

# Setting up the webdriver
driver = webdriver.Chrome()

#01 Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")

# Waiting for page to load
driver.implicitly_wait(10)

#02 Clicking on the Fashion Main element
additional_element = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[10]")
additional_element.click()

# Waiting for the page to load
driver.implicitly_wait(10)

#03 Clicking on the Sneakers into Fashion category
next_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div/section/div[2]/div/div/div/div/ol/li[3]/a/div/img")
next_element.click()

# Waiting for the page to load
driver.implicitly_wait(10)

#04 Choosing a specific women sneaker among multiple
next_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[3]/div/div/div/div[3]/div[1]/span/div/div/div[2]/div/span/a/div/img")

next_element.click()

# Waiting for the page to load
driver.implicitly_wait(10)

#05 Selecting the size from dropdown menu
select_element = driver.find_element(By.ID, "native_dropdown_selected_size_name") #Id value defined
select = Select(select_element)
select.select_by_value("13,B09VCK8FW8")

# Waiting for the page to load
time.sleep(12)  # Pause for 12 seconds

#06 Locating the element using the new XPath after selecting size only user can see See All Buying Options with different company
try:
    wait = WebDriverWait(driver, 10)
    element_to_click = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'See All Buying Options')]")))
    element_to_click.click()
except TimeoutException:
    print("Element not found or not clickable within the specified timeout period")

#07 Add any additional actions we need to perform after clicking the element
try:
    wait = WebDriverWait(driver, 10) #Performing Try and catch method
    input_element = wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/span/span/span/div/div/div[4]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/span//*[local-name()='input']")))
    aria_label = input_element.get_attribute('aria-label')
    print("Aria Label of the Input Element: ", aria_label)

    # Perform actions as needed with the input element
    # For example, you can click on the input element
    input_element.click()

    # Or you can retrieve other attributes like the 'data-csa-c-id'
    data_csa_c_id = input_element.get_attribute('data-csa-c-id')
    print("Data-csa-c-id: ", data_csa_c_id)

except TimeoutException:
    print("Input Element not found within the specified timeout period")

time.sleep(10)  # Pause for 10 seconds
# Close the browser
driver.quit()