
#IT IS PALINDROME
from colorama import Fore,Back,Style
word="Hii Bro".lower()
word_backwords=word[::-1]
if word == word_backwords:
    print(Fore.GREEN+"YES Its a palindrome"+Fore.RESET)
else:
    print(Fore.RED+"It is not a palindrome"+Fore.RESET)

#NOT A PALINDROME
word="malayalam".lower()
word_backwords=word[::-1]
if word == word_backwords:
    print(Fore.GREEN+"YES Its a palindrome"+Fore.RESET)
else:
    print(Fore.RED+"It is not a palindrome"+Fore.RESET)

# word="sagar"
# print(word[::4])
    
    