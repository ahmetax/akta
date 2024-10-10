# AKTA
## Açık Kaynak Türkçe belge Arşivi (Open Source Turkish Documents Archive)

Bu proje kapsamında, telif sorunu olmayan ve denetlenmiş Türkçe belgeleri derleyeceğiz.
Bu belgelerin, LLM çalışması yapan herkes tarafından özgürce kullanılabilmesi,
Türkçeyi destekleyen çalışmaları yaygınlaştırabilecek ve dil kalitesini arttırabilecektir.

Türkçeye özgü bazı karakterler, PDF formatlı belgelerin düzyazıya çevrilmesi sırasında
sorunlar yaratabiliyor. Bu yüzden ilk aşamada düzyazılara (metin) öncelik vermek yerinde olabilir.

Herhangi bir aşamada, arşivimizde yer alan, ancak telif hakkıyla korunduğunu düşündüğünüz ve projemize açık kullanım izni verilmemiş belgelere rastlarsanız, lütfen bizimle iletişim kurun.

Lütfen projemizi destekleyin.

## Open Source Turkish Documents Archive

Within the scope of this project, we will compile Turkish documents that are copyright-free and have been audited.

The free use of these documents by everyone doing LLM studies will be able to disseminate studies supporting Turkish and increase the quality of the language.

Some characters specific to Turkish may cause problems when translating PDF formatted documents into prose. Therefore, it may be appropriate to give priority to prose (text) at the first stage.

If at any stage you come across documents in our archive that you think are protected by copyright and that our project has not been granted open use permission, please contact us.

Please support our project.


## Gelişmeler
2024-10-09

Arşive belge yüklemeye başladım. Belgelerin orijinal "header" ve "footer" bilgilerini korudum. Her belgenin başına, o belgeye ait temel bilgileri Türkçe olarak ekledim.

Belgelerin asıl içeriğini, deep_translator/GoogleTranslator kütüphanesi aracılığıyla İngilizceden Türkçeye çevirdim. Çevrilen metni, orijinal metnin olduğu yere kopyaladım.'
Çevirinin başladığı yere <code>'***</code> START OF TURKISH PART <code>***'</code>, bittiği yere de <code>'***</code> END OF TURKISH PART <code>***'</code> ekledim. Böylece kod yardımı ile sadece Türkçeleştirilmiş metni kolayca çekmek mümkün. Bu amaçla aktalib.py dosyasında yer alan  extract_turkish_body(text) fonksiyonunu kullanmak mümkün.

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


## Developments
2024-10-09

I started uploading documents to the archive. I preserved the original "header" and "footer" information of the documents. I added the basic information about that document in Turkish at the beginning of each document.

I translated the original content of the documents from English to Turkish using the deep_translator/GoogleTranslator library. I copied the translated text to where the original text was.

I added <code>'***</code> START OF TURKISH PART <code>***'</code> to where the translation started and <code>'***</code> END OF TURKISH PART <code>***'</code> to where it ended. Thus, it is possible to easily extract only the Turkishized text with the help of code. For this purpose, it is possible to use the extract_turkish_body(text) function in the aktalib.py file.

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


