

#find nth character in string
def str_counter():
    n = input('Which # character do you want?:\n')
    n = int(n) - 1
    maxChars = int(len(string))

    if n > maxChars:
        print "Error, there are not that many characters!"
    else:
        character = string[n]
        print 'That character is ', str(character)

string = raw_input('Enter your string to check:\n')
numbersNeeded = int(raw_input('How many numbers do you need?: \n'))

counter = 0
while counter < numbersNeeded:
    counter = counter + 1
    str_counter()
