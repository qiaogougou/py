# Filename: func_local.py
def func(x):
	print('x is', x)
	x = 2
	print('Changed local x to', x)

x = 50
func(x)
print('x is still', x)

# x is 50
# Changed local x to 2
# x is still 50