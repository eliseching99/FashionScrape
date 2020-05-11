from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
import urllib.request



driver = webdriver.Chrome(executable_path="/Users/eliseching/Downloads/webScraping/chromedriver")

url="https://cottonon.com/MY/sale/sale-womens/"
driver.get(url)
SCROLL_PAUSE_TIME = 10

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
y = 1000
for timer in range(0,30):
    driver.execute_script("window.scrollTo(0, "+str(y)+")")
    y += 1000  
    time.sleep(1)

#get number of clothes on the page
numberOfClothesID= "search-result-items"
numberOfClothes=driver.find_element_by_id(numberOfClothesID).text
print("Number Of Clothes on this page : "+ driver.find_element_by_id(numberOfClothesID).get_attribute("data-total-page-tiles"))
#print(numberOfClothes)

listofitems=driver.find_element_by_id(numberOfClothesID)
elems=listofitems.find_elements_by_tag_name("li")
print(elems)
print(len(elems))
#for img in elems:
#    print(img.find_element_by_class_name("thumb-link").get_attribute("src"))

#print(elems)
#print(elems[0].find_element_by_class_name("product-tile").get_attribute("id"))
#imageid=(elems[0].find_element_by_class_name("product-tile").get_attribute("id"))
#imageid='"'+imageid+'"'
#exampleimgsrc=driver.find_element_by_id(imageid).text
#print(exampleimgsrc)
#imageeee=driver.find_element_by_xpath('//*[@id='+imageid+"]/div[2]/a/img").get_attribute("src")
#print(imageeee)

#//*[@id="0f8eb7f122c7e8ce2fd6913be4"]/div[2]/a/img
#//*[@id="e56f5d242ec7cffc5a45c5f522"]/div[2]/a/img
#
# for i in range(len(elems)):
#     image=elems[i].find_element_by_class("product-tile").find_element_by_class("product-image").find_element_by_class("thumb-link").get_attribute("src")
#     print(image)
counter=1
for img in elems:
    
    print(counter)
    counter=counter+1
    imageidori=img.find_element_by_class_name("product-tile").get_attribute("id")
    imageid='"'+imageidori+'"'
    imagesrc=driver.find_element_by_xpath('//*[@id='+imageid+"]/div[2]/a/img").get_attribute("src")
    urllib.request.urlretrieve(imagesrc, str(imageidori)+".jpg")


    print(imagesrc)



    


