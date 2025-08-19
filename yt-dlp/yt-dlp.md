Fedora 42'ye yt-dlp'yi kurmak için birkaç farklı yöntem bulunmaktadır. En yaygın ve tavsiye edilen yollar, pip kullanarak veya RPM Fusion deposunu etkinleştirerek kurulum yapmaktır.

Yöntem 1: pip ile Kurulum (Önerilen)

Bu yöntem, yt-dlp'yi sisteminizden bağımsız bir şekilde kurmanızı sağlar ve en güncel sürümü edinmenin en kolay yoludur.

    Gerekli Paketleri Kurun: Öncelikle, pip paket yöneticisini ve gerekli bazı Python geliştirme araçlarını kurmalısınız. Terminali açın ve aşağıdaki komutu çalıştırın:
    Bash

sudo dnf install python3-pip python3-devel

yt-dlp'yi Kurun: Şimdi, pip kullanarak yt-dlp'yi sisteminize kurabilirsiniz. Genellikle ~/.local/bin dizinine kurulur, bu nedenle $PATH değişkeninizde bu dizinin olduğundan emin olun.
Bash

pip install --user yt-dlp

Eğer $PATH'inizde bu dizin yoksa veya komutun çalışmadığını fark ederseniz, şu komutu kullanabilirsiniz:
Bash

pip install --user yt-dlp && echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc

Bu komut, kurulumu yapar ve $PATH'inizi güncelleyerek yt-dlp'yi doğrudan terminalden çalıştırabilmenizi sağlar.

FFmpeg'i Kurun: Videoları dönüştürmek, ses ayıklamak ve diğer işlemleri yapmak için FFmpeg'e ihtiyacınız olacaktır. Onu da DNF ile kurabilirsiniz:
Bash

    sudo dnf install ffmpeg

Yöntem 2: RPM Fusion Deposunu Kullanarak Kurulum

Bu yöntem, yt-dlp'yi DNF paket yöneticinizle sistem genelinde yönetmeyi tercih ediyorsanız kullanışlıdır.

    RPM Fusion Deposunu Etkinleştirin: yt-dlp, Fedora'nın varsayılan depolarında bulunmaz. Bu yüzden önce RPM Fusion free deposunu etkinleştirmelisiniz.
    Bash

sudo dnf install \
  https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm

yt-dlp'yi Kurun: Depo etkinleştirildikten sonra, DNF komutuyla yt-dlp'yi kolayca kurabilirsiniz.
Bash

    sudo dnf install yt-dlp

    Bu yöntem aynı zamanda FFmpeg bağımlılığını da otomatik olarak kurmalıdır.

Kurulumu Kontrol Etme

Kurulumu tamamladıktan sonra, yt-dlp'nin doğru bir şekilde kurulduğundan emin olmak için versiyonunu kontrol edebilirsiniz:
Bash

yt-dlp --version

Eğer versiyon numarası ekrana basılırsa, yt-dlp başarıyla kurulmuş demektir. Artık videoları indirmek için kullanmaya hazırsınız!

Hangi yöntemin size daha uygun olduğunu düşünüyorsunuz?




yt-dlp ile bir videoyu altyazılarıyla birlikte indirmek için birden fazla yöntem var. En yaygın ve pratik olanları aşağıda bulabilirsin.

Video ve Ayrı Altyazı Dosyası İndirme

Bu yöntem, video dosyasının yanında, altyazıları ayrı bir dosya (genellikle .srt veya .vtt formatında) olarak kaydeder.

    Öncelikle, indirmek istediğin videonun mevcut altyazı dillerini görmek için şu komutu kullanabilirsin:

    yt-dlp --list-subs "VİDEO_URL"

    Bu komut, videoda hangi dillerin ve formatların (örneğin, tr için Türkçe, en için İngilizce) olduğunu listeler.

    İstediğin dili belirledikten sonra, videoyu ve altyazıyı beraber indirmek için aşağıdaki komutu kullan:

    yt-dlp --write-sub --sub-lang "tr" "VİDEO_URL"

    Bu komuttaki --write-sub seçeneği, altyazıları indirmeyi sağlar. --sub-lang "tr" ise Türkçe altyazıları seçer. Eğer birden fazla dil indirmek istersen, dilleri virgülle ayırabilirsin (örneğin, --sub-lang "tr,en").

