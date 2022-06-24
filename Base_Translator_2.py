def list_len(list_1):
    list_1.append("placeholder")
    i = 0
    while list_1[i] != "placeholder":
        i = i + 1
    list_1.remove("placeholder")
    return(i)

def convert(string):
    list1=[]
    list1[:0]=string
    return list1

base = 0.5
while base % 1 != 0 or base < 2 or base > 36:
    base = input(print("Of what base is the integer? "))
    base = float(base)
base = int(base)


num_original = input(print("What integer would you like to convert to base 10? Letters should be entered as lowercase." ))
num_original = convert(num_original)


char_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
acceptable_char_list = []
valid_string = True


for i in range (0, base):
    x = char_list[i]
    acceptable_char_list.append(x)

length = list_len(num_original)
i = 0
new_num = 0

# <base> items in acceptable_char_list
# <length> items in num_original

while valid_string == True and i < length:
    counter = 0
    for j in range (0, base):
        if num_original[i] == acceptable_char_list[j]:
            counter = counter + 1
        else:
            counter = counter
    if counter == 1:
        valid_string = True
    else:
        valid_string = False
    i = i + 1

if valid_string == True:
    if base > 9:
        for i in range (0, length):
            if num_original[i] == "a":
                num_original[i] = "10"
            elif num_original[i] == "b":
                num_original[i] = "11"
            elif num_original[i] == "c":
                num_original[i] = "12"
            elif num_original[i] == "d":
                num_original[i] = "13"
            elif num_original[i] == "e":
                num_original[i] = "14"
            elif num_original[i] == "f":
                num_original[i] = "15"
            elif num_original[i] == "g":
                num_original[i] = "16"
            elif num_original[i] == "h":
                num_original[i] = "17"
            elif num_original[i] == "i":
                num_original[i] = "18"
            elif num_original[i] == "j":
                num_original[i] = "19"
            elif num_original[i] == "k":
                num_original[i] = "20"
            elif num_original[i] == "l":
                num_original[i] = "21"
            elif num_original[i] == "m":
                num_original[i] = "22"
            elif num_original[i] == "n":
                num_original[i] = "23"
            elif num_original[i] == "o":
                num_original[i] = "24"
            elif num_original[i] == "p":
                num_original[i] = "25"
            elif num_original[i] == "q":
                num_original[i] = "26"
            elif num_original[i] == "r":
                num_original[i] = "27"
            elif num_original[i] == "s":
                num_original[i] = "28"
            elif num_original[i] == "t":
                num_original[i] = "29"
            elif num_original[i] == "u":
                num_original[i] = "30"
            elif num_original[i] == "v":
                num_original[i] = "31"
            elif num_original[i] == "w":
                num_original[i] = "32"
            elif num_original[i] == "x":
                num_original[i] = "33"
            elif num_original[i] == "y":
                num_original[i] = "34"
            elif num_original[i] == "z":
                num_original[i] = "35"
            else:
                toggle = False
    else:
        toggle = True

    for i in range (0, length):
        x = int(num_original[i])
        num_original[i] = x

    place_val = length - 1

    for i in range (0, length):
        part = num_original[i] * base ** place_val
        new_num = new_num + part
        place_val = place_val - 1

    print(new_num)

else:
    print("The string you entered contained digits not part of base %s. Please try again." % base)
        




            
            




