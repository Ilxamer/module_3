# #Task_1
list_1 = ['1','2','5','python 2.0','python 3.0','hi','python 3.0','5','hi']
list_2 = []
for i in list_1:
	if i not in list_2:
		list_2.append(i)

print(list_1,list_2)

