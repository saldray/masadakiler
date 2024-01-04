# l = [1, 2, 3, 4]
# print(l)
# l.append(55)
# print(l)
# l.insert(2, 111)
# print(l)
# l.remove(111)
# print(l)

# l=[1, 2, 3, 4]
# l.append(55)
# print(l)
# l.insert(2, 111)
# l.append(111)
# print(l)
# l.remove(111)
# print(l)
# # ilk bulduğu 111'i siliyor.

# print(l.pop())
# print(l)

# print(l.index(2))
# print(l.index(55))

#print(l.count(1))
# l.append(1)
# print(l.count(1))

# l.sort()
# print(l)

# 8.49
# https://www.youtube.com/watch?v=V7yZ69pgJKU&list=PLh9ECzBB8tJOoFYmIIiwFjgXDCD9uiD_i&index=1

# append() fonksiyonu sayı eklemeye yarıyor
# extend() fonksiyonu listeleri birleştirmeye yarar

# l=[1, 2, 3, 4]
# l.append(55)
# #print(l.count(1))
# l.append(1)
# l2=[3, 4, 2]
# l.extend(l2)
# print(l)
# print(l.count(1))

# l.sort()
# print(l)

# l'yi extend() etmek yerine append() etsem ne olur.
# append() normalde bir eleman eklemeye yarıyordu.
# l2'yi l'ye append() edince liste bir eleman gibi
# eklenecek

# l=[1, 2, 3, 4]
# l.append(55)
# #print(l.count(1))
# l.append(1)
# l2=[3, 4, 2]
# #l.extend(l2)
# l.append(l2)
# print(l)
# print(l.count(1))

# # l.sort()
# # python3'te sort listeyi ve başka bir tipleri tanımlayamıyor

# print(l)


# l=[1, 2, 3, 4]
# l.append(55)
# #print(l.count(1))
# l.append(1)
# l2=[3, 4, 2]
# #l.extend(l2)
# l.extend(l2)
# print(l)
# print(l.count(1))
# # l.sort()
# # python3'te sort listeyi ve başka bir tipleri tanımlayamıyor
# print(l)
# l.clear()
# print(l)

# # copy anlatılıyor

# l3 = l2 # l3'ün içine l2'dekileri koy
# # shallow copy ve deep copy
# # sığ olanda sadece pointer geçiyoruz. Gösterici geçirıyoruz
# # yani hafızada aynı obje bir kere duruyor yani
# # l2'de l3'de aynı hafızayı gösteriyor bir tane liste var

# print(l3)
# l3.append(600)
# print(l2)
# print(l3)

# # Hafızada aynı yeri gösterdikleri için birine yapılan
# # bir değişiklik diğerinide etkiler

# # Ayrı ayrı varlıklar olsun birinde yaptığım değişiklik
# # diğerini etkilemesin istiyorum ne yapmam lazım

# l4 = l2.copy() # aynı varlıktan bir tane daha ama
# # iki farklı varlık oluşturduk.
# l4.append(700)
# print(l2)
# print(l4)
