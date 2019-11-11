def proc(strings):
    m = 0
    lst = []
    for i in range(len(strings)):
        if len(strings[i]) > m:
            m = len(strings[i])
    for i in range(len(strings)):
        if len(strings[i]) == m:
            lst.append(strings[i])
    return lst


strings = ['cad', 'VB', 'Python', 'MATLAB', 'hello', 'world']
result = proc(strings)
print("the longest words are:")
for item in result:
    print("{: >25}".format(item))
