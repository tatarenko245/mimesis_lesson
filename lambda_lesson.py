y = int(input("Введіть перше ціле число:"))
z = (lambda y: y + 1)(y)
print(z)


x = int(input("Введіть друге ціле число: "))
def iden(x):
    return x
print(iden(x))


# Здесь лямбда-выражение, что по сути есть функция, которая вызывается
full_name = lambda first, last: f"President: Presidetn:  Full name: {first.title()} {last.title()}"
# # Вызываем лямбда-выражение и передаем на вход строки
a = full_name(
    "Petro",
    "Poroshenko"
)
print(a)




