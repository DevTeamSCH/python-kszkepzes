# Python3 alapok  

```python
import this

```

Note:

- Ki ismeri a Pythont?
- Ki tudja mit csinál a kód?

---

### The Zen of Python, by Tim Peters

<div class="half left">
  <ol>
  @size[24px](<li><b>Beautiful is better than ugly.</b></li>)
  @size[24px](<li>Explicit is better than implicit.</li>)
  @size[24px](<li><b>Simple is better than complex.</b></li>)
  @size[24px](<li><b>Complex is better than complicated.</b></li>)
  @size[24px](<li>Flat is better than nested.</li>)
  @size[24px](<li>Sparse is better than dense.</li>)
  @size[24px](<li><b>Readability counts.</b></li>)
  @size[24px](<li>Special cases aren't special enough to break the rules.</li>)
  @size[24px](<li>Although practicality beats purity.</li>)
  @size[24px](<li>Errors should never pass silently.</li>)
  @size[24px](<li>Unless explicitly silenced.</li>)
  @size[24px](<li>In the face of ambiguity, refuse the temptation to guess.</li>)
  </ol>
</div>

<div class="half right">
  <ol start="13">
  @size[24px](<li>There should be one-- and preferably only one --obvious way to do it.</li>)
  @size[24px](<li>Although that way may not be obvious at first unless you're Dutch.</li>)
  @size[24px](<li>Now is better than never.</li>)
  @size[24px](<li>Although never is often better than <i>right</i> now.</li>)
  @size[24px](<li><b>If the implementation is hard to explain, it's a bad idea.</b></li>)
  @size[24px](<li><b>If the implementation is easy to explain, it may be a good idea.</b></li>)
  @size[24px](<li>Namespaces are one honking great idea -- let's do more of those!</li>)
  </ol>
</div>

Note:

- Tim Peters, fő munkatárs
- CPython
- Python tervezési filozófiája, igy irjuk a python kódunkat

---

### Története

- Guido van Rossum
- 1991-ben jött létre
- Magas szintű programozási nyelv

Note:

- BDFL (Benevolent dictator for life)
- Monty Python, karácsony
- könnyen olvasható, tanulható, gyors fejlesztés
- lassú

---

### Interpretált

- A kódot egy értelmező dolgozza fel
- Platformfüggetlen
- Sok féle megvalósítás(CPython, PyPy, ...)

Note:

- Cpython Tim Peters Zen Of Python
- PyPy (C, CLI, JVM), 5x gyorsabb
- Jython bármilyen Java class használhatunk vele, mintha Python modul lenne
- PythonNet

---

### Miért szeretjük a pythont?

Note:

- Magasszintű:
  - Könnyen tanulható, gyors fejlesztés
- Interpretált:
  - Bárhol lefut, nem kell lefordítani

---

![Python is awsome!](https://cdn-images-1.medium.com/max/800/0*_e09A-2xg4x7PG_A.)


Note:

- csomagkezelés, mindenre is van csomag

---

### Tökéletes?!

+++

### Tökéletes?!

NEM!

+++

### Tökéletes?!

- Viszonylag lassú
- Nagy memóriaigény

Note:

- alacsonyszintű nyelvekhez képest, c, c++
- pl: nem kell memoria teruletet foglalni

+++

![C++ vs Python3](https://raw.githubusercontent.com/DevTeamSCH/python-kszkepzes/master/media/c%2B%2B_vs_python.png)

Note:
N-body
 - dinamikus rendszer
 - általában fizikai erőkkel szimulálva
 - pl galaxysok vizsgalata
 - Jupiter, Saturn, Uranus and Neptune

 https://en.wikipedia.org/wiki/N-body_simulation
---

### Csomagok

- Webfejlesztés:
  - Django
  - Flusk
  - Requests

+++

- IT Security:
  - Scapy
  - Nmap

+++

- AI:
  - TensorFlow
  - Keras

+++

- Data Science:
  - Pandas
  - StatsModels
  - NumPy

+++

- GUI:
  - PyQt
  - Tkinter
  - Flexx
 
+++

- Data visualization
  - matplotlib
  - Plotly
  - geoplotlib
Note:

---

### Pip

- Csomagkezelő
  - Egy helyen van minden
  - Könnyen használható

Note:

- könnyen használható
  - C++ ban jóval nehezebb lib import

+++

```bash
pip install <package>
```

---

### Virtualenv

- Saját környezet minden projekthez

Note:

- Dependency, egy csomag több verzió

+++

- Windows:

```cmd
python -m venv venv
```

```cmd
venv\Scripts\activate.bat
```

+++

- Linux:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

### Flake8

- Linter
- Segít jobb kódot írni:
  - Syntax error
  - Typo
  - Rossz formázás
- pep8(Style Guide)



```cmd
pip install flake8
```

```cmd
flake8 <filename>
```

Note:

- Style Guide
  - átlátható
  - egységes
  - kevesebb merge conflict

---

### Black

- Atomatikusan formázza a kódot.

```cmd
pip install black
```

```cmd
black <filename>
```

---

### Hello World

+++

```python
print("Hello World!")

```

+++

```bash
pip install colorama
```

```python
from colorama import init
from colorama import Fore, Back, Style

init()
print(Fore.RED + "some red text")
print(Back.GREEN + "and with a green background")
print(Style.DIM + "and in dim text")
print(Style.RESET_ALL)
print("back to normal now")

```

---

### Szintaxis

```python
"""This is the start of the program """
while 1:
    print("Spam")
    answer = input("Press y for large fries ")
    if answer == "y":
        print("Large fries with spam, mmmm, yummy ")
        continue
    answer = input("Had enough yet? ")
    if answer == "y":
        break
print("Have a ")
print("nice day!")  # Bye bye

```

Note:

- Nincs sorvég jel
- A kód blokkok indentálva vannak nincs kapcsoszárójel
  - 4 space
- komment #, '''alam'''

---

### Változók

- number (integer, floating point, complex)
- boolean
- string
- list, tuple, dictionary, ...

+++

```python
a = 2
b = 3.2
d = 2 + 4j

print(a ** 3)
print(b / 2)
print(d * 2)
```

Output

```python
8
1.6
(4+8j)
```

+++

```python
x = False
str = "string"
str2 = str * 2
str3 = str2 + "abc"

print(x)
print(str)
print(str2)
print(str3)
```

output

```python
False
string
stringstring
stringstringabc
```

---

### List

+++

- Bármilyen típust tartalmazhat (általában egyforma)
- Az elemek indexelhetőek
- Módosítható(mutable)

+++

```python
list = ["a", "b", "c", 1, 2, 3]
for a in list:
    print(a)
list[4] = 22
list.append(50)
del list[3]
print(list[2:])

```

Output:

```python
a
b
c
1
2
3
['c', 22, 3, 50]
```

---

### Mit ír ki?

```python
list = ["SCH", (), 105, "KSZK", "ujonc", 69.69, []]
print list[2:4]
```

---

### Tuple

+++

- Ugyanaz, mint egy lista
- De nem módosítható(immutable)

+++

```python
tuple = ("a", "b", 3)
item = tuple[2]
for a in tuple:
    print(a)

a, b, c = tuple
print(c)

tuple2 = (34, 56, "d")
tuple3 = tuple + tuple2
print(tuple3)

```

Output:

```python
a
b
3

3

('a', 'b', 3, 34, 56, 'd')
```

---

### Dictionary

+++

- Kulcs érték pár
- A kulcs egyedi, érték bármi lehet

+++

```python
dict = {"Name": "Zara", "Age": 10, "Class": "First"}

dict["Age"] = 8
for key, value in dict.items():
    print(key, " : ", value)
del dict["Name"]
print("Name" in dict)

```

Output:

```python
Name  :  Zara
Age  :  8
Class  :  First
False
```

---

### Set

+++

- Mint a lista, csak minden érték egyszer szerepelhet
- Nem biztos, hogy sorban tárolja

+++

```python
set = {1, 3, 5}
print(1 in set)
print(2 in set)
set.add(2)
set.update([6, 4])
for a in set:
    print(a)

```

Output:

```python
True
False
1
2
3
4
5
6
```

---

### Függvények

+++

```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))

```

Output:

```python
55
```

+++

- Opcionális paraméter

```python
def fibonacci(n=10):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci())

```

Output:

```python
55
```

+++

- Tetszőlegesen sok paraméter, list

```python
def minimum(first, *args):
    acc = first
    for x in args:
        if x < acc:
            acc = x
    return acc


print(minimum(3, 4, 2, -8, 6))

```

Output:

```python
-8
```

Note:
- miért van a first paraméter?
- mert a min fgv 0 paraméterre nem értelmes 

+++

- Tetszőlegesen sok paraméter, dictionary

```python
def bar(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


print(bar(Kutya="vau", Cica="miaaau"))

```

Output:

```python
-8
```

+++

- Névszerinti paraméterátadás

```python
def print_rectangle(w=0, h=0, x=0, y=0):
    print("Rectangle")
    print("- size: {}×{}".format(w, h))
    print("- position: ({};{})".format(x, y))


print_rectangle(20, 30, 40, 50)
print_rectangle(x=10, w=19, h=25)

```

Output:

```python
Rectangle
- size: 20×30
- position: (40;50)
Rectangle
- size: 19×25
- position: (10;0)
```


---

### Alap beépített fgv-ek

```python
dir(__builtins__)

```

+++

- input() Allowing user input
- len() Returns the length of an object
- abs() Returns the absolute value of a number
- slice() Returns a slice object
- ...
- https://www.w3schools.com/python/python_ref_functions.asp

---

### Ciklusok

---

### While

+++

```python
i = 1
while i < 6:
    print(i)
    i += 1

```

Output:

```python
1
2
3
4
5
```

---

### For(each)

+++

```python
a = [1, 2, 3]
for x in a:
    print(x)

print("-")

for x in range(1, 6, 2): # for (int i = 1; i < 6; i += 2)
    print(x)

```

Output:

```python
1
2
3
-
1
3
5
```

---

### Elágazások

+++

```python
b = False
x = 3
if not b and x <= 6:
    print("Hello")
elif b or x > 5:
   print("World!")
else:
   print("Hello World!")

```

Output:

```python
Hello
```

---

### Osztályok

+++

```python
class A:
    _b = "Foo"

    def __init__(self):
        self.a = 1

    def print(self, str):
        for x in range(self.a):
            print(self.b, str)

class B(A):
    def __init__(self, a):
        self.a = a

a = A()
a.print("Fighters")
b = B(5)
b.print(u"\u03C1" + " Fej")

```

+++

Output:

```python
Foo Fighters
Foo ρ Fej
Foo ρ Fej
Foo ρ Fej
Foo ρ Fej
Foo ρ Fej
```

---

### Workshop

---

### HF

---

### Dekorátor

+++

```python
def my_decorator(func):
    def wrapper():
       print("Before")
       func()
       print("After")

    return wrapper

@my_decorator
def hello():
    print("Hello")

````

Output:

```python
Before
Hello
After
```
