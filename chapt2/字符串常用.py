s='Hello World eddfkldaasdaifdfs'
print(s)
print('-'*50)

s_set = set(s)
print(s_set)
print('-'*50)

s_list = list(s_set)
s_list.sort(key=s.find)
print(''.join(s_list))
