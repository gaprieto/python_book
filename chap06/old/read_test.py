# read_test.py
# Simple read of a text file

# Reading line by line
print('Line by line')
fname = 'test_file.dat'
f = open(fname, 'r')
for line in f:
   print(line, end='')
f.close()

# reading file into list
print('')
print('File as list')
f = open(fname, 'r')
f_list = list(f)
print(f_list)
print(f_list[1])
f.close()

# Reading and printing all the file
print('Print entire file')
fname = 'test_file.dat'
f = open(fname, 'r')
text = f.read()
print(text)

