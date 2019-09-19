import sys

f_read = open(sys.argv[1], "r")
f_write = open(sys.argv[2], "w")

for l in f_read:
	f_write.write(l)
	print(l)
