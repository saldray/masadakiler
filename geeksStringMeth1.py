# len() function

# A = "GeeksforGeeks"
# print(len(A))

# # count()

# A = "This is a python tutorial"
# print(A.count("is",0,len(A)))

# #we write the starting index
# #which is 0 by default
# #and then ending index
# #which is equal to length by default

# #cnter(), ljust(), rjust()

# str = "GeeksforGeeks"

# print(str.center(20,"-"))
# print(str.ljust(20,'-'))
# print(str.rjust(20,'-'))

# a = (str.center(20,('-')))
# print(len(a))
# print(a[19])
# print(a[15])


# #isalpha(), isalnum(), isspace()
# #is alphabe
# str1 = "abc"
# str2 = "ab12"
# str3 = "   "

# print("For string 1: isalpha() -->",str1.isalpha())
# print("For string 1: isalnum() -->",str1.isalnum())
# print("For string 1: isspace() -->",str1.isspace())
# print()
# print("For string 2: isalpha() -->",str2.isalpha())
# print("For string 2: isalnum() -->",str2.isalnum())
# print("For string 2: isspace() -->",str2.isspace())
# print()
# print("For string 3: isalpha() -->",str3.isalpha())
# print("For string 3: isalnum() -->",str3.isalnum())
# print("For string 3: isspace() -->",str3.isspace())

# b = "def"
# print(b.isalnum())


# # join()
# l = ["Geeks", "for", "Geeks"]
# s = "_"
# print(s.join(l))

#yazbeldem join() metodu

# kardiz = "Besiktas Jimnastik Kulubu"
# bolunmus = kardiz.split()
# print(bolunmus)

# kardiz = " ".join(bolunmus)
# print(kardiz)

# kardiz = "-".join(bolunmus)
# print(kardiz)
# print()
# kardiz = "".join(bolunmus)
# print(kardiz)
# print()
# kardiz = "_".join(bolunmus)
# print(kardiz)


#count()

# sehir = "Kahramanmaras"
# sehir.count("a")

# sehir = "adana"
# sehir.count("a")

# # Python saymaya “adana” karakter dizisinin 1. sırasından başlayacak.
# sehir.count("a", 1)
# sehir.count("a", 3)
# sehir.count("a", 4)

# # ilk karakter dizisinin icinden bir karakteri alıyor
# # count ile sayıyor birden fazla mı diye
# # for döngüsü ile böyle devam ediyor
# #eğer aynısından bir tane daha varsa False dönüyor.

# parola = input("parolanız: ")

# kontrol = True #flag girdik

# for i in parola:
#     if parola.count(i) > 1:
#         kontrol = False

# if kontrol:
#     print('Parolanız onaylandı!')
# else:
#     print('Parolanızda aynı harfi bir kez\
#  kullanabilirsiniz!')


# kelime = input("Herhangi bir kelime: ")

# for harf in kelime:
#     print("{} harfi {} kelimesinde {} kez geciyor!".format(harf, kelime, kelime.count(harf)))


# a harfi adana kelimesinde 3 kez geçiyor!
# d harfi adana kelimesinde 1 kez geçiyor!
# n harfi adana kelimesinde 1 kez geçiyor!
#Böyle bir çıktı elde edebilmek için

kelime = input("Herhang bir kelime: ")
sayac = ""

for harf in kelime:
    if harf not in sayac:
        sayac += harf

for harf in sayac:
    print("{} harf {} kelimesinde {} kez geciyor".format(harf,kelime,
                                                         kelime.count(harf)))
