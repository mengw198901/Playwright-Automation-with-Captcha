#pip install ddddocr -i https://pypi.douban.com/simple

"""  
Image Identification
"""  
from playwright.sync_api import sync_playwright  
import ddddocr  
  
  
with sync_playwright() as p:  
    browser = p.chromium.launch(headless=False)  
    context = browser.new_context()  
    page = context.new_page()  
  
    page.goto('https://www.xxx.com/login')  
    page.locator("#email").fill('123@qq.com')  
    page.locator('#pwd').fill('111111')  
    # save it  
    page.locator('#imgCode').screenshot(path='yzm.png')  
  
    # identify  it
    ocr = ddddocr.DdddOcr(show_ad=False)  
    with open('yzm.png', 'rb') as f:  # open image
        img_bytes = f.read()  # read image
    yzm = ocr.classification(img_bytes)  # identify it
    print(f'the code is: {yzm }')  
  
    # fill it
    page.locator('#code').fill(yzm)  
  
  
    page.pause()
