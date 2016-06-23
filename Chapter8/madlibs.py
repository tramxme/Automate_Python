import pyperclip, re

def madLibs():
    file = open(r'/Users/tram/Desktop/CodeEval/AutomateTheBoringStuff-Python/Chapter8/test.txt')
    default = ['adjective', 'noun', 'adverb', 'verb']

    text = []

    #Display the text
    print("Here's the text: ")
    for line in file.readlines():
        print(line, end="")
        text.append(line.split(" "))

    file.close()
    print()


    for i in range(len(text)):
        for j in range(len(text[i])):
            word = re.sub(r'\W+', r'', text[i][j]).lower()
            if word in default:
                print("Enter ", end="")
                if word[0] in "ueoai":
                    print("an ", end="")
                else:
                    print("a ", end="")
                print("%s: " % word)
                sub = input()
                text[i][j] = text[i][j].lower().replace(word, sub)
        text[i] = " ".join(text[i])
    text = "\n".join(text)

    print(text)
    
    file = open(r'/Users/tram/Desktop/CodeEval/AutomateTheBoringStuff-Python/Chapter8/ResultText.txt', 'w')
    file.write(text)
    file.close()

madLibs()
