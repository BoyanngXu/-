from selenium import webdriver
from PIL import Image
import ddddocr,time

url1 = 'https://i.sjtu.edu.cn/jaccountlogin'
url2 = 'https://i.sjtu.edu.cn/xspjgl/xspj_cxXspjIndex.html?doType=details&gnmkdm=N401605&layout=default&su=521072910031'


chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = chrome_options)
driver.get(url1)

driver.find_element_by_id('user').send_keys('admin')
driver.find_element_by_id('pass').send_keys('123456')

driver.save_screenshot('E://1.png')
capt = driver.find_element_by_id('captcha-img')
left = capt.location['x']
top = capt.location['y']
right = left + capt.size['width']
bottom = top + capt.size['height']
pic = Image.open(r'E://1.png')
pic = pic.crop((left + 420, top + 150 , right + 500, bottom + 200))
pic.save(r'E://1.png')

ocr = ddddocr.DdddOcr()
with open("E://1.png", 'rb') as f:
    image = f.read()
res = ocr.classification(image)
driver.find_element_by_id('captcha').send_keys(res)
driver.find_element_by_id('submit-button').click()
driver.get(url2)

for i in range(2,18):
    # xpath = "//*[@id='"+str(i)+"']"
    # driver.find_element_by_xpath(xpath).click()
    time.sleep(5)
    for j in range(1,7):
        for k in range(1,4):
            xpath = "//*[@id='ajaxForm1']/div[2]/div[1]/div[2]/table["+str(j)+"]/tbody/tr["+str(k)+"]/td[2]/div/div[1]/label/input"
            time.sleep(0.5)
            driver.find_element_by_xpath(xpath).click()
    xpath = "//*[@id='ajaxForm1']/div[2]/div[1]/div[2]/table[7]/tbody/tr/td[2]/div/div[1]/label/input"
    driver.find_element_by_xpath(xpath).click()
    time.sleep(0.5)
    xpath = "//*[@id='ajaxForm1']/div[2]/div[1]/div[2]/table[8]/tbody/tr/td[2]/div/div/textarea"
    driver.find_element_by_xpath(xpath).send_keys("谢谢老师，从您的课中受益良多，您辛苦了！")
    time.sleep(0.5)
    xpath = "//*[@id='ajaxForm1']/div[2]/div[1]/div[2]/table[8]/tbody/tr[2]/td[2]/div/div/textarea"
    driver.find_element_by_xpath(xpath).send_keys("谢谢老师，从您的课中受益良多，您辛苦了！")
    time.sleep(0.5)
    xpath = "//*[@id='btn_xspj_bc']"
    driver.find_element_by_xpath(xpath).click()

