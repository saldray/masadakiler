## 💾 Linux'ta `/tmp` Dizininin Görevi

Linux dosya sistemi hiyerarşisinde (`FHS`), `/tmp` dizini, sistemde çalışan programlar tarafından geçici (temporary) dosyaları depolamak için ayrılmış özel bir alandır.

Bu dizinin temel görevi, **kısa ömürlü ve kalıcı olması gerekmeyen veriler** için hızlı erişimli bir depolama alanı sağlamaktır.

---

## 🎯 Temel Özellikleri ve İşlevi

### 1. Geçici Depolama Alanı

* **Amaç:** Programlar, çalışma sırasında ihtiyaç duydukları ara verileri (örneğin, büyük bir dosya sıkıştırılırken oluşturulan geçici parçalar, tarayıcı önbelleği, oturum verileri) buraya yazar.
* **Kullanıcılar:** Herhangi bir kullanıcı ve uygulama, genellikle kendi geçici dosyalarını oluşturmak için bu dizini kullanabilir.

### 2. Otomatik Temizleme (Volatility)

`/tmp` dizininin en kritik özelliği, içerdiği verilerin **kalıcı olmamasıdır**.

* **Yeniden Başlatma (Reboot):** Geleneksel olarak, sistem yeniden başlatıldığında `/tmp` dizinindeki tüm dosyalar silinir.
* **Zaman Tabanlı Temizleme:** Modern Linux dağıtımlarında (Fedora, Debian, Ubuntu vb.) kullanılan `systemd` ve `tmpfiles.d` servisleri, belirli bir süreden (genellikle 10 gün) daha eski olan dosya ve klasörleri sistem çalışırken bile düzenli olarak otomatik olarak temizler. Bu işlem, dizinin dolmasını engeller.

### 3. Güvenlik ve İzinler

* **Yapı:** `/tmp` dizini genellikle **`sticky bit`** (yapışkan bit) izniyle (`t` veya `1777`) ayarlanmıştır.
* **Anlamı:** Bu izin, bir kullanıcının başkasının sahip olduğu geçici dosyaları **silmesini veya değiştirmesini engeller**. Her kullanıcı, yalnızca kendi oluşturduğu dosyaları veya kendisine ait dizinleri silebilir. Bu, uygulamalar arasında bir güvenlik katmanı oluşturur.

---

## ⚠️ `/var/tmp` ile Farkı

Linux sistemlerinde geçici dosyalar için kullanılan bir diğer dizin de `/var/tmp`'dir. Aralarındaki fark şudur:

| Dizin | Temizleme Prensibi | Amaç |
| :--- | :--- | :--- |
| **`/tmp`** | **Sistem yeniden başlatıldığında SİLİNİR.** | Kısa süreli işlemler ve anlık geçici veriler. |
| **`/var/tmp`** | **Yeniden başlatmaya dayanıklıdır (Kalıcıdır).** | Yeniden başlatmalar arasında korunması gereken, ancak yine de geçici olan büyük veya uzun süreli veriler (örneğin, büyük bir yazılım paketi derlenirken kullanılan ara dosyalar). |










