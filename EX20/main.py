original_list = [0, 1, 2, 3, 4, 5]
modified_list = [num + 3 for num in original_list if num >= 2]

print(modified_list)

string1 = "abc"
string2 = "de"

result = [x + y for x in string1 for y in string2]
print(result)