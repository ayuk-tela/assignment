list = [17, 38, 10, 25, 72]

print(list[0:5])
list.append(12)
print(list)

def reverse(list):
   n_list = list[::-1]
   return n_list
print( 'the reversed list is ',reverse(list))

print('the index is ', list.index(17))

print('deleting 38 >> ', list.remove(38))
print(list)

print('display the sublist of the 2nd and 3rd element ', list[2:3])
print('display the sublist of the begginning to the  2nd element ', list[0:3])
print('display the sublist of the 3rd to the end of the list ', list[3:])
print('display the complete sublist  ', list[:])
print('display the last element using a negative subscript ', list[-1])










