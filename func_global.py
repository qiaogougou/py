# Filename: func_global.py
def func():
	global x
	print('x is', x)
	x = 2
	print('Changed local x to', x)

x = 50
func()
print('Value of x is', x)

# x is 50
# Changed local x to 2
# Value of x is  2