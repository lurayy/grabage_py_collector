from webbot import Browser
import time 
import json

class App:

    def __init__(self):
        with open('URLS.json','r') as j_file:
            data = json.load(j_file)
        self.URLS =  data['URLS']
        self.DONE = data['DONE']
        self.username = 'Reosirieliza'
        self.password = 'huPiVE1KTTVEmFz7'
        self.link = 'http://euw.leagueoflegends.com'
        

    def run(self):
        bot = Browser(showWindow = True)
        bot.go_to(self.link)
        print("went to home page")
        print("checking for login")
        bot.maximize_window()
        bot.click("EUW")
        bot.click("LOGIN")
        print("click login")
        time.sleep(5)
        bot.type(self.username, into="Username")
        bot.type(self.password, into = "Password")
        bot.click("SIGN IN")
        print("clicked sign in")
        time.sleep(5)
        print("signed in")
        i = 0
        for url in self.URLS:
            print(url)
            bot.go_to('https://watch.lolesports.com'+str(url))
            time.sleep(3)
            bot.click("JUMP")
            time.sleep(80)
            temp = self.URLS.pop(i)
            self.DONE.append(temp)
        time.sleep(10)
        print("ok")
        self.save()
        bot.quit()

    def save(self):
        f_json = {
            'URLS':self.URLS,
            'DONE':self.DONE
        }
        with open('URLS.json', 'w') as outfile:
            json.dump(f_json, outfile)
        print("SVed done")


x = App()
x.run()