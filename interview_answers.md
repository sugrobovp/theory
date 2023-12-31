# PYTHON:

Основные типы данных в Python включают целые числа (int), числа с плавающей точкой (float), строки (str), списки (list), кортежи (tuple), множества (set), словари (dict) и булевы значения (bool).

По критерию изменяемости типы данных делятся на изменяемые (mutable) и неизменяемые (immutable).

Например, числа, строки, кортежи и frozenset относятся к неизменяемым типам, а списки, множества и словари к изменяемым типам.

Нет, кортежи (tuple) являются неизменяемыми типами данных. Вы не можете изменить элемент кортежа после его создания.

Упорядоченный тип данных - это тип данных, в котором элементы имеют определенный порядок. К ним относятся строки (str), списки (list), кортежи (tuple), множества (set), словари (dict).

По критерию упорядоченности типы данных делятся на упорядоченные (ordered) и неупорядоченные (unordered). Строки, списки, кортежи - упорядоченные. Множества и словари - неупорядоченные.

Разработчики Python решили сделать строки неизменяемыми, чтобы обеспечить их надежность и предотвратить неожиданные изменения, а списки сделали изменяемыми для более гибкой работы с данными.

Да, знаю, что такое set. Это тип данных, представляющий собой неупорядоченное множество уникальных элементов.

Общее между set и dict заключается в том, что оба они используют фигурные скобки для определения своих элементов, но у dict есть ключи и значения, в то время как set содержит только элементы.

Алгоритмическая сложность проверки наличия значения в множестве - O(1) в среднем случае.

Алгоритмическая сложность добавления элемента в конец списка - O(1), добавления в середину - O(n), где n - количество элементов в списке.

Да, знаю. Стек (stack) и очередь (queue) - это структуры данных, используемые для организации и управления данными. Стек работает по принципу "последний вошел, первый вышел" (LIFO), а очередь - по принципу "первый вошел, первый вышел" (FIFO).

Сложность получения значения по ключу в словаре - в среднем O(1), в худшем случае O(n), где n - количество элементов в словаре.

Встроенная сортировка в Python (функция sorted) имеет алгоритмическую сложность O(n log n), где n - количество элементов в списке.

b = list(a)[-1] создает список из объекта a и затем извлекает последний элемент списка. Результат - последний элемент объекта a (если a является итерируемым).

В Python термин "массив" используется не совсем корректно. Вместо него используется термин "список" для обозначения упорядоченной коллекции элементов.

Области видимости в Python включают глобальную (global), локальную (local) и вложенную (enclosing). Функция внутри себя может работать с переменными из глобальной области видимости (если они не переопределены), но для изменения глобальных переменных нужно использовать ключевое слово global. Глобальная функция также может использовать переменные из вложенных областей видимости.

Замыкание (closure) - это функция, которая сохраняет доступ к переменным из внешней области видимости, в которой она была создана.

Да, знаю, что такое декораторы. Они позволяют изменять поведение функций или методов без изменения их кода. Пример простого декоратора:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```
Из встроенных декораторов в Python, например, @staticmethod, @classmethod, @property. Декораторы из стандартной библиотеки: @lru_cache, @wraps, @contextmanager и другие.

Да, декораторы могут принимать аргументы. Например:

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```
### Хэш-таблица
Хэш-таблица (или хеш-таблица) - это структура данных, которая используется для хранения и организации данных таким образом, чтобы быстро выполнять операции вставки, удаления и поиска. Она основана на хеш-функции, которая преобразует ключи (например, строки или числа) в индексы, где данные будут храниться. Это позволяет достичь очень быстрого доступа к данным в среднем случае.

В Python хэш-таблицы реализованы в виде словарей (dict). Словари в Python - это коллекции, которые хранят пары ключ-значение. Ключи в словаре являются уникальными и неизменяемыми (например, строки, числа, кортежи), а значения могут быть любого типа данных.

