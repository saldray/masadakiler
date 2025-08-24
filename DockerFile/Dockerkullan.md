Linux komutlarını öğrenmek için Docker'da bir konteyner oluşturmak çok pratik bir yöntemdir. Bu sayede, kendi sisteminize herhangi bir şey kurmanıza gerek kalmadan, izole bir Linux ortamında güvenle pratik yapabilirsiniz.

İşte en basit ve etkili yolu:

1. Ubuntu İmajını Kullanarak Konteyner Oluşturma ve Başlatma

Terminalinizi açın ve aşağıdaki komutu çalıştırın:
Bash

docker run -it ubuntu:latest bash

Bu tek satırlık komutun ne anlama geldiğini açıklayalım:

    docker run: Yeni bir Docker konteyneri oluşturma ve çalıştırma komutudur.

    -it: Bu kısım çok önemlidir ve iki ayrı seçeneği birleştirir:

        -i (--interactive): Konteynerin STDIN (standart girdi) akışını açık tutar. Bu, komutları yazabilmenizi sağlar.

        -t (--tty): Konteynere bir pseudo-TTY (sanal terminal) atar. Bu da size komut satırını kullanabileceğiniz bir etkileşimli kabuk sağlar.

    ubuntu:latest: Bu, kullanmak istediğiniz Docker imajının adıdır. ubuntu imajı, temiz bir Ubuntu Linux işletim sistemi içerir. :latest etiketi, imajın en son sürümünü çekmesini sağlar.

    bash: Konteyner başlatıldığında çalıştırılacak olan komuttur. Bu durumda, bash kabuğunu başlatır.

Komutu çalıştırdığınızda, Docker bilgisayarınızda ubuntu:latest imajı yoksa onu otomatik olarak Docker Hub'dan çekecek (indirecek) ve ardından size bir bash kabuğu açacaktır.

2. Linux Komutlarını Öğrenmeye Başlama

Artık terminalinizde konteynerin içindesiniz! Komut satırı root@<konteyner_id>:/# şeklinde görünecektir. Buradan itibaren tüm Linux komutlarını güvenle çalıştırabilirsiniz.

Örnek Komutlar:

    ls: Bulunduğunuz dizindeki dosyaları ve klasörleri listeler.

    pwd: Hangi dizinde olduğunuzu gösterir (print working directory).

    cd /: Kök dizine (/) geçiş yapar.

    mkdir deneme: "deneme" adında yeni bir klasör oluşturur.

    touch dosya.txt: "dosya.txt" adında yeni bir dosya oluşturur.

    apt update: Paket yöneticisinin güncellemelerini çeker. (Sistem paketlerini kurmak için apt install kullanabilirsiniz.)

3. Konteynerden Çıkış Yapma

Öğrenme seansınız bittiğinde, konteynerden çıkmak için terminale exit yazmanız yeterlidir. Konteyner otomatik olarak duracaktır.
Bash

exit

Eğer sadece konteynerden çıkmak ancak arka planda çalışmaya devam etmesini isterseniz, Ctrl + p ve Ctrl + q tuşlarına birlikte basabilirsiniz. Daha sonra docker start <konteyner_id> komutu ile tekrar başlatabilirsiniz.

Bu yöntem, temiz ve geçici bir ortam sağladığı için Linux komutlarını denemek ve öğrenmek için en ideal yoldur.

---------

Linux komutlarını öğrenmek için Docker'da bir imaj kurmak harika bir yöntemdir. Sanal bir ortam oluşturarak sisteminize zarar verme endişesi olmadan dilediğinizce pratik yapabilirsiniz.

İşte adım adım yapmanız gerekenler:

1. Docker'ı Yükleyin

Eğer bilgisayarınızda Docker yüklü değilse, öncelikle Docker'ı kurmanız gerekir. Kendi işletim sisteminize (Windows, macOS, Linux) uygun kurulum adımlarını Docker'ın resmi web sitesinde bulabilirsiniz.

2. Linux İmajını Çekin (Pull)

Docker'ı kurduktan sonra, öğrenmek için kullanabileceğiniz hafif bir Linux dağıtımı imajını Docker Hub'dan çekmeniz gerekir. Ubuntu veya Centos bu iş için en popüler ve uygun seçeneklerdir. Terminalinizi açın ve aşağıdaki komutlardan birini çalıştırın:

Ubuntu için:
Bash

docker pull ubuntu

veya

CentOS için:
Bash

docker pull centos

Bu komutlar, seçtiğiniz işletim sisteminin en son versiyonunu indirir.

3. İmajı Çalıştırın ve Konteynere Bağlanın

İmajı indirdikten sonra, bu imajdan bir konteyner oluşturup içine bağlanmanız gerekir. Konteyner, sizin pratik yapacağınız izole edilmiş sanal ortamdır.

Aşağıdaki komutu kullanarak bir konteyner oluşturup içine bağlanın:

Ubuntu için:
Bash

docker run -it ubuntu /bin/bash

veya

CentOS için:
Bash

docker run -it centos /bin/bash

