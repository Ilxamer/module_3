#Task_1

# def binary_search(array,elem):
# 	low_border = 0
# 	high_border = len(array)
# 	mid = 0
# 	while elem != array[mid] and low_border <= high_border:
# 		mid = (low_border + high_border) // 2
# 		if elem == array[mid]:
# 			return mid
		
# 		elif elem < array[mid]:
# 			high_border = mid -1

# 		else:
# 			low_border = mid + 1
		
# 	return -1 #возвращает индекс числа
		

# list_num = [5,12,34,65,78,99,105,130,169,531,1042]
# number = 87

# print('Index of {}:{}'.format(number,binary_search(list_num,number)))

#Task_2
def sort_insert(array):
	for index in range(1,len(array)):
		current_value = array[index] 							   #текущее значение
		position = index  			 							   #Индекс текущего значения 
		while position > 0 and array[position -1] > current_value: #Цикл while сортирует внутри подмассива элементы
			array[position] = array[position-1]
			position -= 1
		array[position] = current_value
	return array


array= [54,123,44,643,12,345,768,33,1,41]
print('Исходный массив :', array)
result = sort_insert(array)
print('Результат сортировки: ', result)



#Task_3

graph = {'1':set(['2','3']),
'2':set(['1','10','11','12']),
'3':set(['1','4','5']),
'4':set(['3','6']),
'5':set(['3','6']),
'6':set(['4','5','7']),
'7':set(['6']),
'8':set(['10','11']),
'9':set(['12']),
'10':set(['2','8']),
'11':set(['2','8']),
'12':set(['2','9'])}


queue = []
visited =[]

def bfs(graph, start):
	global queue
	visited.append(start)
	queue.append(start)

	while queue:
		s = queue.pop(0)
		print(s)

		for neighbour in graph[s]:
			if neighbour not in visited:
				visited.append(neighbour)
				queue.append(neighbour)



print(bfs(graph,'1'))



