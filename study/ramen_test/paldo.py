### chromedriver 사용해야 크롤링 가능 ###
 ## 팔도 영양성분 크롤링 ##


# google 홈페이지 '대한민국' 크롤링 #

from selenium import webdriver

driver = webdriver.Chrome("/Users/choeseunghui/Developer/chromedriver")
url = 'https://www.google.co.kr/'
driver.get(url)

# driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div[1]/div/div[1]/a").click()
#
# driver.find_element_by_xpath("//*[@id='gb']/div/div[1]/div/div[1]/a").click()

korea = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]").text

# print(korea)

driver.close()




