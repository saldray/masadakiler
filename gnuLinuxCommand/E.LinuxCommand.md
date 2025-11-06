`head -n3 animals.txt | wc -w`

> **head** varsayılanı -n, 10 satırdır.
> ilk üç satırı gösterir ve 
> **wc** word count,  **-w** word 
> ilk üç satırı gösterir ve ilk üç satırdaki kelime sayısını yazdırır.

`cut -f2 animals.txt`

> ikinci sütundaki satırları yazdırır hepsini

>> **-f** field saymaya birden başlar

`cut -f1,3 animals.txt | head -n3`

> 1, 2 ve sütunların tamamını yazdırır
> pipe (boru) dan sonra baştan head -n3 ile
> baştan ilk üç satırı bastırır.

`cut -c1-3 animals.txt`

> -c character position
> 1, 2, 3 aralığını (range) alır
> ilk sütunun ilk satırlarının ilk üç karakterini ekrana basar.

`cut -f4 animals.txt`

> Lutz, Mark

> Barrett, Daniel

> Schwartz, Randal

> ...

`cut -f4 animals.txt | cut -d, -f1`

> **-d** delimeter (ayraç)
> virgülü ayraç sayıp öncesindeki soyadları alır.

---

`pattern`   örüntü

`file name pattern` dosya adı örüntüleri

`cat` `concatenate` birleştir, ard arda bağlamak, peşpeşelemek.

> art arda <Enter>

>arka arkaya <Enter>

>>Türkçe bir kelime olup, kökeni Arapça’dır. Ard kelimesi yer anlamına gelirken, arda kelimesi ise sıralı olarak anlamına gelmektedir. Bu nedenle ardarda kelimesi, yerlerin sıralı olarak takibi anlamına gelmektedir.

`mkdir -p dir/{a,b,c} && touch dir/a/file{001..009}.txt dir/b/file{010..020}.txt dir/c/file{100..110}.txt`
