from uuid import uuid4

 #Функція, що генгерує строки в uuid форматі
def identify():
    x=uuid4()
    return x
a= identify()
print(a)

# Функція, що повертає строку
def name_of_president(name, last_name):
    return (f"Вітаємо, {name} {last_name}! Ви отримали посаду Президента України")
p=name_of_president(
    name=input("Введите Ваше имя: ").capitalize(),
    last_name=input("Введите Вашу фамилию: ").capitalize()
)
print(p)