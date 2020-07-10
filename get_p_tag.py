from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

import cv2

import math

chromedriver_path = "C:\\Users\\Dhanvi\\Headless_Browsers\\chromedriver"

chrome_options = Options()
chrome_options.add_argument("--headless")

web_driver = webdriver.Chrome(executable_path=chromedriver_path,options=chrome_options)

url = "file:///C:/Users/Dhanvi/pdf_data/5b7c7eda-bf64-11ea-8b25-0cc47a792c0a_id_5b7c7eda-bf64-11ea-8b25-0cc47a792c0a.html"

with web_driver as driver:
    wait = WebDriverWait(driver,20)
    driver.get(url)
    wait.until(presence_of_element_located((By.TAG_NAME,"div")))
    print("waiting finished")
    html=driver.find_elements_by_tag_name("html")[0]
    print(html.rect)
    body = driver.find_elements_by_tag_name("body")[0]
    print(body.rect)
    x=html.location['x']
    y=html.location['y']
    width = int(html.size['width']*2.12)
    height = int(html.size['height']*3.8983)
    image = cv2.imread("C:\\Users\\Dhanvi\\pdf_data\\20695_2010_8_1501_20635_Judgement_17-Feb-2020\\20695_2010_8_1501_20635_Judgement_17-Feb-2020-01.jpg")
    cv2.rectangle(image,(x,y),(x+width,y+height),(255,0,0),2)
    cv2.imwrite("editedPage.jpg",image)
    total_divs = []
    i=1
    while True:
        try:
            div = driver.find_element_by_xpath("/html/body/div["+str(i)+"]")
            print("/html/body/div["+str(i)+"]")
            total_divs.append(div)
            i+=1
        except :
            break
    print(len(total_divs))
    #divs = driver.find_elements_by_tag_name("div")
    div1 = total_divs[0]
    print(div1.size)
    print(div1.location)
    divs = div1.find_elements_by_tag_name("div")
    print(len(divs))
    for i,div in enumerate(divs):
        add_x = div.location['x']
        add_y = div.location['y']
        add_width = div.size['width']
        add_height = div.size['height']
        # print(div.location)
        # print(div.size)
        x=div.location['x']
        y=div.location['y']
        width=int(div.size['width']*2.12)
        height=int(div.size['height']*3.8983)
        cv2.rectangle(image,(x,y),(x+width,y+height),(255,0,0),2)
        cv2.imwrite('editedPage.jpg',image)
        div_text = div.text
        span = div.find_elements_by_tag_name("span")
        sups = div.find_elements_by_tag_name("sup")
        subs = div.find_elements_by_tag_name("sub")
        for sup in sups:
            div_text = div_text.replace(sup.text,"")
        for sub in subs:
            div_text = div_text.replace(sub.text,"")
        print(div_text)
        # if(len(span)>0):
            # location = span[0].location
            # size = span[0].size
            # print(span[0].text)
            # print(size)
            # print(location)
            # print(span[0].rect)
            # x = math.ceil(location['x']*2.25)
            # y = math.ceil(div.location['y']*2.75)
            # width = math.ceil(div.size['width']*2.75)
            # height = math.ceil(div.size['height']*2.75)
            # cv2.rectangle(image,(x,y),(x+width,y+height),(255,0,0),2)
            # cv2.imwrite("editedPage.jpg",image)
    # for div in total_divs[:5]:
    #     divs = div.find_elements_by_tag_name("div")
    #     for div2 in divs[:5]:
    #         span = div2.find_elements_by_tag_name("span")
    #     if(len(span)>0):
    #         print(span[0].text)
    #         print(span[0].location)
    #         print(span[0].size)
    # print(len(divs))
    driver.quit()

    # /html/body/div[1]
    # /html/body/div[2]
    # #/html/body/div[3]
    # /html/body/div[3]
