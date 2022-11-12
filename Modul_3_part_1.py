#Task_1
# x = int(input('Какую сумму вы хотели внести на вклад?'))
# p = int(input('Под какой процент?'))
# p = p/100
# y = int(input('Какую сумму вы хотите?'))

# year = 0
# while x <= y:
# 	x = int(x + x*p)
# 	year +=1
# 	print(year)


#Task_2

# n = int(input('Enter your number :'))
# i = 0	
# while i <= n:
# 	print('for - частный случай цикла while', i )
# 	i +=1

#Task_3
n = int(input('Введите число :'))
sum_n = 0
while n > 0:
	digital = n % 10
	sum_n = sum_n + digital
	n //= 10
print('Сумма цифр :', sum_n)



