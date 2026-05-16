#  E-Ticaret Müşteri Zekası: Uçtan Uca Veri Analitiği

Bu çalışma, devasa hacimli ham e-ticaret verilerini anlamlı ticari içgörülere dönüştüren bir veri bilimi projesidir. Proje kapsamında sadece görselleştirme yapılmamış, veriler arasındaki gizli korelasyonlar ve müşteri davranış kalıpları ortaya çıkarılmıştır.

---

#  Neler Yaptık? 

## 1. Veri Entegrasyonu ve Akıllı Temizlik (ETL)

###  Çoklu Kaynak Birleştirme
Shopping, Behavior ve Reviews veri setleri; müşterilerin demografik özellikleri ile satın alma sonrası memnuniyet puanlarını eşleştirmek amacıyla birleştirildi.

###  Veri Standartlaştırma
Kolon isimlerindeki düzensizlikler (boşluklar, büyük/küçük harf hataları vb.) `regex` ve `pandas` fonksiyonları kullanılarak temizlendi ve hatasız bir veri hattı (pipeline) oluşturuldu.

###  Eksik Veri Yönetimi
Memnuniyet puanı bulunmayan satırlar, kategorik ortalamalar kullanılarak “akıllı doldurma” yöntemiyle tamamlandı.

---

## 2. Müşteri Segmentasyonu ve Feature Engineering

###  Yaş Gruplandırma
Ham yaş verisi, pazarlama stratejilerine uygun olacak şekilde 6 farklı segmente ayrıldı:

- 0-18
- 19-25
- 26-35
- 36-45
- 46-60
- 60+

###  Harcama Analitiği
Birim fiyat ve miktar çarpılarak toplam sepet tutarı (`total_amount`) hesaplandı ve aykırı değerler (outliers) kontrol edildi.

---

## 3. Derinlemesine Davranış Analizi

###  Kategori Dominansı
Her yaş grubunun sepetindeki baskın kategoriler “Pazar Payı” yaklaşımıyla analiz edildi.

###  Trend Tespiti
Genç segmentin moda odaklı tüketimi ile orta yaş segmentinin teknoloji ve ayakkabı odaklı yüksek hacimli tüketimi arasındaki farklar istatistiksel olarak doğrulandı.

---

#  Öne Çıkan Bulgular

| Yaş Grubu | Favori Kategori | Davranış Özeti |
|---|---|---|
| 0-18 | Clothing | Düşük sepet tutarı, yüksek işlem hacmi |
| 46-60 | Technology | En yüksek toplam ciro katkısı ve premium ürün tercihi |
| 60+ | Shoes / Clothing | Daha stabil ama yüksek kaliteli alışveriş alışkanlığı |

---

#  Dashboard Özellikleri

##  Canlı Filtreleme
Kullanıcıların yaş grubuna göre anlık kategori dağılımını görmesini sağlayan interaktif seçim kutuları.

##  Dinamik Metrikler
Toplam satış hacmi, ortalama sepet tutarı ve en popüler kategorinin anlık takibi.

##  Kıyaslama Modu (A/B Testi Görünümü)
İki farklı yaş grubunun tercihlerini yan yana getiren “Düello” ekranı.

---

#  Dosya Yapısı ve Kurulum

```bash
project/
│
├── analysis.ipynb   # Verinin mutfağı. Tüm temizlik ve ML denemeleri burada.
├── app.py           # Kullanıcıya sunulan dashboard arayüzü.
├── data/            # Ham CSV dosyalarının merkezi deposu.
└── README.md