# AKTA
## Açık Kaynak Türkçe belge Arşivi (Open Source Turkish Documents Archive)

Bu proje kapsamında, telif sorunu olmayan ve denetlenmiş Türkçe belgeleri derleyeceğiz.
Bu belgelerin, LLM çalışması yapan herkes tarafından özgürce kullanılabilmesi,
Türkçeyi destekleyen çalışmaları yaygınlaştırabilecek ve dil kalitesini arttırabilecektir.

Türkçeye özgü bazı karakterler, PDF formatlı belgelerin düzyazıya çevrilmesi sırasında
sorunlar yaratabiliyor. Bu yüzden ilk aşamada düzyazılara (metin) öncelik vermek yerinde olabilir.

Herhangi bir aşamada, arşivimizde yer alan, ancak telif hakkıyla korunduğunu düşündüğünüz ve projemize açık kullanım izni verilmemiş belgelere rastlarsanız, lütfen bizimle iletişim kurun.

Lütfen projemizi destekleyin.

(Özel işlerim nedeniyle projeyle bir süreliğine ilgilenemeyebilirim.
Lütfen mazur görün.)

## Open Source Turkish Documents Archive

Within the scope of this project, we will compile Turkish documents that are copyright-free and have been audited.

The free use of these documents by everyone doing LLM studies will be able to disseminate studies supporting Turkish and increase the quality of the language.

Some characters specific to Turkish may cause problems when translating PDF formatted documents into prose. Therefore, it may be appropriate to give priority to prose (text) at the first stage.

If at any stage you come across documents in our archive that you think are protected by copyright and that our project has not been granted open use permission, please contact us.

Please support our project.

## Kitap ve Belge Bağışçıları

- Project Gutenberg (36000 İngilizce belge Türkçeye çevrilerek arşive ekleniyor)

## Book and Document Donors

- Project Gutenberg (36,000 English documents are being translated into Turkish and added to the archive)

## Gelişmeler
2025-02-09

metadata.jsonl ve akta_metadata_search.py dosyaları eklendi.
Kütüphane kurulumu: pip install rich unidecode
Kullanım: python akta_metadata_search.py "Charles Dixon" [--field author]

2025-02-03

20000 belgeyi aştık.

2025-01-19

15000 belgeyi aştık.

2025-01-09

12300 belgeyi aştık.

2024-11-25

10000 belgeyi aştık.

2024-11-07

5000 belgeyi aştık.

2024-10-29

Yüklenen belge sayısı  2872 oldu.
Belgeleri kategorilendirmek amacıyla bir model geliştirmek üzere Turkish-Text-Classification projesini başlattık.

2024-10-24

Yüklenen belge sayısı 2000 oldu.

2024-10-18

Yüklenen belge sayısı 1200'e yaklaştı.

2024-10-14

AKTA Projesi için bir logoya ihtiyacımız var. Ancak bunun için bir bedel ödemem mümkün değil. Onun yerine, kendi yazdığım Yeni Başlayanlar İçin Python kitabımı hediye edebilirim:).

2024-10-09

Arşive belge yüklemeye başladım. Belgelerin orijinal "header" ve "footer" bilgilerini korudum. Her belgenin başına, o belgeye ait temel bilgileri Türkçe olarak ekledim.

Belgelerin asıl içeriğini, deep_translator/GoogleTranslator kütüphanesi aracılığıyla İngilizceden Türkçeye çevirdim. Çevrilen metni, orijinal metnin olduğu yere kopyaladım.'
Çevirinin başladığı yere \*\*\* START OF TURKISH PART \*\*\*, bittiği yere de \*\*\* END OF TURKISH PART \*\*\* ekledim. Böylece kod yardımı ile sadece Türkçeleştirilmiş metni kolayca çekmek mümkün. Bu amaçla aktalib.py dosyasında yer alan  extract_turkish_body(text) fonksiyonunu kullanmak mümkün.

Kodlarda genellikle İngilizce terimler kullanmaya çalıştım. Böylelikle, Türkçe bilmeyenlerin de kullandığım yapıyı daha kolay anlamaları mümkün olabilir diye düşünüyorum.

Yüklediğim belgelerde gözden geçirme işlemleri şimdilik çok azdır. Sorunlu yerlere rastladığınızda durumu bildirirseniz, gerekli düzeltmeleri hızlıca yapmak mümkün olabilir.

Gözden geçirme işlemlerini öncelikle -varsa- kelime hatalarını bulma şeklinde, daha sonra da yapay zeka araçları kullanarak anlamsal ve yapısal kontrollerini yaptırmayı planlıyorum.

Bu konuya ilişkin tüm önerilere açığım.
 

2024-10-06

Project Gutenberg'in izniyle yaklaşık 36 000 belgeyi Türkçeye çevirip, AKTA projesine ekleyebileceğiz. 

