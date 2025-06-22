import os
from datetime import datetime
from linebot import LineBotApi
from linebot.models import FlexSendMessage
from screenshot import capture_heat_image
from flex_builder import build_flex

def upload_image_and_get_url(local_path):
    # 建議改為 imgur / S3 / 自建圖床上傳
    # 暫時模擬回傳靜態網址
    return "https://your-server.com/" + local_path

def main():
    image_path = capture_heat_image()
    image_url = upload_image_and_get_url(image_path)
    
    now_str = datetime.now().strftime("%m/%d %H:%M")
    flex = build_flex(image_url, now_str, level="第3級")

    line_bot_api = LineBotApi(os.environ["CHANNEL_ACCESS_TOKEN"])
    line_bot_api.push_message(os.environ["GROUP_ID"], FlexSendMessage(alt_text="今日熱危害", contents=flex))

if __name__ == "__main__":
    main()
