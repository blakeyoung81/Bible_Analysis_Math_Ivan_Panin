# Input the bible
f = open(r"C:\Users\blake\OneDrive\Desktop\Python\Projects\Bible analysis\kjv-1769.txt")
bible = f.read()
# Get word in dictionary with number
print(bible)
# Get 40th word
string = ""
interval = 39
while interval < (39*5000):
    letter_found = True
    word40 = bible.split()[interval]
    try:
        letter =(word40[7])
        print(letter)
    except:
        letter_found = False
# Get 7th letter

# Return and print
    #print(word40)
    interval = interval + 40
    if letter_found == True:
        string = string + letter


    