Bu komuttaki parametrelerin anlamları şunlardır:

    run: Belirttiğiniz imajdan yeni bir konteyner oluşturur.

    -it: Bu iki harfin birleşimi, interaktif (interactive) ve tty (terminal) oturumu sağlar. Bu sayede konteynerin içinde komut çalıştırabilir ve çıktısını görebilirsiniz.

    ubuntu veya centos: Kullanacağınız imajın adı.

    /bin/bash: Konteynerin içinde çalışacak kabuk (shell). Bu komut, konteyner başlar başlamaz sizi bash kabuğuna yönlendirir.

4. Linux Komutlarını Keşfedin!

Tebrikler! Artık bir Linux ortamının içindesiniz. Komut satırınız muhtemelen root@<konteyner_id>:/# şeklinde görünecektir.

Artık temel Linux komutlarını rahatlıkla deneyebilirsiniz. İşte başlayabileceğiniz birkaç örnek:

    ls: İçinde bulunduğunuz dizindeki dosyaları ve klasörleri listeler.

    pwd: Hangi dizinde olduğunuzu gösterir (print working directory).

    cd: Dizin değiştirmenize yarar.

    mkdir <klasör_adı>: Yeni bir klasör oluşturur.

    touch <dosya_adı>: Yeni bir dosya oluşturur.

    rm <dosya_adı>: Bir dosyayı siler.

    cp <kaynak> <hedef>: Bir dosyayı kopyalar.

    mv <kaynak> <hedef>: Bir dosyayı taşır veya adını değiştirir.

5. Konteynerden Çıkış Yapma

Komut denemeleriniz bittikten sonra, konteynerden çıkmak için exit komutunu kullanmanız yeterlidir.
Bash

exit

Bu komut, hem kabuktan çıkar hem de çalışan konteyneri durdurur.

Bu yöntem, gerçek bir sistem kurmaya göre hem daha hızlı hem de daha güvenlidir. Dilediğiniz zaman konteyneri silip baştan başlayabilirsiniz. Linux komutlarını öğrenmek için çok verimli bir pratik yöntemidir.

Başka hangi Linux komutlarını öğrenmek istersiniz?


--------

docker ubuntu image'inın içine dizin nasıl kopyalanır

Docker'da çalışan bir Ubuntu imajının içine dosya veya dizin kopyalamanın en yaygın ve etkili yolu docker cp komutunu kullanmaktır. Bu komut, çalışan bir konteyner ile yerel makineniz arasında dosya transferi yapmanızı sağlar.

İşte adım adım nasıl yapılacağı:

1. Kopyalamak İstediğiniz Dosya ve Konteyneri Hazırlayın

Öncelikle, yerel makinenizde kopyalamak istediğiniz dosya veya dizin hazır olmalı.

Ayrıca, bir Ubuntu konteynerinin çalışıyor olması gerekir. Eğer çalışmıyorsa, aşağıdaki komutla bir konteyner başlatabilirsiniz:
Bash

docker run -it -d --name my-ubuntu ubuntu

Bu komuttaki parametreler:

    -it: İnteraktif ve TTY oturumu açar.

    -d: Konteyneri arka planda (detached) çalıştırır.

    --name my-ubuntu: Konteynerinize kolayca hatırlayabileceğiniz bir isim verir.

2. docker cp Komutunu Kullanın

Konteyneriniz çalıştıktan sonra, yerel makinenizdeki bir dosyayı veya dizini bu konteynerin içine kopyalayabilirsiniz.

a) Tek Bir Dosyayı Kopyalamak

Yerel makinenizdeki belgelerim/rapor.txt dosyasını my-ubuntu adlı konteynerin içindeki /home dizinine kopyalamak için:
Bash

docker cp belgelerim/rapor.txt my-ubuntu:/home/

b) Bir Dizin İçindeki Tüm Dosyaları Kopyalamak

Yerel makinenizdeki projelerim adlı dizini, içindeki tüm dosyalarla birlikte my-ubuntu konteynerinin içindeki /usr/local/ dizinine kopyalamak için:
Bash

docker cp projelerim/. my-ubuntu:/usr/local/

projelerim/. şeklinde dizin adının sonuna . koyarak o dizinin içindeki her şeyi kopyalamayı belirtirsiniz.

c) Dizinin Kendisini Kopyalamak

Eğer projelerim dizininin kendisini ve içindekileri kopyalamak isterseniz:
Bash

docker cp projelerim my-ubuntu:/usr/local/

Bu komut, /usr/local/projelerim adında yeni bir dizin oluşturup içine dosyaları kopyalar.

3. Kopyalanan Dosyayı Kontrol Etme

Dosyanın başarıyla kopyalandığından emin olmak için konteynere bağlanıp kontrol edebilirsiniz:
Bash

docker exec -it my-ubuntu /bin/bash

Konteynerin içine girdikten sonra, kopyaladığınız dizine giderek dosyaları listeleyin:
Bash

cd /usr/local/
ls

Eğer her şey yolundaysa, kopyaladığınız dosya veya dizini burada görebilirsiniz.

Özetle

Durum	                                Komut
Dosya Kopyalama         	            docker cp <yerel_dosya> <konteyner_adı>:<hedef_dizin>
Dizindeki her şeyi kopyalama    	    docker cp <yerel_dizin>/. <konteyner_adı>:<hedef_dizin>
Dizinin kendisini kopyalama	            docker cp <yerel_dizin> <konteyner_adı>:<hedef_dizin>














