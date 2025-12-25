import search
import loader
import frequency
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


loader.loader("f1.txt", "f1_clean.txt")
loader.loader("f2.txt", "f2_clean.txt")


yes = True
fwords1 = frequency.find_freq("f1_clean.txt")
fwords2 = frequency.find_freq("f2_clean.txt")

clear_screen()

print("Search Engine 1.0")
print("________________________________________________")
while yes:
    sword = input("Enter the word:").lower()
    found1, freq1, found2, freq2 = search.search(sword)

    if found1:
        print(f'Found in file 1 {freq1} times')
    if found2:
        print(f'Found in file 2 {freq2} times')

    if not (found1) and not (found2):
        print("Word doesn't exist.")

    print("________________________________________________")

    fans = int(input("Enter k for the top k frequent words to be found."))

    freq_list1 = frequency.find_list(fwords1, fans)
    freq_list2 = frequency.find_list(fwords2, fans)

    print(f"The top {fans} word in file one are:")
    for freq, words in freq_list1:
        print(f"Word: {words.upper()}     Frequency: {freq}")

    print(f"The top {fans} word in file two are:")
    for freq, words in freq_list2:
        print(f"Word: {words.upper()}     Frequency: {freq}")

    print("________________________________________________")

    ans = input("Do you want to continue(Y/N)?").strip().upper()
    if ans == "Y":
        yes = True
    elif ans == "N":
        yes = False
    else:
        print("Invalid input, ending the program......")
        yes = False


print("________________________________________________")

print("Thank you for using the program!!!")
