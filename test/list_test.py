#!/usr/bin/python3

x = int(input("pls enter an integer: "))
if x < 0:
    x = 0
    print('Negative chagned to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

words = ["cat", 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for w in words[:]:
    if len(w) > 6:
        words.insert(0, w);

print(words)


for i in range(5):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

class MyEmptyClass:
    pass

def fib(n):
    """print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end = ', ')
        a, b = b, a + b
    print()

def fib2(n):
    """Return a list containing the Fibonacci series up to n"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

fib(2000)
f100 = fib2(100)
print(f100)


def ask_ok(prompt, retries = 4, complaint = 'Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError("uncooperative user")
        print(complaint)

ask_ok('Do u really want to quit?')

# default argument test, default argument value is evaluated only once.
def f(a, L = []):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f1(a, L = None ):
    if L is None:
        L = []
    L.append(a)
    return L


print(f1(1))
print(f1(2))
print(f1(3))

# keyword argument and positional argument
def cheeseshop(kind, *arguments, **keywords):
    print("--Do you have any", kind, "?")
    print("--I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# arbitrary argument lists

def write_multiple_items(file, seperator, *args):
    file.write(seperator.join(args))

def concat(*args, sep = '/'):
    return sep.join(args)

print(concat('earth', 'mars', 'venus'))

# lambda expression
def make_incrementor(n):
    return lambda x : x + n

f = make_incrementor(42)
print(f(0))
print(f(1))

# documentation strings
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """

    pass

print(my_function.__doc__)

def f_anno(ham: str, eggs: str = 'eggs') -> str:
    print("annotation: ", f.__annotations__)
    print("arguments", ham, eggs)
    return ham + " and " + eggs

f_anno('spam')
