from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException,StaleElementReferenceException
import pandas as pd 


import time
import re 



class PANTIP_Automation:
    def __init__(self) -> None:
        self.driver = self.initialize_driver()
        self.driver.set_window_size(1700,1500)


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
            elem.click()
            
           
          
            # fine name katoo
            all_ul = "//ul[@class='pt-list pt-list-item__full-title pt-list__type-a']"
            ul_elememnt =WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, all_ul)))
            # Store the ID of the original window
            original_window = self.driver.current_window_handle
  
            #get number comment
            span_elements = ul_elememnt.find_elements(By.CLASS_NAME,"pt-li_stats-comment")

            #keep data frame 
            data_frame_title = {}
            data_frame_comment = {}
            for span_element in (span_elements):
                # try:
                    try:
                        desesired_text = re.sub(r"message", "", span_element.text)
                        print(desesired_text)
                        desesired_text = int(desesired_text)
                        #fileter number comment
                        if desesired_text >= 2:
                       

                            #loop all comment to get posts text and text comments 
                            x_path = "//div[@class='pt-list-item__title']/h2/a[@class='gtm-latest-topic gtm-topic-layout-compact gtm-topic-type-filter-favorite']"
                            h2_elements = ul_elememnt.find_elements(By.XPATH, x_path)

                            for element in h2_elements:

                                print(element.text)
                                #add to dataframe
                                data_frame_title.setdefault("title",[]).append(element.text)

                                print(data_frame_title)
                                self.driver.execute_script("arguments[0].click();", element)
                                time.sleep(3)
                                self.driver.execute_script('window.scrollTo(0, 1000)')
                                time.sleep(3)
                                self.driver.switch_to.window(self.driver.window_handles[1])

                                #get text in comment
                                get_id = "comments-jsrender"
                                
                                comments_container = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, get_id)))
                                time.sleep(3)
                                all_comment_elements = comments_container.find_elements(By.XPATH, "//*[@class='display-post-story-wrapper comment-wrapper']")
                            
                                #loop all comment to list 
                                if all_comment_elements:
                                    comment_texts = [element.text for element in all_comment_elements if element.text]
                                    print(len(comment_texts))
                                    scaped_comment_dict = {"comment":comment_texts}
                                    time.sleep(3)
                                    self.driver.close()
                                    self.driver.switch_to.window(original_window)

                                else:
                                    print("Comments container not found.")


                    except StaleElementReferenceException:
                        print("Element became stale, refreshing...")
                        break
                   
                     

                    
                    

    
                              

         
               
                    
      
            assert "No results found." not in self.driver.page_source

        finally:
            time.sleep(3)
            self.driver.quit()  # Close the browser gracefully





if __name__ == "__main__":
    pantip = PANTIP_Automation()
    pantip.get_fav()