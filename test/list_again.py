#!/usr/bin/python3.4
a = [66.25, 333, 333, 1, 1234.5]

print(a.count(333), a.count(66.25), a.count('x'))

# using list as a stack
stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print(stack)

vec = [-4, -2, 0, 2, 4]
print([x * 2 for x in vec])

# tuple
t = 12345, 54321, 'hello!'
print(t[0])

print(t)

tel = {'jack' : 4098, 'sape' : 4139}
tel['guido'] = 4127

print(tel)

del tel['jack']
print(tel)


print(list(tel.keys()))

r = {x: x**2 for x in (2, 4, 6)}
print(r)
