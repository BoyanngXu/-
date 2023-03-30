from selenium import webdriver
from PIL import Image
import ddddocr,time,random
url = 'http://query.bjeea.cn/queryService/rest/score/103'

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get(url)

examNo = 50200000
examinneNo = "21110105100231"
idCard = "049849"

for i in range(1,3):
    examNo = examNo + 1
    driver.save_screenshot('1.png')
    capt = driver.find_element_by_name('captcha')
    left = capt.location['x']
    top = capt.location['y']
    right = left + capt.size['width']
    bottom = top + capt.size['height']
    pic = Image.open(r'1.png')
    pic = pic.crop((left+355,top+185,right+385,bottom+195))
    pic.save(r'1.png')
    driver.quit()

    ocr = ddddocr.DdddOcr()
    with open("1.png", 'rb') as f:
        image = f.read()
    res = ocr.classification(image)

    driver.find_element_by_name('captcha').send_keys(res)
    driver.find_element_by_id('examNo').send_keys("0"+ str(examNo))
    driver.find_element_by_id('examinneNo').send_keys(examinneNo)
    driver.find_element_by_id('idCard').send_keys(idCard)
    time.sleep(3+2*random.random())
    driver.find_element_by_id('queryBtn').click()