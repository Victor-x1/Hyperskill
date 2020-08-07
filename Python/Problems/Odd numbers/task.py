a_string = input()
a_list = a_string.split()
map_object = map(int, a_list)
list_of_integers = list(map_object)
odd_list = [x for x in list_of_integers]
print(odd_list)

