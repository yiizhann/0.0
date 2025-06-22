from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from io import BytesIO
import time
import os

def capture_heat_image():
    # Setup headless Chrome
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1200x1000")

    driver = webdriver.Chrome(options=options)
    driver.get("https://hiosha.osha.gov.tw/content/info/heat1.aspx")
    
    time.sleep(5)  # 等待圖表載入
    screenshot = driver.get_screenshot_as_png()
    driver.quit()

    # 開啟圖片並裁切區域（left, top, right, bottom）
    img = Image.open(BytesIO(screenshot))
    cropped = img.crop((345, 260, 930, 580))
    cropped_path = "heat_crop.png"
    cropped.save(cropped_path)

    # 回傳圖檔網址（此處需對接圖床或 LINE Image Message 上傳 API）
    return cropped_path  # 或上傳後的網址
