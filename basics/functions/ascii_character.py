print("Program Started!")
print("Please enter an ASCII code")

ascii = int(input())

if ascii in range (32, 127):
    print("The character represented by the ASCII code", ascii, " is: ", chr(ascii))

else:
    print("program ended")
