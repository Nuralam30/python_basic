
vowel = 0
consonant = 0
digit = 0
specialChar = 0
whiteSpace = 0

str = input('Enter your text :')
text = str.lower()
print(len(text))

for i in text :
    ch = i
    if(ch >='a' and ch <='z'):
        if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
            vowel += 1
        else:
            consonant += 1

    elif (ch >= '0' and ch <= '9'):
        digit += 1

    elif(ch == ' '):
        whiteSpace += 1

    else:
        specialChar += 1



print('total vowel :', vowel)
print('total consonant :', consonant)
print('total digit :', digit)
print('special character :', specialChar)
print('total whitespace :', whiteSpace)

