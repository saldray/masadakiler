>>> eğer java programını main'i ve demo class'ını ayrı birer dosyaya yazsaydım nasıl yapardım.
... class Demo {
... 
...     static String  str1 = "abc";
...     static String str2 = "   ";
...     static String str3;  
...     static String str4 = null;
...     public static void main(String args[]) {
... 
...         System.out.println(str1);
...         System.out.println(str2);
...         System.out.println(str3);
...         System.out.println(str4);
...         System.out.println(str3.length());
...     }
... }
Tamamdır, bu Java programını `Demo.class` dosyasının bulunduğu bir klasör yapısıyla 
nasıl oluşturabileceğinizi adım adım açıklıyorum.

**1. Dosya Yapısı:**

Öncelikle, aşağıdaki gibi bir klasör yapısı oluşturun:

```
DemoKlasimleri/
├── Demo.java
└── Main.java
```

**2. Demo.java Dosyası İçeriği:**

```java
// Demo.java
package DemoKlasimleri; //Paket bildirimi (isteğe bağlı, ancak iyi bir uygulamadır)

public class Demo {
    static String str1 = "abc";
    static String str2 = "   ";
    static String str3;  // Başlangıçta null değerine sahip
    static String str4 = null;

    public static void main(String args[]) {
        System.out.println(str1);
        System.out.println(str2);
        System.out.println(str3); // str3 null olduğu için null pointer exception 
vermemesi önemli
        System.out.println(str4);
        System.out.println(str3.length()); // str3 null olduğu için bu satırda hata 
oluşabilir
    }
}
```

**3. Main.java Dosyası İçeriği:**

```java
// Main.java
package DemoKlasimleri;

public class Main {
    public static void main(String[] args) {
        System.out.println("Ana Program Başlıyor...");
        new Demo().main(args); // Demo sınıfının main metodunu çağırıyoruz.
        System.out.println("Ana Program Bitti.");
    }
}
```

**Açıklamalar:**

*   **Paketler:** `DemoKlasimleri` paketi, kodunuzu daha düzenli tutmaya yardımcı olur.  
Java'da, sınıflar ve paketler belirli bir dizin yapısıyla ilişkilendirilir.
*   **`Demo` Sınıfı:**  `Demo` sınıfı, `str1`, `str2`, `str3` ve `str4` gibi 
değişkenleri içerir.
*   **`main` Metodu:**  `Demo` sınıfının `main` metodu, programın başlangıç noktasını 
belirtir.
*   **`Main` Sınıfı:**  `Main` sınıfı, `Demo` sınıfının `main` metodunu çağırarak 
programın çalışmasını başlatır.  Bu, `Demo` sınıfının `main` metodunun doğrudan 
çalışmasını engeller.  Bu tasarım, daha karmaşık uygulamalarda sınıfların ve metotların 
daha iyi organize edilmesine yardımcı olur.

**4. Derleme ve Çalıştırma:**

1.  **Terminali Açın:**  Derleme işlemlerini gerçekleştirmek için bir terminal veya 
komut istemi açın.

2.  **Klasörün İçine Girin:**  Terminalde, `DemoKlasimleri` klasörünün bulunduğu dizine 
gidin.  (Örneğin, `cd /path/to/DemoKlasimleri`)

3.  **Derleme:**  Aşağıdaki komutu kullanarak `Demo.java` dosyasını derleyin:

    ```bash
    javac Demo.java
    ```

    Bu komut, `Demo.class` dosyası ve gerekli tüm derlenmiş dosyaları oluşturacaktır.

4.  **Çalıştırma:**  Aşağıdaki komutu kullanarak derlenmiş `Demo` sınıfını çalıştırın:

    ```bash
    java DemoKlasimleri.Demo
    ```

    Bu, `Demo` sınıfının `main` metodunu çalıştıracak ve konsolda çıktıları 
gösterecektir.

**Çıktı:**

Programın çıktısı aşağıdaki gibi olacaktır:

```
abc
   
null
0
```

**Önemli Notlar:**

*   **NullPointerException:** `str3` değişkeni başlangıçta `null` değerine sahiptir. 
`str3.length()` metodunu çağırmadan önce `str3`'e bir değer atamanız gerekir, aksi 
takdirde `NullPointerException` hatası oluşur.
*   **Paketler:** Paketler, kodunuzu daha düzenli ve yönetilebilir hale getirir.  
Paketleri, kodunuzu farklı projeler arasında paylaşmanıza ve daha karmaşık uygulamalarda 
kodunuzu yönetmenize yardımcı olabilir.

Umarım bu açıklama, Java programınızı ayrı dosyalarla nasıl oluşturacağınızı ve 
çalıştıracağınızı anlamanıza yardımcı olur. Başka sorularınız olursa çekinmeyin!
