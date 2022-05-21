with open('list.txt', 'r') as f:
    lines = f.readlines()

lines_with_http = ['http://'+x for x in lines if 'http' not in x]


with open('list2.txt', 'w') as f:
    f.writelines(lines_with_http)
