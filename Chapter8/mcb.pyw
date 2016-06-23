#! python3
# Test2.pw - Saves and loads pieces of text to the clipboard
# Usage:
# pyw mcb.pyw save <keyword> - Saves clipboard to keyword.
# py mcb.pyw <keyword> - Loads keyword to clipboard.
# py mcb.pyw list - Loads all keywords to clipboard.
# py mcb.pyw delete <keyword> - Deletes keyword from the shelve
# py mcb.pyw delete - Deletes all keywords from shelve

import shelve, pyperclip, sys

def main():
    mcbShelf = shelve.open('mcb')
    print(dict(mcbShelf))

    # Save clipboard content.
    if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
        mcbShelf[sys.argv[2]] = pyperclip.paste()

    elif len(sys.argv) == 2:
        # List keywords and load content.
        if sys.argv[1].lower() == "list":
            pyperclip.copy(str(list(mcbShelf.keys())))

        elif sys.argv[1].lower() == "delete":
            mcbShelf.clear()


        elif sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])

    # Delete <keyword>
    elif len(sys.argv) == 3 and sys.argv[1].lower() == "delete" and sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]

    mcbShelf.close()


main()
