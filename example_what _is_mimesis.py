from mimesis import Person
from mimesis.enums import Gender
from mimesis import Generic
from mimesis import Address
from mimesis import locales

# Генерація повного імені для жінок по мові
person = Person('en')
person.full_name(gender=Gender.FEMALE)
print(person.full_name())

# Генерація повного імені для чоловіків по мові
peron = Person('uk')
person.full_name(gender=Gender.MALE)
print(person.full_name())

# Генерація місяця по мові
g = Generic('uk')
g.datetime.month()
print(g.datetime.month())

#Генерація imei кода
my_cod =  Generic('en')
my_cod.code.imei()
print(my_cod.code.imei())

#Генерація назв фруктів по назві
f = Generic('uk')
f.food.fruit()
print(f.food.fruit())

#Генерація області по мові
adr = Address('uk')
adr.region()
print(adr.region())

# Генерація країни по мові
adr = Address('uk')
adr.country()
print(adr.country())

# Генерація адреси
adr = Address('uk')
adr.address()
print(adr.address())

# Генерація поного імені людини з іншого регіону
person =Person(locales.EN)
person.full_name()
print(person.full_name())
with person.override_locale(locales.RU):
    person.full_name()
print(person.full_name())


person = Person('rtv', seed=0xFF)
person.full_name()
print(person.full_name())