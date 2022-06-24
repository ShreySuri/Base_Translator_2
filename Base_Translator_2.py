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


            
            




