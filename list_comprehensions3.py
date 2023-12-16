# comprehensions listelerin kapsanması, içerilmesi
# kavranması
# l = []
# # 1'den 9'a kadar olan sayıların(rakamların) karelerini
# # listenin içine koyacağız
# for x in range(10):
#     l.append(x ** 2)

# print(l)

# l = []

# for x in range(1, 11):
#     l.append(x ** 2)

# print(l)

# sideeffect
# genellikle bir kodun yazılmasında bir amaç vardır.
# ve o amaç için yazılan kodun o amaç dışında başka
# bir şey yapmaması istenir.
# Yaparsa şayet ona yan etkiler denir.
# Burada aslınad şöyle bir durum söz konusu

# x aslında döngü içerisinde kullandığımız döngü
# değişkeni

l = []

for x in range(1, 11):
    l.append(x ** 2)

print(l)
print(x)

# Benim niyetim x değişkenini tanımlayıp içine 10
# koymak değildi. Benim isteğimin dışında bir şeyler
# oldu. Bu bizim için bir yan etki istemediğimiz bir durum

# Burada lamda kalkülüse giriş yapalım.

# squares = list(map(lambda x: x**2, range(10)))

# print(squares)

squares = list(map(lambda x: x**2, range(1, 11)))

print(squares)

# lambda
# herhangi bir değer içermeyen geçişler, boş geçişler
# lambda boşluğu ifade eden bir yapı aslında (math)

# Buradaki tanımıda isimsiz bir fonksiyon tanımlamak
# ve (function pointer C) (delegete functions C#'ta)
# map
# Bir fonksiyonu al listenin tüm elemanlarına uygula
