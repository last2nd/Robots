from selenium import webdriver
import sys
import time
from getpass import getpass
import time

options = webdriver.ChromeOptions()
#user- agent
options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36')

options.add_argument('--disable-blink-features=AutomationControlled')

options.headless = True

browser = webdriver.Chrome(
    executable_path= r'Chromedriver\chromedriver_android',
    options=options)
 
def entry():
    print('Opening instagram...')
    browser.get(url= 'https://www.instagram.com/')
    browser.implicitly_wait(10)

    name = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    name.click()
    name.send_keys(input('Username: '))
    browser.implicitly_wait(10)
    print('Username entered')

    password = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    password.click()
    password.send_keys(input('Password:')) 
    browser.implicitly_wait(10)
    print('Password entered')
    
    enter = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
    enter.click()
    browser.implicitly_wait(10)
    return 'Input'

def check():
    print('Checking...')
    try:
        search = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys('pornhub')
        browser.implicitly_wait(10)
        return True
    except Exception:
        print('Error: Auntification error')
        browser.refresh()
        return False

try: 
    print(""" 
            .##.....##.########..######...######..##....##..######...########.....###....##.....##
            .###...###.##.......##....##.##....##..##..##..##....##..##.....##...##.##...###...###
            .####.####.##.......##.......##.........####...##........##.....##..##...##..####.####
            .##.###.##.######....######...######.....##....##...####.########..##.....##.##.###.##
            .##.....##.##.............##.......##....##....##....##..##...##...#########.##.....##
            .##.....##.##.......##....##.##....##....##....##....##..##....##..##.....##.##.....##
            .##.....##.########..######...######.....##.....######...##.....##.##.....##.##.....##
            
                                            Directed by last2nd
                        Usage:  enter count of post which you save and like
                                input username and password from in instagram

                        WARNING: DEVELOPER USE PornHub INSTAGRAM PAGE 
                                 DON`T CARE DEVELOPER AND ANYONE ANOTHER CAN`T
                                 SEE YOUR PASSWORD BUT ANYWAY USE IT CAREFULLY  
            """)
    
    n = int(input('Count ---> '))
    
    while True:
        entry()
        if not check():
            continue
        else:
            start = time.time()
            print('Checking done!')
            print('PornHub page is already searching...')
            break

    pornhub = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')
    pornhub.click()
    # browser.implicitly_wait(10)
    time.sleep(3)
    print('PornHub page opened')
    
    i = 0
    while i != n:
        choose = browser.find_elements_by_class_name('_9AhH0')
        choose[i].click()
        print(f'{i+1} --------------- {i+1}')
        browser.implicitly_wait(10)
        # time.sleep(2)

        like = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div[3]/section[1]/span[1]/button')
        like.click()
        browser.implicitly_wait(10)
        # time.sleep(2)

        save = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div[3]/section[1]/span[4]/div/div/button')
        save.click()
        browser.implicitly_wait(10)
        
        print(f'Post liked and saved')

        close = browser.find_element_by_xpath('/html/body/div[6]/div[3]/button')
        close.click()
        browser.implicitly_wait(10)

        i += 1
        continue
    print('All done!')

except Exception as e:
    print(sys.exc_info())
    print(e)
finally:
    browser.close()
    browser.quit()
    print(f'Time: {round(time.time() - start, 1)}')
    print('EXIT')
