import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from config import CHROME_PROFILE_PATH


class WhatsAppDriver:
    def __init__(self, url):

        def extract_username_and_phone(chat_bubble):
            username_xpath = "//span[contains(@class, '_2ne0X')]"
            phone_number_xpath = "//span[contains(@class, 'WJuYU')]"
            
            username_element = chat_bubble.find_element(By.XPATH, username_xpath)
            phone_number_element = chat_bubble.find_element(By.XPATH, phone_number_xpath)
            
            username = username_element.text
            phone_number = phone_number_element.text
            
            return username, phone_number
        
        # start settup
        self.options = Options()
        self.options.add_argument(CHROME_PROFILE_PATH)

        # Set the executable path using Service
        chromedriver_path = '/userDir/chromedriver_mac_arm64/chromedriver'
        service = Service(chromedriver_path)

        self.browser = webdriver.Chrome(service=service, options=self.options)
        # end- keeps us logged in to whatsapp and by passes the QR scan

        self.browser.maximize_window()
        self.browser.get(url)
        self.browser.driver.implicitly_wait(30)
        self.GroupName = "TestGroup"
        self.groupEle = self.browser.find_element(By.XPATH,f"//span[contains(text(),'{self.GroupName}')]")
        self.groupEle.click()

        # Find all the image elements in the chat
        user_messages = self.browser.find_elements(By.XPATH, "//div[contains(@class,'cm280p3y')]//img[contains(@class,'jciay5ix')]")

        for i, message in enumerate(user_messages, 1):
            # Extract the sender's username and phone number from the chat bubble that has image v
            chat_bubble = message.find_element(By.XPATH, "..")
            username, phone_number = extract_username_and_phone(chat_bubble)

            # Get the image data from the 'src' attribute of the image element
            image_url = message.get_attribute("src")
            
            # Download the image content using the WebDriver's execute_script method
            image_data = self.browser.execute_script("""
                var xhr = new XMLHttpRequest();
                xhr.open('GET', arguments[0], false);
                xhr.send(null);
                if (xhr.status === 200) {
                    return xhr.responseText;
                }
            """, image_url)
            
            if image_data:
                # Get the current year and month for the file path
                current_year = time.strftime("%Y")
                current_month = time.strftime("%m")
                
                # Create the directory if it does not exist
                save_dir = os.path.join("/current_Dir/", current_year, current_month)
                os.makedirs(save_dir, exist_ok=True)
                
                # Define the file name and path where you want to save the image
                file_name = f"payment{i}.jpg"
                save_path = os.path.join(save_dir, file_name)
                
                # Save the image data to the specified path
                with open(save_path, 'wb') as f:
                    f.write(image_data.encode('utf-8'))
                    
                print(f"Image {i} saved successfully to: {save_path}")
                
                # Print the username and phone number for reference
                print(f"Sender's Username: {username}")
                print(f"Sender's Phone Number: {phone_number}")
            else:
                print(f"Failed to retrieve Image {i}.")

    


if __name__ == "__main__":
    whatsapp_driver = WhatsAppDriver("https://web.whatsapp.com/")
