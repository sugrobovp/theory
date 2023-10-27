Выборка данных:

1. Вывести список всех пользователей из модели User.
Получить список всех книг из модели Book.
Вывести все заказы (Order) с указанием даты создания.
Фильтрация данных:

2. Получить список книг (Book), которые были опубликованы после 2020 года.
Найти всех пользователей (User), чьи имена начинаются на букву "A".
Найти заказы (Order) пользователя с именем "John".
Агрегация данных:

3. Посчитать общее количество книг в базе данных.
Найти среднюю цену всех книг.
Вычислить сумму заказов для каждого пользователя.
Сортировка данных:

4. Вывести список всех книг, отсортированный по алфавиту по названию.
Найти заказы (Order) пользователя с именем "Alice" и отсортировать их по дате создания в убывающем порядке.
Связи между моделями:

5. Вывести список всех авторов (Author), которые написали книги (Book) после 2019 года.
Найти всех пользователей (User), которые сделали заказы (Order) на книги определенного автора.
Группировка данных:

6. Найти количество заказов (Order) для каждой книги (Book).
Подсчитать, сколько книг (Book) каждый пользователь (User) добавил в корзину.
Изменение данных:

7. Обновить цену всех книг (Book), опубликованных до 2021 года, на 10%.
Удалить всех пользователей (User), которые не сделали ни одного заказа (Order).
Сложные запросы:

8. Найти пользователя (User), который сделал наибольшее количество заказов (Order).
Получить список всех книг (Book), которые есть в корзинах пользователей, но еще не были куплены.

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    authors = models.ManyToManyField(Author)

class User(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    order_date = models.DateField()
```

```python
1. User.objects.all()
Book.objects.all()
orders = Order.objects.all()
for order in orders:
    print(f'{order.id} with date {order.pub_date}')
```
```python
2. Book.objects.filter(pub_date__gt=2020)
User.objects.filter(name__startswith='A')
Order.objects.filter(name='John')
```
```python
3. Book.objects.count()
Book.objects.aggregate(Avg('price'))['price']
users = User.objects.annotate(total_orders=Sum('order__books__price'))
for user in users:
    print(f'{user.name} with total money spent: {user.total_orders}')
```
```python
4.  Book.objects.order_by('title')
Order.objects.filter(user__name='Alice').order_by('-pub_date')
```
```python
5. Author.objects.filter(book__pubyear__gt=2019)
author = Author.objects.get(name='Иван Иванов')
User.objects.filter(order__books__authors=author)
```
```python
6. books_orders_with_count = Book.objects.annotate(order_count=Count('order'))
for books in books_orders_with_count:
    print(f'{book.title} with order count: {book.order_bount}')
    
user_with_books_count = User.objects.annotate(book_count=Sum('cart_books'))
for user in user_with_books_count:
    print(f'{user.name} with order count: {user.book_bount}')
```
```python
7. books_to_update = Book.objects.filter(publication_year__lt=2021)
updated_books = books_to_update.update(price=F('price') * 1.1)

user_to_delete = User.objects.filter(order=None)
deleted_users = user_to_delete.delete()
```
```python
8. User.objects.annotate(order_count=Count('order')).order_by('-order_count').first()

books_in_carts=Book.objects.filter(cart__isnull=False)
books_ordered=Book.objects.filter(ordered__isnull=False)
books_not_purchsed = books_in_carts.exclude(pk__in=books_ordered.values_list('pk', flat=True))
```

```python

```




