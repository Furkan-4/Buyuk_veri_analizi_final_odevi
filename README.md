BÜYÜK VERİ ANALİZİ FİNAL PROJE RAPORU
Öğrenci Adı Soyadı: [Furkan Yıldız]
Öğrenci Numarası: [22430040010]
GitHub Proje Linki: [https://github.com/Furkan-4/Buyuk_veri_analizi_final_odevi]
Yöntem: Keşifçi Veri Analizi (EDA), İstatistiksel Risk İncelemesi ve Sınıflandırma Modelleri
Tarih: 16.06.2026
1. GİRİŞ VE VERİ SETİ
Bu çalışmada, bireylerin yaşam tarzı ve klinik ölçümlerini içeren dATA.csv veri seti analiz edilmiştir. Veri seti 327 katılımcıya ve 21 farklı niteliğe sahiptir. Eksik değer (NaN) veya mükerrer kayıt bulunmamaktadır. Metinsel kategorik veriler modelleme aşaması için LabelEncoder ile sayısal formata dönüştürülmüştür.
2. TANIMLAYICI İSTATİSTİKLER
•	Heart Patient (Hedef Değişken): Veri setinde 108 kalp hastası (%33.03) ve 219 sağlıklı birey (%66.97) yer almaktadır.
•	BMI (Vücut Kitle İndeksi): Popülasyonun BMI ortalaması 25.24'tür (Hafif kilolu sınırındadır). Minimum BMI 16.51, maksimum ise 42.46'dır.
•	Demografi: Popülasyonda erkek katılımcı sayısı (196) kadınlardan (131) fazladır. En yoğun yaş grubu 50 yaş üstüdür.
3. RİSK FAKTÖRÜ ANALİZİ (ÇAPRAZ TABLO BULGULARI)
•	Yaş (Age): 35 yaş altındaki grupta kalp hastalığı oranı %11.49 iken, 50 yaş üstü grupta bu oran %51.15'e yükselmektedir. Yaşlanma doğal bir risk faktörüdür.
•	Kan Basıncı (Blood Pressure): Hipertansiyon hastalarının %58.14'ü kalp hastasıdır. Normal tansiyonlularda bu oran %19.67'dir.
•	Fiziksel Aktivite: Haftada 5 gün veya daha fazla spor yapan bireylerin %100'ü sağlıklıdır; aralarında hiç kalp hastası yoktur.
•	Diyabet: Diyabet hastalarının %41.18'inde kalp rahatsızlığı görülürken, diyabeti olmayanlarda bu oran %21.90'dır.
4. MAKİNE ÖĞRENMESİ MODELLERİ VE PERFORMANS
Verinin %80'i eğitim, %20'si test olarak ayrılarak iki farklı algoritma eğitilmiştir:
1.	Lojistik Regresyon (Logistic Regression): Doğruluk (Accuracy): %77.27, Keskinlik (Precision): %81.82, Duyarlılık (Recall): %40.91, F1-Skor: %54.55.
2.	Rastgele Orman (Random Forest): Doğruluk (Accuracy): %74.24, Keskinlik (Precision): %72.73, Duyarlılık (Recall): %36.36, F1-Skor: %48.48.
Model Yorumu: Test setinde en kararlı ve yüksek başarıyı Lojistik Regresyon göstermiştir. Ancak her iki modelin de Recall (Duyarlılık) değerleri düşüktür (%40.91 ve %36.36). Sağlık sektöründe Recall hayati önem taşır; çünkü gerçek hastaları gözden kaçırmamak (False Negative sonucunu engellemek) gerekir. Modellerin tahmin gücü bu yönüyle zayıftır.
5. SONUÇ VE DEĞERLENDİRME
•	Analiz bulguları tıp literatürüyle (yaş, yüksek tansiyon, diyabet ve hareketsizliğin kalp hastalığını tetiklemesi) tamamen uyumludur.
•	Veri setinin eksik veri barındırmaması güçlü yönü; ancak 327 satır gibi küçük bir örnekleme sahip olması ve anket beyanına dayanması zayıf yönüdür.
•	Bu verilerle gerçek hayatta klinik/tıbbi bir karar asla verilemez. Güvenilir bir tıbbi modelleme için anjiyo, EKG sinyalleri ve kan biyokimyası (kolesterol, lipid) gibi objektif klinik test sonuçlarına ihtiyaç vardır.
IX. KAYNAKLAR
1.	Heart Disease Risk Factors and Patient Health Survey Dataset (dATA.csv). 
2.	Büyük Veri Analizi Proje Uygulama Esasları Kılavuzu. 

