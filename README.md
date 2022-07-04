# Django REST Framework

![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### PY-Venv

1.  Создание виртуального окружения
>python -m venv venv

2.  Активация виртуального окружения
* cmd
>venv\scripts\activate.bat

* PowerShell
>venv\scripts\activate.ps1

3.  Деактивация виртуального окружения
>deactivate

### PY-Django Rest Framework

* Загрузка drf
>pip install djangorestframework

* Загрузка пакета авторизации по токенам (после подключения провести миграции)
>pip install djoser

* Загрузка пакета авторизации по jwt-токенам
>pip install djangorestframework-simplejwt

* Создание файла с зависимостями проекта
>pip freeze > req.txt

### PY-Django ORM

Blog.objects.

all()   получить все данные

all().reverse   получить все данные в обратном порядке

all()[:5]   получить первые пять записей (начиная с последних)

all()[10:]    получить все записи, начиная с десятой



count()   получить количество записей

order_by('pk')    отсортировать по параметру в скобках

exclude()   получить все записи за исключением (в скобках параметры)

get(pk=1)   получить ОДНУ запись по ключевому параметру



filter(pk__gt=12)   эквивалент WHERE pk > 12, gt - больше, чем

filter(pk__gte=12)    эквивалент WHERE pk >= 12, gt - больше или равно, чем

filter(pk__lt=12)   эквивалент WHERE pk < 12, gt - меньше, чем

filter(pk__lte=12)    эквивалент WHERE pk <= 12, gt - меньше или равно, чем

filter(category__title='Личные записи')   получить записи из категории <внешний ключ>__<первичная модель>



filter(title__contains='blog')    поиск с учетом регистра

filter(title__icontains='blog')   поиск без учета регистра


filter(pk__in=[1, 2, 3])    поиск в указанном диапазоне

filter(pk__in=[1, 2, 3], title__contains='blog')    можно комбинировать запросы (логическое И по умолчанию)

filter(Q(pk__in=[5, 6]) | Q(title__contains='запись'))    получить запись с pk 5 или 6 ИЛИ запись, где в title есть слово 'запись' **import Q

filter(Q(pk__in=[5, 6]) | Q(title__contains='запись') & ~ Q(pk__lt=4))    ... И pk записи НЕ должен быть меньше 4 **import Q



first()   получить первую по дате запись (сортировка по дате: самая последняя)

last()    получить последнюю запись (сортировка по дате: самая ранняя)

order_by('pk').first()    получить первую запись по параметру pk



._set   получить связанные данные

notes_set.count()   получить количество записей в note

.get_previous_by_created_at()   предыдущая запись (created_at - параметр даты создания записи)

.get_next_by_created_at()   следующая запись (created_at - параметр даты создания записи)

.notes.get_next_by_created_at(pk__gt=10, title__icontains='запись')   следующая запись из notes, чей id больше 10, а в title есть слово 'запись'


aggregate(Min('views'), Max('views'))   получить минимальное и максимальное значения поля views

aggregate(min_views=Min('views'), max_views=Max('views'))   именованные параметры **import Min, Max


values('title', 'views', 'category__title')   получить title записи, количество просмотров и название категории записи


ИНКРЕМЕНТ

from django.db.models import F

note = Blog.objects.get(pk=1)

note.views = F('views') + 1

note.save()


raw("")   позволяет писать запросы на языке SQL

Blog.objects.all() равносильно Blog.objects.raw("SELECT * FROM blog_blog")

raw-запрос должен содержать id (не pk)

##### Обучающие материалы
[Уроки по Django REST Framework](https://www.youtube.com/playlist?list=PLA0M1Bcd0w8xZA3Kl1fYmOH_MfLpiYMRs)
