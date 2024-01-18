

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

import re 
# driver = webdriver.Chrome()
# driver.get("https://pantip.com/tag/ยา")

# try:
#     # Wait for the title to contain "ยา" (expected title)
#     WebDriverWait(driver, 10).until(EC.title_contains("ยา"))

#     # Find the element using a more descriptive XPATH
#     elem = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//a[text()='คลังกระทู้โปรด']"))
#     )
#     elem.click()

#     # Ensure "No results found." is not present after clicking
#     assert "No results found." not in driver.page_source

# finally:
#     print("done")
    # driver.quit()  # Close the browser gracefully


class PANTIP_Automation:
    def __init__(self) -> None:
        self.driver = self.initialize_driver()


    def initialize_driver(self) -> webdriver.Chrome:
        option = Options()
        option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=option)

        return driver
    

    def get_fav (self):
        self.driver.get("https://pantip.com/tag/ยา")
        try:
            # Wait for the title to contain "ยา" (expected title)
            WebDriverWait(self.driver, 10).until(EC.title_contains("ยา"))

            # click คลังกระทู้โปรด
            elem = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='คลังกระทู้โปรด']"))
            )
           
            elem.click()
            # fine name katoo
            all_ul = "//ul[@class='pt-list pt-list-item__full-title pt-list__type-a']"
            ul_elememnt =WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, all_ul)))
            
            #get number comment
            for index,span_element in enumerate(ul_elememnt.find_elements(By.CLASS_NAME,"pt-li_stats-comment")):
                desesired_text = re.sub(r"message", "", span_element.text)
                desesired_text = int(desesired_text)
                if desesired_text >= 5:
                    #get post text and filter comment >5
                    get_text = ul_elememnt.find_elements(By.TAG_NAME, "h2")[index]
                    print(get_text.text)
                    time.sleep(3)
                    get_text.click()

                    # get text in comment 
                    all_comment = "display-post-story-wrapper comment-wrapper"
                    #https://www.selenium.dev/documentation/webdriver/interactions/windows/
                   

         
               
                    
            # print(desired_text)
            assert "No results found." not in self.driver.page_source

        finally:
            #print("done")
            time.sleep(3)
            self.driver.quit()  # Close the browser gracefully





if __name__ == "__main__":
    pantip = PANTIP_Automation()
    pantip.get_fav()