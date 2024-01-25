from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException,StaleElementReferenceException
from selenium.common import exceptions
import time

import re 



class PANTIP_Automation:
    def __init__(self) -> None:
        self.driver = self.initialize_driver()
        self.driver.set_window_size(1500,1328)


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
         
            time.sleep(3)
            # elem_list = WebDriverWait(self.driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, "//*[@id='gtm-topic-layout-headline']"))
            # ).click()
            
            elem.click()
            
            # elem_list.click()

            # time.sleep(3)
           
          
            # fine name katoo
            all_ul = "//ul[@class='pt-list pt-list-item__full-title pt-list__type-a']"
            ul_elememnt =WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, all_ul)))
            # Store the ID of the original window
            original_window = self.driver.current_window_handle
  
            #get number comment
            span_elements = ul_elememnt.find_elements(By.CLASS_NAME,"pt-li_stats-comment")
            for index,span_element in enumerate(span_elements):
                try:
                    desesired_text = re.sub(r"message", "", span_element.text)
                    print(desesired_text)
                    desesired_text = int(desesired_text)
                    if desesired_text >= 5:
                        #get post text and filter comment >5
                        
                    # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "h2")))
                        get_text = ul_elememnt.find_elements(By.TAG_NAME, "h2")[index]
                        print(get_text.text)
                        time.sleep(3)
                        
                        get_text.click()
                        print("just clicked")
                        #print(len(self.driver.window_handles))
                        self.driver.switch_to.window(self.driver.window_handles[1])

                        #get text in comment
                        get_id = "comments-jsrender"
                        
                        comments_container = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, get_id)))
                        #time.sleep(3)
                        all_comment_elements = comments_container.find_elements(By.XPATH, "//*[@class='display-post-story-wrapper comment-wrapper']")
                        
                        if all_comment_elements:
                            comment_texts = [element.text for element in all_comment_elements if element.text]
                            print(comment_texts)
                        else:
                            print("Comments container not found.")
                
                
                except exceptions.StaleElementReferenceException as e:
                        print(f"{e}Comments container not found within timeout.")       
                   
                        print("dearxoasis")
                            

                    
                    

             

                    # # get text in comment 
                    # all_comment = "display-post-story-wrapper comment-wrapper"
                    # #https://www.selenium.dev/documentation/webdriver/interactions/windows/
                              

         
               
                    
            # print(desired_text)
            assert "No results found." not in self.driver.page_source

        finally:
            #print("done")
            time.sleep(3)
            self.driver.quit()  # Close the browser gracefully





if __name__ == "__main__":
    pantip = PANTIP_Automation()
    pantip.get_fav()