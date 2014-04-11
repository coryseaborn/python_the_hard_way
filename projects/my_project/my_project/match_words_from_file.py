from sys import argv

script, filename, search = argv

file = open(filename, 'r')
run = file.read()

#text = raw_input("Searching for: ")
# 

lists = run.split()

matching = [x for x in lists if search in x]
print matching

# x = re.findall("interface GigabitEthernet\d+.\d+", f)
# >>> x
# 'hi my name is what'
# >>> y
# ['hi', 'my', 'name', 'is', 'what']
# >>> z = re.findall('name', x)
# >>> z
# ['name']
# >>> 