Altyazıları Videoya Gömme (Hardcoded Subtitles)

Bu yöntem, altyazıları doğrudan video dosyasına "yakarak" ekler. Bu sayede, altyazılar her zaman videoyla birlikte görünür ve ayrıca bir altyazı dosyasına ihtiyaç duyulmaz. Ancak, bu işlem videoyu yeniden kodlamayı gerektirdiği için daha uzun sürer ve ffmpeg'in sistemine kurulu olması gerekir.

yt-dlp --write-sub --sub-lang "tr" --embed-subs --embed-metadata --merge-output-format mp4 "VİDEO_URL"

Bu komuttaki ek seçeneklerin anlamları:

    --embed-subs: Altyazıları video dosyasına gömer.

    --embed-metadata: Video bilgilerini (başlık, açıklama vb.) dosyaya gömer.

    --merge-output-format mp4: Farklı formatlardaki video ve ses akışlarını birleştirerek nihai çıktıyı .mp4 formatında oluşturur.

Not: Bu yöntem, video kalitesine bağlı olarak dosya boyutunu artırabilir. Eğer videoyu farklı cihazlarda altyazısız izleme esnekliği istiyorsan, ilk yöntemi tercih etmen daha iyi olacaktır.



Video ve Altyazıyı Birlikte İndirme

yt-dlp ile bir videoyu ve onun altyazılarını aynı anda indirmek oldukça kolaydır. İşte size en yaygın kullanılan komutlar ve açıklamaları:

1. Otomatik Altyazı Seçimi

Bu komut, videonun mevcut tüm altyazılarını (otomatik olarak oluşturulanlar dahil) bulur ve indirir.

yt-dlp --write-sub --embed-sub [video_link]

    --write-sub veya -S: Mevcut altyazıları indirir.

    --embed-sub: İndirilen altyazıyı video dosyasına gömer. Bu sayede, video oynatılırken altyazılar otomatik olarak görünür.

2. Belirli Bir Dildeki Altyazıyı İndirme

Eğer sadece belirli bir dildeki altyazıyı indirmek isterseniz, dil kodunu belirtmeniz gerekir. Örneğin, Türkçe altyazı için tr kullanabilirsiniz.

yt-dlp --write-sub --sub-lang tr --embed-sub [video_link]

    --sub-lang tr: Sadece Türkçe altyazıları indirir. Birden fazla dil için en,tr gibi virgülle ayırarak ekleyebilirsiniz.

3. Farklı Formatlarda İndirme

Bazen altyazıları ayrı bir dosya olarak indirmek daha faydalı olabilir. Bu durumda, --embed-sub komutunu kullanmanıza gerek yoktur. Aşağıdaki komutlar, altyazıları video ile aynı isimde ayrı bir .vtt veya .srt dosyası olarak kaydeder.

a) VTT Formatında İndirme:

yt-dlp --write-sub --sub-langs tr --convert-subs vtt [video_link]

b) SRT Formatında İndirme:

yt-dlp --write-sub --sub-langs tr --convert-subs srt [video_link]

    --convert-subs: Altyazı dosyasını belirttiğiniz formata dönüştürür. Çoğu video oynatıcı, hem .vtt hem de .srt dosyalarını destekler.

Ek İpuçları

    En iyi video ve ses kalitesini seçmek için: Genellikle altyazı komutlarıyla birlikte -f bestvideo+bestaudio/best komutunu kullanmanız önerilir. Bu, en iyi görüntü ve ses kalitesini ayrı ayrı indirip birleştirir.

    yt-dlp -f bestvideo+bestaudio/best --write-sub --embed-sub [video_link]

    Kullanılabilir altyazı dillerini görmek için: Bir videoda hangi dillerde altyazı bulunduğunu öğrenmek isterseniz, şu komutu kullanabilirsiniz:

    yt-dlp --list-subs [video_link]

    Oynatma listesi indirme: Eğer bir oynatma listesindeki tüm videoları altyazılarıyla birlikte indirmek isterseniz, oynatma listesi linkini kullanmanız yeterlidir. yt-dlp her bir video için aynı komutu uygular.

    yt-dlp --write-sub --embed-sub [oynatma_listesi_linki]







