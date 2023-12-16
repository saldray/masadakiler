# # l = [1, 2, 3]
# # l.append(55)
# # print(l)
# # # stacklarde push ve pop vardır.
# # # push en sona eleman eklemeye
# # # pop en sonadan eleman almaya yarar.
# # print(l.pop())
# # print(l)
# # print(l.pop())
# # print(l)

# # # popleft in yüklü olmadığını görelim..
# # l2 = [44, 55, 66]
# # l2.append(77) # append() listenin sonuna ekliyor
# # # popleft ise pop'tan farklı olarak baştan eleman alıyor

# # print(l2.pop(0))
# # #print(l2.popleft())# popleft hata verir import etmek gerekiyor şimdilik yorum ekleyip kullanmadan
# #  # yukarıda baştan nasıl eleman(öğe) alacağımıza bakalım
# # print(l2)

# # "collections" veri yapıları ile ilgili kütüphaneyi
# # içeren yapı içinde çok sayıda hazır yazılmış kodumuz
# # var
# # collections içinden deque'yu import edeceğiz

# from collections import deque
# # eklemek istediğimiz sayıların, öğelerin listesini
# # verdiğimizde deque onu otomatik olarak deque ya
# # çeviririz
# l3 = deque([11, 23, 45])
# print(l3)
# l3.append(67)
# print(l3.popleft())
# print(l3)
