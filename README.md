# Python OOP Youtube
## Lesson 1: Классы и объекты. Атрибуты классов и объектов
1. Ссылки на атрибуты класса:
![Attribute](lesson_1/1.JPG)
2. Добавление своего атрибута в переменную:
![Attribute](lesson_1/2.JPG)
3.  Добавление новых атрибутов(сохранение взаимосвязи):
![Attribute](lesson_1/3.JPG)
4. Итог:
![Attribute](lesson_1/4.JPG)
## Lesson 2: Методы классов. Параметр self
1. Передача self:
![Method](lesson_2/1.JPG)
2. Значение self для метода(для чего его создали):
![Method](lesson_2/2.JPG)
## Lesson 3: Инициализатор __init__ и финализатор __del__
1. Инициализатор __init__ и финализатор __del__(start)
![Magic](lesson_3/1.JPG)
2. Инициализатор __init__ (Принцип действия)
![Magic](lesson_3/2.JPG)
3. Финализатор __del__ (принцип действия)
Работает по принципу: пока есть внешняя ссылка на 
объект-нужен(обратное-не нужен(__del__ подчищает))
![Magic](lesson_3/3.JPG)
## Lesson 4: Магический метод __new__. Пример паттерна Singleton
1. Магический метод __new__(start)
![Magic](lesson_4/1.JPG)
2. Иерархи классов по умолчанию:
![Magic](lesson_4/2.JPG)
3. Паттерн Singleton:
![Magic](lesson_4/3.JPG)
## Lesson 5: Методы класса (classmethod) и статические методы (staticmethod)
1. @classmethod: прописывать имя класса внутри самого класса это плохая практика, лучше использовать
cls/self так программа становится более универсальной
![Magic](lesson_5/1.JPG)
2. Простой случай с методами
![Magic](lesson_5/2.JPG)
3. Наглядно про обращение через @classmethod
![Magic](lesson_5/3.JPG)
4. @staticmethod предлагается использовать только переданными аргументами
![Magic](lesson_5/4.JPG)
## Lesson 6: Режимы доступа public, private, protected. Сеттеры и геттеры
1. Механизм инкапсуляции
![Magic](lesson_6/1.JPG)
2. getter and setter (интерфейсные методы)
![Magic](lesson_6/2.JPG)
3. Дополнительный модуль для работы с приватными методами
![Magic](lesson_6/3.JPG)
## Lesson 7: Магические методы __setattr__, __getattribute__, __getattr__ и __delattr__
1. Четыре магических методов
![Magic](lesson_7/1.JPG)
2. 