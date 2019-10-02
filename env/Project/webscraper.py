from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re


path_to_chromedriver = '/Users//yumo0/OneDrive/sanitySites/recipe-pyth-api/chromedriver_win32/chromedriver' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
url = 'https://www.rema.no/kampanjevarer/'
browser.get(url)

images = browser.find_elements_by_tag_name('img')
#browser.find_element_by_id('kundeavis.search').send_keys('stavanger')
#browser.find_element_by_id('kundeavis.search').send_keys(Keys.RETURN)
#python_button = browser.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/article/div[1]/div[1]/div/div/div/div[1]/div[1]/nav/ul/li[2]/a')
#python_button.click()
#Create a class to hold the object we wish to return, containing the name and link to the picture
class Item(object):
    def __init__(self, name, link):
        self.name = name
        self.link = link



#Go through all the images on the page and return any item that has the same name as our ingredient
for image in images:
    if(image.get_attribute('alt') == 'Farris'):
        it = Item(image.get_attribute('alt'), image.get_attribute('src'))
        print(it.link)

#Doesn't fully work yet, but is supposed to go through kundeavisene from rema and find the images so we can download them
'''
url = 'https://www.rema.no/kundeaviser/ff2abUV/'
browser.get(url)
python_element = browser.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div[2]/div/div[1]/div/div[1]/div')
string = re.search("(?P<url>https?://[^\s]+)", python_element.get_attribute('style')).group("url")
print(string)
'''

#coop obs
url = 'https://kundeavis.coop.no/aviser/obs/mariero/?id=2249&email=false'
browser.get(url)
python_obs_element = browser.find_element_by_xpath('//*[@id="menu_button_pdf"]/img')
python_obs_element.click()
browser.close()
