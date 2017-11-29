from selenium import webdriver
# from selenium.common import By
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

try:
	chrome_options = Options()
	# chrome_options.binary_location ="/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe"
	driver = webdriver.Chrome()
	driver.implicitly_wait(1)
	driver.get("http://rldb.me")
	assert driver.title == "RLDB"
	print("[SUCCESS] The site is up")
	items_dropdown = driver.find_element_by_id("nav-dropdown")
	items_dropdown.click()
	crates_link = driver.find_element_by_link_text("Crates")
	crates_link.click()
	# header = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.tag_name, "h1")))
	header = driver.find_element_by_tag_name("h1")
	assert header.text == "Crates"
	print("[SUCCESS] The nav-bar link(s) works")
	image = driver.find_element_by_class_name("instance-card")
	image.click()
	print("[SUCCESS] The page has data, and it's clickable")
	header = driver.find_element_by_tag_name("h1")
	assert header.text == "Turbo Crate"
	print("[SUCCESS] The link doesn't 404")
	contains = driver.find_element_by_class_name("instance-card")
	print("[SUCCESS] Our model page links to other models")
	contains.click()
	print("[SUCCESS] The models are clickable")
	header = driver.find_element_by_tag_name("h1")
	assert header.text == "Kalos"
	print("[SUCCESS] And they take us to the pages of other models")
	print("[INFORMATION] Navigating to /players/...")
	driver.get("http://rldb.me/players")
	card_one_text = driver.find_element_by_class_name("player-card").text
	pagination = driver.find_element_by_class_name("pagination")
	page_button = driver.find_element_by_link_text("1")
	print("[SUCCESS] Pagination module is working. And...")	
	page_button = driver.find_element_by_link_text("2")
	print("[SUCCESS] We have multiple pages. And...")	
	page_button.click()
	header = driver.find_element_by_tag_name("h1")
	assert header.text == "Players"
	card_two_text = driver.find_element_by_class_name("player-card")
	assert card_two_text != card_one_text
	print("[SUCCESS] The pages have different data")
	fil = driver.find_element_by_class_name("Select-control")
	print("[SUCCESS] Filter module is working")
	paragraphs = driver.find_elements_by_tag_name("p")
	assert any(p.text == "Playstation" for p in paragraphs)
	filter_box = driver.find_element_by_xpath("//div[2]/input")
	filter_box.send_keys("steam\n")
	paragraphs = driver.find_elements_by_tag_name("p")
	assert all(p.text != "Playstation" for p in paragraphs)
	print("[SUCCESS] Filter actually filters")
	all_names = [name.text for name in driver.find_elements_by_tag_name("h2")]
	sorted_names = sorted(all_names)
	assert all_names != sorted_names
	driver.find_element_by_xpath("//div[3]//button").click()
	driver.find_element_by_link_text("Increasing").click()
	all_names = [name.text for name in driver.find_elements_by_tag_name("h2")]
	sorted_names = sorted(all_names)
	assert all_names == sorted_names
	print("[SUCCESS] Sort works")
	search_bar = driver.find_element_by_xpath("//div[2]/ul[2]//input")
	search_bar.send_keys("Turbo\n")
	driver.implicitly_wait(5)
	search_bar.submit()
	print("[SUCCESS] We have a search bar. And...")
	header = driver.find_element_by_tag_name("h1")
	assert header.text == "Search: Turbo"
	print("[SUCCESS] It searches. And...")
	link = driver.find_element_by_link_text("Turbo Crate")
	print("[SUCCESS] It returns relevant results")
	link.click()
	print("[SUCCESS] That take us to the proper pages")
	print("\n--------------------------------")
	print("TESTING COMPLETE. ALL TESTS PASS")
	print("--------------------------------\n")

	



except AssertionError as e:
	print("[FAIL] ")
	print(e)
except NoSuchElementException as e:
	print("[FAIL] ", e)
# except:
	# print("[ERROR] Unkown error encountered")

finally:
	print("Closing in 3 seconds...")
	time.sleep(3)
	driver.quit()