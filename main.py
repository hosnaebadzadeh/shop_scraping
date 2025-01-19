from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ask = input("What do you want to search for on eBay?: ")

driver = webdriver.Chrome()
driver.get("https://www.ebay.com")

try:
    search_box = driver.find_element(By.ID, "gh-ac")
    search_box.send_keys(ask)
    search_box.send_keys(Keys.RETURN)

    while True:
        products = driver.find_elements(By.CSS_SELECTOR, ".s-item")
        print(f"Number of products found on this page: {len(products)}")

        for product in products:
            try:
                name = product.find_element(By.CSS_SELECTOR, ".s-item__title").text
                price = product.find_element(By.CSS_SELECTOR, ".s-item__price").text
                link = product.find_element(By.CSS_SELECTOR, ".s-item__link").get_attribute("href")
                description = product.find_element(By.CSS_SELECTOR, ".s-item__subtitle").text if product.find_elements(
                    By.CSS_SELECTOR, ".s-item__subtitle") else "No description available"
                try:
                    rating = product.find_element(By.CSS_SELECTOR, ".x-star-rating span").text
                except NoSuchElementException:
                    rating = "No rating"

                print("\nProduct Name:", name)
                print("Price:", price)
                print("Description:", description)
                print("Link:", link)
                print("Rating:", rating)

            except NoSuchElementException:
                continue

        # next page
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, ".pagination__next")
            next_button.click()
            time.sleep(2)
        except NoSuchElementException:
            print("No more pages.")
            break

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()

# https://github.com/hosnaebadzadeh

