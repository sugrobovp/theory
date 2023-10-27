## Функции высшего порядка

**Определение** - Функция высшего порядка - функция, которая принимает другую функцию в качестве аргумента или возвращает в качестве значения

Пример из python - map, filter, reduce

По факту - эти функции легко заменить:

**Пример:**
```python
list(map(lambda x: x**2, range(5)))
[x**2 for x in range(5)]
```

## Анонимные функции

**Определение**: Анонимная функция - lambda функция

**Пример** (Сортировка слов в обратном порядке):
```python
fruits = ['apple', 'banana', 'cherry', 'fig']
sorted(fruits, key=lambda word: word[::-1])
```

**Применение**: Анонимные функции используются в основном в качестве аргументов для функций высшего порядка. Нетривиальные лямбда выражения неэффективны либо нечитаемы

## Девять видов вызываемых объектов

**Определение**: Объект называется вызываемым, если к нему можно применить (). Так же это можно проверить с помощью функции callable()

**Примеры**:
1. Пользовательские функции (def)
2. Встроенные функции (len, strftime)
3. Встроенные методы (dict.get)
4. Методы (функции, опредленные в теле класса)
5. Классы (при вызове класс сначала выполняет свой метод __new__, потом вызывает метод __init__)
6. Экземпляры классов (если в классе определен метод __call__, то экземпляры можно вызывать как функции)
7. Генераторные функции (функции или методы, в теле которых используется yield)
8. Платформенные сопрограммы (async def)
9. Асинхронные генераторные функции (async def и внутри еще yield)

## Пользовательские вызываемые типы

**Определение**: Любой объект можно заставить вести себя как функция, для этого нужно реализовать __call__

**Пример**

```python
import random

class BingoCage:
    """Корзина, из которой можно выбирать элементы в перемешанном состоянии"""

    def __init__(self, items):
        self._items = items
        random.shuffle(self._items)
        
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
        
    def __call__(self):
        return self.pick()
```

## Модуль operator

**Пример 1.1 (reduce через lambda)**:

```python
from functions import reduce

def factorial(n):
    """Итеративный факториал через reduce"""
    return reduce(lambda x, y: x*y, range(1, n+1))
```

**Пример 1.2 (reduce через mul)**

```python
from functions import reduce
from operator import mul

def factorial(n):
    """Тот же факториал, но с использованием mul, вместо lambda функции"""
    return reduce(mul, range(1, n+1))
```

**Пример 2 (itemgetter)**

```python
from operator import itemgetter

a = (
    [1, 2, 3],
    [3, 4, 8],
    [5, 10, 13]
)

# itemgetter возвращает callable объект
for _list in sorted(a, key=itemgetter(1)):
    print(_list)
```

**Пример 3 (attrgetter)**

**Определение**: attrgetter достает атрибут из класса

```python
from collections import namedtuple
from operator import attrgetter

# Определяем класс Dog
Dog = namedtuple('Dog', 'name weight height')

# name_height будет доставать вес и рост
name_height = attrgetter('weight', 'height')

# Данные по собакам
dogs_data = [
    ('James', '25kg', '61cm'),
    ('Marie', '14kg', '55cm'),
    ('Sam', '18kg', '70cm')
]

# Создаем объекты собак по данным
dogs_objects = [
    Dog(name, weight, height)
    for name, weight, height in dogs_data
]

# Сортируем по весу и выводим name_height(имя и рост)
for dog in sorted(dogs_objects, key=attrgetter('weight')):
    print(name_height(dog))
```

## Фиксация аргументов с помощью functools.partial

**Определение**: Partial принимает на входе вызываемый объект и возвращает новый вызываемый объект, в котором заранее предопределены несколько аргументов

**Пример**

```python
from functools import partial


# Изначально функция принимает 4 объекта
def four_obj(a, b, c, d):
    return a + b + c + d

# Теперь новый callable объект ex принимает два объекта по дефолту - это 1 и 2 заместо a и b
ex = partial(four_obj, 1, 2)
# А еще два мы можем докидывать
print(ex(3, 4))
```
