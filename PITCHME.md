# Python 3 alapok

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
      -  Könnyen tanulható, gyors fejlesztés
   - Interpretált:
      - Bárhol lefut, nem kell lefordítani

---

KÉP: https://cdn-images-1.medium.com/max/800/0*_e09A-2xg4x7PG_A.

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

### Hátrányok

 - Lassabb, mint egy lefordított program

Note:

---

### Pip

```
pip install colorama
```

 - csomagkezelő

  - egy helyen van minden

  - könnyen használható

  - globálisan felrakhatók a csomagok

Note:

- könnyen használható
  - C++ ban jóval nehezebb

---

### Virtualenv

 - saját környezet minden projekthez(dependecy)

 - pipenv

---

### Hello World!

```python
print("Hello World!")
```

---

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

### Szintaxis

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
   
   if file_text == file_finish:
      # close the file
	  file.close
      break
   file.write(file_text)
   file.write("\n")
file.close()
file_name = input("Enter filename: ")

if len(file_name) == 0:
   print ("Next time please enter something")
   sys.exit()

try:
   file = open(file_name, "r")

except IOError:
   print ("There was an error reading file")
   sys.exit()
file_text = file.read()
file.close()
print (file_text)
```

Note:

- Nincs sorvég jel
- A kód blokkok indentálva vannak nincs kapcsoszárójel
- komment #

---

### Változók

- integer
- float
- string
- list
- tuple
- dictionary

---

### List

```python
myList = ['physics', 'chemistry', 'physics', 1997, 2000]
```

bármilyen típus lehet benne

módosítható(mutable)

---

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

Ugyanaz, mint egy lista

Nem módosítható(immutable)

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

Kulcs érték pár

A kulcs egyedi, érték bármi lehet

```python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
```

```python
print ("dict['Name']: ", dict['Name'])
dict['Age'] = 8
del dict['Name']
```

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

```python
count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1
```

```python
>>> range(5)
range(0, 5)
>>> list(range(5))
[0, 1, 2, 3, 4]
```

---

#### For

```python
for var in range(5):
   print (var)
```

```python
for letter in 'Python':     # traversal of a string sequence
   print ('Current Letter :', letter)
print()
fruits = ['banana', 'apple',  'mango']

for fruit in fruits:        # traversal of List sequence
   print ('Current fruit :', fruit)
```

---

### Elágazás

```python
if expression1:
   statement(s)
elif expression2:
   statement(s)
elif expression3:
   statement(s)
else:
   statement(s)
```

---

### Osztályok

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

---

### Getter, Setter