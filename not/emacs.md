Emacs’te açık buffer’ları kapatmanın birkaç pratik yolu var:

- Tek bir buffer’ı kapatma:
  - İmleç o buffer’ın içindeyken **C-x k** (kill-buffer) → buffer kapanır.

- Mevcut pencereyi/sekmeyi kapatma (buffer’ı değil):
  - **C-x 0** ile o pencere kapanır; buffer arka planda açık kalabilir.

- Tüm buffer’ları (veya belirli türleri) kapatma:
  - **M-x kill-some-buffers** → listeden seçim yaparak kapat.
  - **M-x kill-matching-buffers** → örüntüye uyan buffer’ları kapat.

İstersen, hangi Emacs kullandığını (vanilla / Spacemacs / Doom) ve “pencere mi buffer mı” kapatmak istediğini söyle; ona göre en hızlı kısayolu söyleyebilirim.
