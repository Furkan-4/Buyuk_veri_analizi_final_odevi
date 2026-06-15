BÜYÜK VERİ ANALİZİ FİNAL PROJE RAPORU
Öğrenci Adı Soyadı: [Furkan Yıldız]
Öğrenci Numarası: [22430040010]
GitHub Proje Linki: [https://github.com/Furkan-4/Buyuk_veri_analizi_final_odevi]
Yöntem: Keşifçi Veri Analizi (EDA), İstatistiksel Risk İncelemesi ve Sınıflandırma Modelleri
Tarih: 16.06.2026
I. GİRİŞ
Kardiyovasküler sistem rahatsızlıkları, tıp dünyasında en yüksek ölüm riskine sahip kronik durumlar arasında yer almaktadır. Bu çalışmada, bireylerin yaşam şekilleri, demografik detayları ve klinik geçmiş bilgilerini ihtiva eden dATA.csv veri seti analiz edilmiştir. Analizin temel hedefi, hangi kontrol edilebilir veya edilemez faktörlerin kalp rahatsızlıklarını tetiklediğini bulmak ve makine öğrenmesi metotları ile erken tanı risk puanlaması geliştirmektir. 
II. VERİ SETİNİN TANITIMI
Çalışmada kullanılan dATA.csv veri seti 327 katılımcıya ait 21 farklı niteliği içermektedir. Veri setinde yer alan sütunlar; demografik özellikler (yaş, cinsiyet, medeni durum), günlük alışkanlıklar (fiziksel aktivite, sigara, alkol, beslenme) ve objektif/sübjektif klinik ölçümlerden (boy, kilo, BMI, kan basıncı kategorisi, diyabet durumu) oluşmaktadır. 
III. VERİ ÖN İŞLEME
Analiz öncesinde python programlama dili ile veri temizliği süreçleri yürütülmüştür:
•	Eksik Değer Analizi: Yapılan kontrolde veri setindeki hiçbir hücrede eksik veya tanımsız değer (NaN/Null) olmadığı görülmüştür.
•	Mükerrer Kayıt Analizi: Veri setinde tamamen aynı özellik dizilimine sahip mükerrer (tekrar eden) bir satır bulunmadığı saptanmıştır (df.duplicated().sum() == 0).
•	Özellik Tipi Dönüşümü: Kategorik nitelikteki metinsel veriler, analizlerin ve modellerin çalışabilmesi için LabelEncoder yöntemiyle yapılandırılmış sayısal kategorilere ayrılmıştır.
IV. TANIMLAYICI İSTATİSTİKLER
4.1 Sayısal Değişkenler Betimsel İstatistikleri
•	Height (Boy): Popülasyonun boy ortalaması 163.07 cm'dir. Minimum değer 137.2 cm, maksimum değer ise 182.9 cm olarak hesaplanmıştır.
•	Weight (Kilo): Katılımcıların ortalama ağırlığı 67.18 kg'dır. Standart sapma 11.93 kg olarak bulunmuştur.
•	BMI (Vücut Kitle İndeksi): Ortalama BMI değeri 25.24'tür. En düşük BMI 16.51, en yüksek BMI 42.46'dır. Ortalama değer, popülasyonun genel olarak "hafif kilolu" (overweight) sınıf sınırında yer aldığını kanıtlamaktadır.
4.2 Kategorik Frekans Dağılımları
•	Heart Patient Dağılımı: Veri setinde 108 kişi kalp hastası (Yes), 219 kişi ise sağlıklı bireydir (No). Popülasyondaki kalp hastası oranı %33.03'tür. 
•	Cinsiyet Dağılımı: Veri setinde 196 Erkek (Male) ve 131 Kadın (Female) bulunmaktadır. 
•	En Yaygın Yaş Grubu: 131 kayıt ile "> 50" (50 yaş üstü) grubudur. 
•	En Yaygın Kan Basıncı Kategorisi: 122 kayıt ile "Normal" kan basıncı seviyesidir. 
V. GÖRSELLEŞTİRMELER
 




Proje gereksinimleri uyarınca eksen isimleri ve etiketleri açık olacak şekilde 6 temel grafik python script'i vasıtasıyla diske işlenmiştir:
•	Grafik 1 (Bar Chart): Heart patient hedef değişkeninin genel dağılımını gösterir. Sağlıklı bireylerin çoğunlukta olduğu gözlemlenmektedir. 
•	Grafik 2 (Count Plot): Yaş grupları bazında kalp hastası dağılımını gösterir. 
•	Grafik 3 (Count Plot): Cinsiyet özelinde hastalık durumunu kıyaslar. 
•	Grafik 4 (Boxplot): Kalp hastası olan ve olmayan bireylerin BMI dağılım aralıklarını sergiler. 
•	Grafik 5 (Count Plot): Kan basıncı aşamaları ile kalp hastalığı arasındaki bağı canlandırır. 
•	Grafik 6 (Count Plot): Fiziksel aktivite sıklığının hedef değişkenle kesişimini gösterir. 
(Not: Kodun ürettiği heart_disease_plots.png isimli görseli raporu Word'e aktarırken bu alana ekleyiniz.)
VI. RİSK FAKTÖRÜ ANALİZİ
Veri setindeki temel değişkenler çapraz tablolama (crosstab) yardımıyla derinlemesine incelenmiştir:
1.	Age (Yaş): 35 yaş altındaki bireylerde kalp rahatsızlığı oranı sadece %11.49 iken, 50 yaş üstündeki bireylerde bu oran %51.15'e çıkmaktadır. Yaş değişkeni kalp hastalığı ile doğrudan ilişkilidir ve Grafik 2 bu farkı net bir şekilde desteklemektedir. Bulgular tıp literatüründeki yaşlanma-damar sertliği tezi ile tamamen mantıklıdır. 
2.	Blood Pressure (Kan Basıncı): "Hypertension" (Hipertansiyon) hastası bireylerin %58.14'ünün kalp hastası olduğu görülmektedir. Normal kan basıncına sahip olanlarda bu oran yalnızca %19.67'dir. Hipertansiyonun kalp kasını yorduğu bilinen kronik bir gerçektir, Grafik 5 bunu açıkça doğrular. 
3.	Physical Activity (Fiziksel Aktivite): Haftada 5 veya daha fazla gün spor yaptığını belirten bireylerin %100'ü sağlıklı çıkmış, aralarında hiç kalp hastasına rastlanmamıştır. Fiziksel aktivitenin kardiyovasküler koruyuculuğu kanıtlanmıştır, bulgular mantıklıdır. 
4.	Diabetes (Diyabet): Klinik olarak diyabet teşhisi konmuş kişilerin %41.18'i kalp hastasıdır. Normal şeker seviyesindeki bireylerde bu oran %21.90'a düşmektedir. Diyabetin damar endotel yapısını bozması tıp bilgisiyle birebir örtüşür. 
5.	Gender (Cinsiyet): Kadınların %37.40'ı, erkeklerin %30.10'u kalp hastasıdır. Bu örneklem grubunda kadınların oranı hafif yüksek çıkmıştır. 
VII. MAKİNE ÖĞRENMESİ MODELİ VE MODEL YORUMLAMA
7.1 Model Performans Değerleri
Veri setinin %80'i eğitim, %20'si test seti olarak ayrılmış ve modeller eğitilmiştir:
•	Lojistik Regresyon (Logistic Regression): Accuracy: 0.7727, Precision: 0.8182, Recall: 0.4091, F1-score: 0.5455.
•	Rastgele Orman (Random Forest Classifier): Accuracy: 0.7424, Precision: 0.7273, Recall: 0.3636, F1-score: 0.4848.
7.2 Model Bulgularının Değerlendirilmesi
•	Başarılı Modelin Seçimi: Test setinde tüm metrikler (Accuracy, F1-Score) ele alındığında Lojistik Regresyon modeli %77.27 doğrulukla daha başarılı ve kararlı sonuçlar üretmiştir.
•	Accuracy Metriğinin Sınırları: Sınıflandırma problemlerinde Accuracy tek başına asla yeterli değildir. Veri setindeki sınıflar dengeli olmadığında (%67 sağlıklı, %33 hasta), model hiç kimseye hasta demese bile %67 doğruluk payı yakalar. Bu yüzden tek başına aldatıcıdır. 
•	Recall Metriğinin Önemi: Sağlık ve tıp alanında en hayati metrik Recall'dur. Recall (Duyarlılık), gerçek kalp hastalarının ne kadarının sistem tarafından "doğru teşhis edilebildiğini" gösterir. Kalp hastası birine "sağlıklısın" (False Negative) teşhisi koyup evine göndermek hayati risk taşır. Bu nedenle Recall'un maksimize edilmesi gerekir. 
•	Modelin Yakalama Gücü: Mevcut modellerimizin en zayıf kaldığı yer Recall değerleridir (%40.91 ve %36.36). Modeller gerçek hastaların yarıdan fazlasını kaçırmaktadır ve bu haliyle geliştirilmeye muhtaçtır.
•	Önemli Değişkenler: Katkı payı incelendiğinde modelde en önemli rol oynayan değişkenlerin Yaş (Age), Kan Basıncı (Blood Pressure), Diyabet (Diabetes) ve BMI olduğu saptanmıştır.
VIII. BULGULARIN YORUMLANMASI VE SONUÇ
•	Beklentilerle Uyum: Analiz sonuçlarına göre en ilişkili faktörler beklenen yönde sonuç vermiştir. Yaşlanma, yüksek tansiyon, diyabet ve hareketsizlik beklendiği yönde kalp hastalığı riskini muazzam oranda artırmıştır. 
•	Veri Setinin Güçlü ve Sınırlı Yönleri: Güçlü yönü veri kaybı (eksik değer) içermemesidir. Sınırlı yönü ise sadece 327 satırdan oluşması ve anket/beyan temelli (self-reported) olmasıdır. 
•	İhtiyaç Duyulan Ek Veriler: Daha kararlı bir klinik modelleme için; anjiyo raporları, EKG/Efor test sinyalleri, Troponin değerleri ve tam kan sayımı lipid/kolesterol biyokimya sonuçlarına ihtiyaç duyulmaktadır.
•	Klinik Karar Geçerliliği: Bu veri seti ile gerçek hayatta klinik karar asla verilemez. Veriler hastaların kişisel beyanlarına dayanmaktadır ve hata payı çok yüksektir. Tıbbi teşhis mekanizmaları yanılma payı kabul etmeyen nesnel klinik tetkiklerle yürütülmek zorundadır. 
IX. KAYNAKLAR
1.	Heart Disease Risk Factors and Patient Health Survey Dataset (dATA.csv). 
2.	Büyük Veri Analizi Proje Uygulama Esasları Kılavuzu. 

