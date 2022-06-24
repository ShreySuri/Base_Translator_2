def convert(string):
    list1=[]
    list1[:0]=string
    return list1



base = 0.5
while base % 1 != 0 or base < 2 or base > 36:
    base = input(print("Of what base is the integer? "))
    base = float(base)
base = int(base)


num_original = input(print("What integer would you like to convert to base 10?" ))
num_original = convert(num_original)


char_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
acceptable_char_list = []

for i in range (0, base):
    x = char_list[i]
    acceptable_char_list.append(x)



