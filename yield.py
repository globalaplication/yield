import os
def fflist(path):
	dir = [path]
	for j in dir:
		yield [j]
		if os.path.isdir(j) is True:
			for k in os.listdir(j):
				dir.extend([j+'/'+k])
for test in fflist('/home/linux/Test'):
	print test
