# **Whatsapp-GroupInfo-Extractor**
This is a subpart of WhatsApp business automation project that extract image receipts and user info from a WhatsApp business group-chat to process payment using Selenium WebDriver.


## **Prerequisites**

Before running the script, ensure you have the following:

- Python installed on your system (version 3.x recommended).
- Chrome web browser installed on your system.
- ChromeDriver installed and added to your system PATH.

## **Setup**

- Clone the repository:
```
git clone https://github.com/UmukoroG/Whatsapp-GroupInfo-Extractor.git

```
- Change directory to project location and Install the required dependencies:

```
pip install selenium

```
- Run the Script
```
python UserInfo.py

```

## **Result**
1. A Chrome window will open, and you will need to scan the QR code using your WhatsApp mobile app to log in.
Once logged in, the script will navigate to the WhatsApp Web page.
1. It will then locate the chat group with the name "TestGroup" (you can modify the GroupName variable in the script if needed) and open it.
1. The script will start downloading all the images from the chat and save them in a folder named by the current year and month, e.g., current_Dir/2023/07.
1. Each image will be saved with a filename like payment1.jpg, payment2.jpg, etc., in the corresponding folder.
1. The script will also print the username and phone number of the sender for each downloaded image.
