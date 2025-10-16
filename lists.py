names = [ 'Dave', 'Paula', 'Thomas', 'Lewis']
a = names[2]
names[2] = 'Tom'
names.append('Alex')
names.insert(2, 'Aya')
print(names)

for name in names:
    print(name)

b = names[0:2]
print(b)
c = names[2:]
print(c)
names[1] = 'Becky'
print(names)
names[0:2] = [ 'Dave', 'mark', 'Jeff']
print(names)

a = ['x','y'] + ['z', 'z', 'y']
print(a)
names = []
print(names)
names = list()
print(names)
letters = list('Denver')
print(letters)


a = [1, 'Denver', 3.14, ['Kubrick', 7, 9, [100, 101]], 10]
print(a[1])
print(a[3] [2])
print(a[3][3][1])