Внутренне словари в Python реализованы как хеш-таблицы. Вот как это работает:

Хеш-функция: Когда вы добавляете элемент в словарь (например, my_dict[key] = value), Python вычисляет хеш-значение для ключа key. Хеш-значение - это целое число, которое используется как индекс в массиве (бакете) хеш-таблицы.

Разрешение коллизий: Если два разных ключа имеют одинаковое хеш-значение (коллизия), Python использует метод разрешения коллизий для управления этой ситуацией. Общим методом разрешения коллизий является использование списка или цепочки (цепочка связанных списков) в одном бакете. Если ключи имеют одинаковое хеш-значение, они будут храниться в одном и том же бакете, а затем будет выполнен поиск внутри этого бакета для нахождения конкретного значения.

Оптимизация размера: Чтобы уменьшить вероятность коллизий и оптимизировать производительность, Python динамически изменяет размер словаря при достижении определенного порога. Этот процесс называется "перехешированием".

Пример использования словаря (хеш-таблицы) в Python:

```python
my_dict = {'apple': 2, 'banana': 3, 'cherry': 1}
print(my_dict['banana'])  # Выведет 3
```
Хеш-таблицы в Python обеспечивают высокую производительность операций вставки, удаления и поиска элементов, и они широко используются в различных задачах программирования.

# PYTHON OOP:

Да, писал классы. Классы позволяют организовать данные и методы в объектно-ориентированной парадигме программирования.

Функция и метод - это в основном одно и то же, за исключением того, что метод всегда привязан к какому-то объекту (экземпляру класса) и может получать доступ к его данным.

Магические методы (dunder-методы) - это методы в Python, начинающиеся и заканчивающиеся двумя подчеркиваниями, например __init__, __str__, __add__. Они позволяют переопределить стандартное поведение операций для объектов вашего класса.

Обязательным аргументом для нестатических методов является self, который ссылается на сам объект, к которому применяется метод.

__init__ - это конструктор класса, который вызывается при создании нового объекта. Он инициализирует атрибуты объекта.

self - это ссылка на текущий объект класса, которая передается первым аргументом во все нестатические методы класса.

@classmethod и @staticmethod - это декораторы для определения классовых методов. @classmethod принимает cls в качестве первого аргумента и может работать с классом, а @staticmethod - не принимает ссылку на класс и является "чистой" функцией.

Миксины (mixins) - это классы, которые предоставляют определенное поведение, но не предназначены для самостоятельного использования. Их можно "подмешивать" (mix in) к другим классам для расширения функциональности.

SomeClass.__mro__ - это атрибут, который содержит порядок разрешения методов (Method Resolution Order) для класса SomeClass. Если метод не найден в самом классе, Python будет искать его в базовых классах в порядке, указанном в __mro__.

Объект класса не может вызывать метод класса напрямую, только через экземпляр класса. Метод класса вызывается на классе, а не на объекте.

__new__ - это магический метод, вызываемый перед __init__, и он используется для создания нового экземпляра класса. Сиглтон - это паттерн проектирования, который гарантирует, что у класса есть только один экземпляр.

Три основные парадигмы ООП: инкапсуляция, наследование и полиморфизм.

Инкапсуляция - это концепция, которая позволяет скрыть детали реализации и предоставить интерфейс для взаимодействия с объектом.

"Переопределение метода" означает, что вы предоставляете новую реализацию существующего метода в подклассе.

Чтобы изменить поведение оператора + для объекта вашего кастомного класса, вы должны переопределить магический метод __add__ в вашем классе.

Свойство (property) - это способ определения атрибута класса так, чтобы его можно было читать и записывать, как обычную переменную, но с выполнением дополнительного кода при доступе к нему.

Композиция - это концепция, при которой объект класса содержит в себе другие объекты, и их взаимодействие происходит через методы этого класса.

Наследование решает проблему повторного использования кода, но может привести к проблемам, связанным с жесткой зависимостью между классами.