Bu dosyaların toplam boyutu  yaklaşık 15 Gbyte tutacak gibi görünüyor. Asıl boyut, çeviriler tamamlandıktan sonra belli olacak.  Eğer dosyaları zipleyerek saklarsak, depolama alanı üçte birine düşebilir.

Yine de, projenin tamamiyle github üzerinden sürdürülmesi pek olası değil. 

O yüzden en kısa zamanda, daha geniş bir depolama alanına geçmemiz gerekiyor.

Dosyaları indirmek ve Türkçeye çevirmek için gereken betikleri hazırladım. 

Kaynak sistemlere aşırı yüklenmemek için, özellikle indirme işlemlerini aralıklarla yapmaya çalışıyorum. 

Çeviriler, deep_translate kütüphanesiyle GoogleTranslate tarafından gerçekleştirilecek. Bu işlemler de aralıklı olarak yapılmak zorunda.

Gelişmeleri buradan duyurmaya devam edeceğim.


## Yapılacaklar Listesi

- Telif süresi dolan yazarlara ait eserlerin derlenmesi ve günümüz Türkçesine çevrilmesi için kod yazılması

- AKTA arşivine mükerrer belge eklenmesini engelleyecek denetim kodlarının yazılması

- Arşivin tanıtımına katkıda bulunacak ve kullanımını kolaylaştıracak örnek kodların üretilmesi

- Belge bağışında bulunabilecek kişi ve kuruluşlarla iletişime geçilmesi

- Arşivin içeriğinin sürekli analiz edilmesi ve elde edilen sonuçların paylaşılması

- Projeye katkıda bulunabilecek kişi ve kuruluşlarla iletişime geçilmesi

- Projenin sürdürülebilirliğini güvence altına alacak önlemlerin geliştirilmesi

- Projenin sosyal medyada tanıtılması

- Soru-cevap veriseti oluşturulması (Ön çalışmalara başlandı)

- Gutenberg.org gibi açık kaynak belge paylaşan kurumlara izin başvurusu yapılması (İzin alındı)
 

## Developments

2025-02-09

metadata.jsonl and akta_metadata_search.py dosyaları added
Library installation: pip install rich unidecode
Usage: python akta_metadata_search.py "Charles Dixon" [--field author]

2025-02-03

We have exceeded 20000 documents.

2025-01-19

We have exceeded 15000 documents.

2025-01-09

We have exceeded 12300 documents.

2024-11-25

We have exceeded 10000 documents.

2024-11-07

We have exceeded 5000 documents.

2024-10-29

The number of uploaded documents is 2872. 
We started the Turkish-Text-Classification project to develop a model to categorize documents.

2024-10-24

The number of uploaded documents approached 2000.

2024-10-18

The number of uploaded documents approached 1200.

2024-10-09

I started uploading documents to the archive. I preserved the original "header" and "footer" information of the documents. I added the basic information about that document in Turkish at the beginning of each document.

I translated the original content of the documents from English to Turkish using the deep_translator/GoogleTranslator library. I copied the translated text to where the original text was.

I added \*\*\* START OF TURKISH PART \*\*\* to where the translation started and \*\*\* END OF TURKISH PART \*\*\* to where it ended. Thus, it is possible to easily extract only the Turkishized text with the help of code. For this purpose, it is possible to use the extract_turkish_body(text) function in the aktalib.py file.

I generally tried to use English terms in the codes. In this way, I think that it will be easier for those who do not know Turkish to understand the structure I use.

There are very few review processes in the documents I upload for now. If you report the situation when you come across problematic areas, it will be possible to make the necessary corrections quickly.

I plan to review the text first by finding word errors -if any- and then by using artificial intelligence tools to perform semantic and structural checks.

I am open to all suggestions on this subject.

2024-10-06

With the permission of Project Gutenberg, we will be able to translate approximately 36,000 documents into Turkish and add them to the AKTA project.

The total size of these files is expected to be around 15 Gbytes. The actual size will be determined after the translations are completed. If we store the files in zip format, the storage space can be reduced by a third.

However, it is unlikely that the project will be maintained entirely on github.

Therefore, we need to move to a larger storage space as soon as possible.

I have prepared the scripts needed to download the files and translate them into Turkish.

In order not to overload the source systems, I am trying to perform the downloads at intervals.

The translations will be performed by GoogleTranslate with the deep_translate library. These operations will also have to be done at intervals.

I will continue to announce the developments here.

## Todo List

- Writing code to compile works by authors whose copyrights have expired and translate them into modern Turkish

- Writing control codes that will prevent duplicate documents from being added to the AKTA archive

- Producing sample codes that will contribute to the promotion of the archive and facilitate its use

- Contacting individuals and organizations that can donate documents

- Continuously analyzing the content of the archive and sharing the results obtained

- Contacting individuals and organizations that can contribute to the project

- Developing measures to ensure the sustainability of the project

- Promoting the project on social media

- Creating a question-answer dataset (Preliminary work has begun)

- Applying for permission to institutions that share open source documents, such as Gutenberg.org (Permission received)


