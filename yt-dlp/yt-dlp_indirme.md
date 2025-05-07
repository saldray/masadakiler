Elbette, yt-dlp ile bir videoyu ve altyazısını indirmek oldukça kolaydır. İşte size adım adım nasıl yapacağınızı gösteren bir örnek:

**Temel Komut:**

```bash
yt-dlp --write-subs --embed-subs <video_url>
```

**Komutun Açıklaması:**

* `yt-dlp`: yt-dlp programını çalıştırır.
* `--write-subs`: Bu seçenek, mevcut olan tüm altyazı dosyalarını (genellikle `.vtt` veya `.srt` formatında) indirir.
* `--embed-subs`: Bu seçenek, indirilen altyazı dosyalarını doğrudan video dosyasına gömer. Bu sayede videoyu oynatırken altyazılar otomatik olarak görünür.
* `<video_url>`: İndirmek istediğiniz YouTube videosunun veya desteklenen diğer platformlardaki videonun URL'sini buraya yapıştırın.

**Örnek Kullanım:**

Diyelim ki indirmek istediğiniz video şu URL'ye sahip: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`

Bu durumda kullanmanız gereken komut şu olacaktır:

```bash
yt-dlp --write-subs --embed-subs https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

**Ek Seçenekler:**

* **Belirli Bir Altyazı Dilini İndirme:** Birden fazla dilde altyazı mevcutsa ve sadece belirli bir dili indirmek istiyorsanız `--sub-lang` seçeneğini kullanabilirsiniz. Örneğin, sadece İngilizce altyazıyı indirmek için:

    ```bash
    yt-dlp --write-subs --embed-subs --sub-lang en <video_url>
    ```

    Birden fazla dili indirmek için dilleri virgülle ayırabilirsiniz: `--sub-lang en,tr`

* **Altyazıları Ayrı Bir Dosya Olarak Kaydetme:** Altyazıları videoya gömmek yerine ayrı bir dosya olarak kaydetmek isterseniz `--embed-subs` seçeneğini kullanmayın. Sadece `--write-subs` yeterli olacaktır. Altyazı dosyası, video dosyasıyla aynı dizine ve aynı isimle (farklı bir uzantıyla) kaydedilecektir.

    ```bash
    yt-dlp --write-subs <video_url>
    ```

* **Altyazı Formatını Belirtme:** İndirilecek altyazıların formatını belirtmek için `--sub-format` seçeneğini kullanabilirsiniz. Örneğin, altyazıları `.srt` formatında indirmek için:

    ```bash
    yt-dlp --write-subs --sub-format srt <video_url>
    ```

**Özet:**

Bir videoyu ve altyazısını yt-dlp ile indirmek için genellikle şu komutu kullanırsınız:

```bash
yt-dlp --write-subs --embed-subs <video_url>
```

İhtiyaçlarınıza göre `--sub-lang` ve `--sub-format` gibi ek seçenekleri de kullanabilirsiniz.
