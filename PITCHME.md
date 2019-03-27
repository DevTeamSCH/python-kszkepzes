# Python3 alapok  

```python
import this
```

---

### The Zen of Python, by Tim Peters

<div class="half left">
  <ol>
  @size[24px](<li><b>Beautiful is better than ugly.</b></li>)
  @size[24px](<li><b>Explicit is better than implicit.</b></li>)
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
- Nem kell fordítani
- Platformfüggetlen

Note:

---

### Miért szeretjük a python?

Note:

- Magasszintű:
  - Könnyen tanulható, gyors fejlesztés
  - Interpretált:
    - Bárhol lefut, nem kell lefordítani

---

![Python is awsome!](https://cdn-images-1.medium.com/max/800/0*_e09A-2xg4x7PG_A.)

---

### Tökéletes?!

+++
### Tökéletes?!

NEM!

+++

### Tökéletes?!
- Lassú, nagyon lassú
- Zabálja a ramot


Note:

+++
Kép: https://benchmarksgame-team.pages.debian.net/benchmarksgame/faster/gpp-python3.html

Note:
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

- csomagkezelő
  - egy helyen van minden
  - könnyen használható

Note:

- könnyen használható
  - C++ ban jóval nehezebb

+++

```bash
pip install flake8
```


---

### Virtualenv

- saját környezet minden projekthez

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
source venv\bin\activate
```

---

### Flake8

- linter
- segít jobb kódot írni:
  - syntax error
  - typo
  - rossz formázás
- pep8

Note:
  pep8:
    - Style Guide
    - átlátható
    - egységes
    - kevesebb merge conflict

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
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
```

---

### Szintaxis TODO

```python
#!/usr/bin/python3
import sys

try:
   # open file stream
   file = open(file_name, "w")

except IOError:
   print ("There was an error writing to", file_name)
   sys.exit()
print ("Enter '", file_finish,)
print "' When finished"

while file_text != file_finish:
   file_text = raw_input("Enter text: ")
  
```

Note:

- Nincs sorvég jel
- A kód blokkok indentálva vannak nincs kapcsoszárójel
- komment #

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
d = 2+4j
x = False
str = "string"
str2 = str * 2
str3 = str2 + "abc"
```

+++

```python
print(a ** 3)
print(b / 2)
print(d * 2)
print(x)
print(str)
print(str1)
print(str2)
```

```python
8
1.6
4+8j
False
string
stringstring
stringabc
```

---

### List

+++

- bármilyen típus tartalmazhat (általában egyforma)

- Az elemek indexelhetőek

- módosítható(mutable)

```python
myList = ['physics', 'chemistry', 'physics', 1997, 2000]
```

+++

```python
print ("myList[0]: ", myList[0])
print ("myList[1:5]: ", myList[1:5])
```

```python
myList.append(5)
del myList[2]
```

---

### Tuple

+++

- Ugyanaz, mint egy lista

- De nem módosítható(immutable)

```python
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
```

```python
# tup1[0] = 100;
tup3 = tup1 + tup2
print (tup3)
```

---

### Dictionary

+++

- Kulcs érték pár
- A kulcs egyedi, érték bármi lehet

```python
dict = {'Name': 'Zara', 'Age': , 'Class': 'First'}
```

```python
print ("dict['Name']: ", dict['Name'])
dict['Age'] = 8
del dict['Name']
```

---

### Set

+++

- mint a lista, csak minden érték egyszer szerepelhet
- nem biztos, hogy sorban tárolja

```python
set = {1, 3, 5}
print(1 in set)
print(2 in set)
set.add(2)
set.update([6,4])
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
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)
```

+++

- Opciónális paraméter

```python
def fibonacci(n = 10):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)
```

+++

- Tetszőlegesen sok paraméter

```python
def minimum(first, *args): # *args néven szokás
    acc = first
    for x in args:
        if x < acc:
            acc = x
    return acc

print(minimum(3, 4, 2, -8, 6))
```

+++

- névszerinti paraméterátadás

```python
def print_rectangle(w=0, h=0, x=0, y=0):
    print("Rectangle")
    print("- size: {}×{}".format(w, h))
    print("- position: ({};{})".format(x, y))

print_rectangle(20, 30, 40, 50)
print_rectangle(x=10, w=19, h=25)
```

+++

---

### Alap beépített fgv-ek

int

hex

oct

str

len

list

range

---

### Ciklusok

---

#### While

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
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)
```