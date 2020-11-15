from selenium import webdriver
from Security import private_Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time



class webscrapper():

    #global variables
    likes = []
    links = []
    driver: WebDriver

    #Initalizing the Web scrapper
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://instagram.com")


    def login(self):
        try:
            # Grab username and password paths
            ig_username = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
            ig_pass = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
            #Get Username and Password
            get_Private_Username = private_Keys()
            get_Private_Password =private_Keys()

            #Pass in private username and Password
            ig_username.send_keys(get_Private_Username.getUserName())
            ig_pass.send_keys(get_Private_Password.getPassWord())
            #Click on login button and wait for 10 seconds
            login_btn = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div'))
            login_btn.click()
            #Close the pop-ups
            pop_Up_btn = WebDriverWait(self.driver, 13).until(lambda driver: self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button'))
            pop_Up_btn.click()
            pop_Up_btn_2 = WebDriverWait(self.driver, 13).until(lambda driver: self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]'))
            pop_Up_btn_2.click()

            # Get input from user to search for Instagram page
            search_bar = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input'))
            text_val = input('Enter IG name to look-up ')
            search_bar.send_keys(text_val + "\n")
            time.sleep(5)
            try:
                while True:
                    #This will end in an error state
                    search_bar.send_keys(u'\ue007')
            except Exception:
                print("Search entering Error")
            finally:
                #Move to next function
                print("It worked")
                self.igCrawler()
        except Exception:
            print("End of function scope")

    def igCrawler(self):

        time.sleep(15)
        #Get all elements with the 'a' tag which are the Instagram posts
        links = self.driver.find_elements_by_tag_name('a')

        def condition(link):
             #function gets all links that has .com/p/ in it and return it these are Instagram posts
             return '.com/p/' in link.get_attribute('href')
        #Filter all links that don't have .com/p/ at the end
        valid_links = list(filter(condition, links))

        #Use this number in range to edit how many posts to loop through
        for i in range(5):
            link = valid_links[i].get_attribute('href')

            if link not in self.links:
                self.links.append(link)
        
        for link in self.links:
            #Display each Instagram post page
            self.driver.get(link)
            time.sleep(3)
            get_span = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[2]/div/div/button/span")
            text = get_span.text
            self.likes.append(text)
        #Get the post with the most likes
        highest_like = self.getHighest(self.likes)
        print("Getting the Instagram photo with the most likes")
        time.sleep(10)
        self.driver.get(self.links[highest_like])
    #Get the postion of the largest number in the likes array
    def getHighest(self, like):
        return max( (v, i ) for i, v in enumerate(like) )[1]






# Create finite automata to scrape data members from a user's profile
#
scrap = webscrapper()










