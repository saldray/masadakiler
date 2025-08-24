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


-----



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

Durum	Komut
Dosya Kopyalama	docker cp <yerel_dosya> <konteyner_adı>:<hedef_dizin>
Dizindeki her şeyi kopyalama	docker cp <yerel_dizin>/. <konteyner_adı>:<hedef_dizin>
Dizinin kendisini kopyalama	docker cp <yerel_dizin> <konteyner_adı>:<hedef_dizin>

Unutmayın, bu komut sadece çalışan konteynerler için geçerlidir. docker ps komutu ile çalışan konteynerleri listeleyip adını veya ID'sini öğrenebilirsiniz.


------------


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



----------


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

Durum	Komut
Dosya Kopyalama	docker cp <yerel_dosya> <konteyner_adı>:<hedef_dizin>
Dizindeki her şeyi kopyalama	docker cp <yerel_dizin>/. <konteyner_adı>:<hedef_dizin>
Dizinin kendisini kopyalama	docker cp <yerel_dizin> <konteyner_adı>:<hedef_dizin>

Unutmayın, bu komut sadece çalışan konteynerler için geçerlidir. docker ps komutu ile çalışan konteynerleri listeleyip adını veya ID'sini öğrenebilirsiniz.

tar.gz uzantılı dosyayı bilgisayardan docker image a copyalama

.tar.gz uzantılı bir dosyayı yerel bilgisayarınızdan bir Docker konteynerine kopyalamanın iki ana yolu vardır:

    Çalışan bir konteynere kopyalama: Bu, en yaygın ve hızlı yöntemdir. docker cp komutunu kullanarak, tıpkı normal bir cp komutu gibi dosya transferi yapabilirsiniz.

    İmaj oluşturma aşamasında kopyalama: Eğer dosyayı, konteyner her başlatıldığında içinde olmasını istediğiniz bir uygulamanın parçası olarak görüyorsanız, Dockerfile kullanarak imajın içine dahil edebilirsiniz.

Yöntem 1: Çalışan Bir Konteynere Kopyalama

Bu yöntem, zaten çalışan bir konteynere anlık bir dosya transferi yapmak istediğinizde idealdir.

1. Konteynerinizi Hazırlayın

Öncelikle kopyalamayı yapacağınız konteynerin çalıştığından emin olun. Konteynerin adını veya ID'sini öğrenmek için docker ps komutunu kullanabilirsiniz.
Bash

docker ps

Çıktıdan konteynerinizin adını veya ID'sini not alın. (Örnek: my-ubuntu-container)

2. docker cp Komutunu Kullanın

Yerel makinenizdeki .tar.gz dosyasını (~/dosya.tar.gz) çalışan konteynerin içine (/usr/src) kopyalamak için aşağıdaki komutu kullanın:
Bash

docker cp ~/dosya.tar.gz my-ubuntu-container:/usr/src/

Bu komut, sıkıştırılmış dosyanızı olduğu gibi kopyalar. Dosyayı konteynerin içinde açmak (extract) için konteynere bağlanıp tar komutunu kullanmanız gerekir.

3. Dosyayı Konteyner İçinde Açma (İsteğe Bağlı)

Konteynerin içine girerek kopyaladığınız .tar.gz dosyasını açabilirsiniz.
Bash

# Konteynerin içine bağlanın
docker exec -it my-ubuntu-container /bin/bash

# Kopyaladığınız dizine gidin
cd /usr/src/

# Dosyayı açın
tar -xzvf dosya.tar.gz

    -x: Sıkıştırılmış dosyayı açar.

    -z: gzip sıkıştırmasını çözmek için kullanılır (.gz uzantılı dosyalar için).

    -v: İşlem sırasında dosyaları gösterir (verbose).

    -f: İşlem yapılacak dosyayı belirtir.

Yöntem 2: Dockerfile ile İmaj Oluşturma Aşamasında Kopyalama

Bu yöntem, uygulamanızın kalıcı bir parçası olacak dosyaları dahil etmek için en iyi uygulamadır. Her yeni konteyner bu dosyayı otomatik olarak içerecektir.

1. Dockerfile Oluşturma

Proje dizininizde bir Dockerfile oluşturun ve aşağıdaki içeriği ekleyin:
Dockerfile

# Temel imajı belirleyin
FROM ubuntu:latest

# Uygulamanızın çalışacağı dizini belirleyin
WORKDIR /usr/src/app

# .tar.gz dosyasını kopyalayın
COPY ./dosya.tar.gz .

# Kopyaladığınız dosyayı açın
RUN tar -xzvf dosya.tar.gz

# .tar.gz dosyasını silin (isteğe bağlı, imaj boyutunu küçültür)
RUN rm dosya.tar.gz

# Uygulamanız için gerekli diğer komutları ekleyin
# ...

    COPY: Bu komut, yerel makinenizdeki dosyayı Docker imajının içine kopyalar.

    RUN: Bu komut, imaj oluşturulurken bir komut çalıştırmanızı sağlar. Burada tar komutu ile .tar.gz dosyasını açıyoruz.

2. Docker İmajını Oluşturma

Dockerfile ve dosya.tar.gz dosyasının bulunduğu dizinde aşağıdaki komutu çalıştırarak yeni bir imaj oluşturun:
Bash

docker build -t benim-ubuntu-uygulamam .

Bu komut, bulunduğunuz dizini (.) "build context" olarak belirler ve Dockerfile'ı kullanarak benim-ubuntu-uygulamam adında yeni bir imaj oluşturur. Bu imajın içinde .tar.gz dosyası açılmış ve içeriği yerleştirilmiş olacaktır.

Bu iki yöntem de .tar.gz dosyanızı Docker ortamına taşımanıza olanak tanır. Hangi yöntemi seçeceğiniz, dosyanın ne amaçla kullanılacağına bağlıdır. Eğer geçici bir işlemse docker cp, kalıcı bir kurulumun parçasıysa Dockerfile kullanmak en doğru yaklaşımdır.





