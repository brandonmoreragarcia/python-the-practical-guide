simple_list = [1,2,3,4]
simple_list.extend([5,6,7])
print(simple_list)
del simple_list[0]
print(simple_list)


d = {'name': 'max'}
print(d.items())
for k,v in d.items():
    print(k,v)

t = (1,2,3)
print(t.index(1))

s = {'max', 'anna', 'max'}
print(s)

