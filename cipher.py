#Please enter a sentence:
#The encrypted sentence is:
#right shift text 5 place

    
alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
text = input("Please enter a sentence:")
text = text.lower()
shift = (5)
x = {}
encryptedText = ""

for i in range (0,26):
    letter = alphabet[i]
    shiftedLetter = alphabet[(i + shift) % 26]
    x[letter] = shiftedLetter
    
    
for letter in text:
    if letter in alphabet:
        letter = x[letter]
        encryptedText = encryptedText + letter
    else:
        encryptedText = encryptedText + letter
print("The encrypted sentence is:" + encryptedText)

