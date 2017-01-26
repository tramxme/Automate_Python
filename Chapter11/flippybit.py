from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def main():
    url = "http://flippybitandtheattackofthehexadecimalsfrombase16.com/"
    browser = webdriver.Firefox()
    browser.get(url)

    #Start the game
    time.sleep(5) #wait for game to load
    browser.execute_script('$("#game-container").mousedown()')

    valList = {"1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A":"1010", "B":"1011", "C":"1100", "D":"1101", "E":"1110", "F":"1111"}

    while True:
        if (browser.execute_script('return $(".enemy").length') == 0):
            print("Len is 0 sleeping")
            time.sleep(1)
        elif browser.execute_script('return $(".enemy").length') > 0:
            val = browser.execute_script('return $(".enemy")[0].innerHTML')
            print(val)
            firstFour = ""
            secondFour = ""
            if (len(val) == 1):
                firstFour = valList.get(val)

            elif(len(val) == 2):
                firstFour = valList.get(val[1])
                secondFour = valList.get(val[0])

            if firstFour != "":
                for i in range(4):
                    if firstFour != None and firstFour[4 - i - 1] == "1":
                        string = 'jQuery($(".tapper")[' + str(i) + ']).mousedown()'
                        browser.execute_script(string)
                        print(string)


            if secondFour != "":
                for i in range(4, 8):
                    if (secondFour[4 - i - 1] == "1"):
                        string = 'jQuery($(".tapper")[' + str(i) + ']).mousedown()'
                        browser.execute_script(string)
                        print(string)

            time.sleep(2)

main()
