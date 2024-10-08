# Напишите программу, которая принимает от пользователя пароль и проверяет его правильность. Если пароль верный, выведите сообщение "**Доступ разрешен**", иначе – "**Доступ запрещен**".

# **Требования:**

# - Заранее задайте в программе правильный пароль в виде строки.
# - Использовать оператор ветвления для проверки.

# создаем переменную и присваиваем ей правильный пароль
password = "RightPassword:)"

# запрашиваем пароль от пользователя
users_password = input("Введите пароль: ")

# проверяеи одинаковы ли строки
if password == users_password:
  # если да, то выведится **Доступ разрешен**
  print("**Доступ разрешен**")
else:
  # если нет, то выведится **Доступ запрещен**
  print("**Доступ запрещен**")