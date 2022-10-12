danısman=0
konut_sat=0
konut_kira=0
isyeri_sat=0
isyeri_kira=0
arsa_sat=0
arsa_kira=0
adet_para=0 #en az 10 adet veya en az 25000 TL tutarında emlak kiralayan danışmanların sayısı
kota_dan=0 #kotasını dolduran danisman sayisi
satis_yok=0 #hic satis yapamayan danisman sayisi
prim_dan=0 #primi maasindan yuksek olan danisman sayisi
kira_yuksek=0 #kira bedeli asgari ucretten yuksek olan konut sayısı
konut_sat_bedel=0 #emlak tipi konut olup satilan ev bedeli
isyeri_sat_bedel=0 #emlak tipi isyeri olup satilan ev bedeli
arsa_sat_bedel=0 #emlak tipi arsa olup satilan ev bedeli
max_sat_bedel_tip='' #en yüksek bedelle satılan emlağın tipi
max_sat_bedel=0 #en yüksek bedel satılan emlagın bedeli
max_sat_bedel_ad='' #en yüksek bedelle satış yapan emlağın ismi
max_kira_konut=0 #en yüksek bedelle kiralanan konutun kira bedeli
max_kira_konut_ad='' #en yüksek bedelle kiralanan konutu kiralayan danışmanın ismi

dan_say=int(input("Acenteye bağlı olarak çalışan emlak danışmanı sayısı: "))
while dan_say<=0:
    dan_say = int(input("Hatalı girdiniz, tekrar giriniz: "))

while danısman<dan_say:
    emlak_tip1=0 #emlak tipi konut olan
    emlak_tip2=0
    emlak_tip3=0
    islem_turu1=0
    islem_turu2=0
    max_kira_bedel=0
    ASGARI_UC = 2324.70
    IKRAMIYE = ASGARI_UC / 2

    devam=True

    danısman+=1 #emlak danismani sayisini hesapliyorum
    ad_soy = input("Emlak danışmanının adını ve soyadını giriniz: ")

    maas=int(input("Aldığınız maaşı giriniz: "))
    while maas<ASGARI_UC:
        maas=int(input("Hatalı girdiniz, tekrar giriniz: "))

    kota=int(input("Kotayı giriniz: "))
    while kota<10*maas:
        kota=int(input("Hatalı girdiniz, tekrar giriniz: "))
    while devam:

        emlak_tip = input("Emlak tipini giriniz(Konut,İş yeri,Arsa(K/k/İ/i/A/a karakterleri)): ")
        while emlak_tip != 'K' and emlak_tip != 'k' and emlak_tip != 'İ' and emlak_tip != 'i' and emlak_tip != 'A' and emlak_tip != 'a':
            emlak_tip = input("Hatalı girdiniz, tekrar giriniz: ")

            islem_turu = input("İşlem türünü giriniz(Satış,Kiralama(S/s/K/k karakterleri)): ")
            while islem_turu != 'S' and islem_turu != 's' and islem_turu != 'K' and islem_turu != 'k':
                islem_turu = input("Hatalı girdiniz, tekrar giriniz: ")

            if emlak_tip == 'K' or emlak_tip == 'k':
                emlak_tip1 += 1  # emlak tipi konut olan emlak sayısı
                if islem_turu=='S' or islem_turu=='s': #emlak tipi konut olup satılan evler
                    konut_sat +=1
                    konut_sat_bedel += satis_bedel #emlak tipi konut olup satılan ev bedeli
                else:
                    konut_kira+=1 # emlak tipi konut olup kiralanan evler

                    if kira_bedel==max_kira_konut: #en yüksek bedelle kiralanan konutun kira bedeli
                        kira_bedel = max_kira_konut
                        max_kira_konut_ad = ad_soy #en yüksek bedelle kiralanan konutu kiralayan danışmanın adı soyadı

                    if kira_bedel > ASGARI_UC:
                        kira_yuksek += 1  # kira bedeli asgari ucretten yuksek olan konut sayısı

            elif emlak_tip == 'İ' or emlak_tip == 'i':
                emlak_tip2 += 1  # emlak tipi işyeri olan emlak sayısı
                if islem_turu=='S' or islem_turu=='s': #emlak tipi işyeri olup satılan evler
                    isyeri_sat +=1
                    isyeri_sat_bedel += satis_bedel #emlak tipi isyeri olup satılan ev bedeli
                else:
                    isyeri_kira +=1 #emlak tipi isyeri olup kiralan evler

            elif emlak_tip == 'A' or emlak_tip == 'a':
                emlak_tip3 += 1  # emlak tipi arsa olan emlak sayısı
                if islem_turu == 'S' or islem_turu == 's':  # emlak tipi arsa olup satılan evler
                    arsa_sat +=1
                    arsa_sat_bedel += satis_bedel #emlak tipi arsa olup satılan ev bedeli
                else:
                    arsa_kira +=1 #emlak tipi arsa olup kiralanan evler

        if islem_turu == 'S' or islem_turu == 's':
            islem_turu1 += 1  # işlem türü satış olan emlak sayısı

            oran1 = islem_turu1 / (islem_turu1 + islem_turu2) * 100  # o ay sattıgı emlak oranı
            oran2 = islem_turu2 / (islem_turu1 + islem_turu2) * 100  # o ay kiraladıgı emlak oranı

            satis_bedel = int(input("Satış bedelini girin: "))

            while satis_bedel <= 0:
                satis_bedel = int(input("Hatalı girdiniz, tekrar giriniz: "))
                emlak_kom1 = satis_bedel * 4 / 100  # satış için alınan emlak komisyonu

                if satis_bedel==max_sat_bedel:
                    satis_bedel = max_sat_bedel #en yüksek bedelle satılan emlagın satıs bedeli
                    max_sat_bedel_tip = emlak_tip #en yüksek bedelle satılan emlagın tipi
                    max_sat_bedel_ad = ad_soy #en yüksek bedelle satılan emlagı satan danismanin adı soyadı

        elif islem_turu == 'K' or islem_turu == 'k':
            islem_turu2 += 1  # işlem türü kiralama olan emlak sayısı
            oran1 = islem_turu1 / (islem_turu1 + islem_turu2) * 100  # o ay sattıgı emlak oranı #sonradan adım bunları buraya
            oran2 = islem_turu2 / (islem_turu1 + islem_turu2) * 100  # o ay kiraladıgı emlak oranı


            kira_bedel = int(input("Kira bedelini girin: "))
            while kira_bedel <= 0:
                kira_bedel = int(input("Hatalı girdiniz, tekrar giriniz: "))

            if islem_turu2>=10 or kira_bedel>=2500:
                adet_para+=1 #en az 10 adet veya en az 25000 TL tutarında emlak kiralayan danışmanların sayısı

            emlak_kom2 = kira_bedel  # kiralama için alınan emlak komisyonu
            ort_kira_bedel = kira_bedel / islem_turu2  # o ay kiraladığı konutların ortalama kira bedeli
            emlak_kom = (satis_bedel * 4 / 100) + kira_bedel  # toplam emlak komisyonu
            prim = emlak_kom * 10 / 100
            top_ücret = maas + prim + IKRAMIYE  # yerleri yanlış olabilir üsttekiyle

            if prim>maas:
                prim_dan += 1 #primi maasindan yuksek olan danisman sayisi

            if kira_bedel >= max_kira_bedel:
                max_kira_bedel = kira_bedel  # hata olabilir max kira bedelini bulmaya calistim

        emlak = input("O ay sattığı/kiraladığı başka var mı?(E/e/H/h): ")
        while emlak != 'E' and emlak != 'e' and emlak != 'H' and emlak != 'h':
            emlak = input("Hatalı girdiniz, tekrar giriniz: ")  # if emlak e ise ne olcak onu yazmayı unutma bulamadın mal

        if emlak=='H' or emlak=='h':
            satis_yok +=1 #hic satis yapamayan danisman sayısı #yeri yanlis olabilir bak buraya hop
            devam=False


    print("Adı soyadı:", ad_soy)
    print("O ay sattığı emlak adedi:", islem_turu1)
    print("O ay kiraladığı emlak adedi:", islem_turu2)
    print("O ay kiraladığı emlak oranı:", oran1)
    print("O ay satılan emlak oranı:", oran2)
    print("O ay kiraladığı konutların ortalama kira bedeli:", ort_kira_bedel)
    print("o ay en yüksek bedelle kiraladığı konutun kira bedeli (TL):", max_kira_bedel)
    print("O ay maaşı:", maas)
    print("O ay primi: ",prim)
    print("O ay kotası:", kota)
    print("O ay acenteye kazandırdığı toplam komisyon tutarı(TL)", emlak_kom)

    if emlak_kom>=kota:
        kota='Kota dolduruldu' #kotanın doldurup doldurulmadığı printlemeye çalıştım olmamış olabilir
        print(kota)
        print("Aldığı ikramiye:", IKRAMIYE)

        if kota=='Kota dolduruldu':
            kota_dan += 1 #kotasını dolduran danisman sayisi
    else:
        kota='Kota doldurulmadı'
        print(kota)

    print("O ay toplam ücreti (TL):", top_ücret)

    sat_oran1=konut_sat/(konut_sat+konut_kira)*100 #emlak tipi konut olanların satılma oranı
    sat_oran2=isyeri_sat/(isyeri_sat+isyeri_kira)*100 #emlak tipi isyeri olanların satılma oranı
    sat_oran3= arsa_sat/(arsa_sat+arsa_kira)*100 #emlak tipi arsa olanların satılma oranı

    kota_dan_oran=(kota_dan/danısman)*100 #o ay kotasını dolduran danışmanların tüm danışmanlar içindeki oranı
    satis_yok_oran=(satis_yok/danısman)*100 #hiç satış yapmayan danışmanların tüm danışmanlar içindeki oranı
    prim_dan_oran=(prim_dan/danısman)*100 #primi maaşından yüksek olan danışmanların tüm danışmanlar içindeki oranı
    kira_asg_oran=(kira_yuksek/konut_kira)*100 #kiralanan konutlardan kira bedeli, aylık asgari net ücretten yüksek olan konutların kiralanan konutlar icindeki oranı

    satis_bedel_top=konut_sat_bedel+isyeri_sat_bedel+arsa_sat_bedel
    satis_bedel_ort1=konut_sat_bedel/konut_sat #emlak tipi konut olup satılan evlerin satış bedeli ortalaması
    satis_bedel_ort2=isyeri_sat_bedel/isyeri_sat #emlak tipi isyeri olup satılan evlerin satış bedeli ortalaması
    satis_bedel_ort3=arsa_sat_bedel/arsa_sat #emlak tipi arsa olup satılan evlerin satış bedeli ortalaması

    print("Emlak tipi konut olup satılan emlak sayısı: ", konut_sat)
    print("Emlak tipi konut olup kiralanan emlak sayısı: ", konut_kira)
    print("Emlak tipi konut olup satılma oranı: ", sat_oran1)

    print("Emlak tipi işyeri olup satılan emlak sayısı: ", isyeri_sat)
    print("Emlak tipi işyeri olup kiralanan emlak sayısı: ", isyeri_kira)
    print("Emlak tipi işyeri olup satılma oranı: ", sat_oran2)

    print("Emlak tipi arsa olup satılan emlak sayısı: ", arsa_sat)
    print("Emlak tipi arsa olup kiralanan emlak sayısı: ", arsa_kira)
    print("Emlak tipi arsa olup satılma oranı: ", sat_oran3)

    print("Emlak tipi konut olup satılan konutların satış bedeli toplamı: ", konut_sat_bedel)
    print("Emlak tipi konut olup satılan konutların satış bedeli ortalaması: ", satis_bedel_ort1)

    print("Emlak tipi işyeri olup satılan işyerlerinin satış bedeli toplamı: ", isyeri_sat_bedel)
    print("Emlak tipi işyeri olup satılan işyerlerinin satış bedeli ortalaması: ", satis_bedel_ort2)

    print("Emlak tipi arsa olup satılan arsaların satış bedeli toplamı: ", arsa_sat_bedel)
    print("Emlak tipi arsa olup satılan arsaların satış bedeli ortalaması: ", satis_bedel_ort3)

    print("O ay en yüksek bedelle satılan emlağın tipi: ", max_sat_bedel_tip)
    print("O ay en yükse bedelle satılan emlağın bedeli: ", max_sat_bedel)
    print("O ay en yüksek bedelle satılan emlağı satan danışmanın adı soyadı: ", max_sat_bedel_ad)

    print("o ay en yüksek bedelle kiralanan konutun kira bedeli (TL): ", max_kira_konut)
    print("O ay en yüksek bedelle kiralanan konutu kiralayan danışmanın adı soyadı: ", max_kira_konut_ad)

    print("o ay kiralanan konutlardan kira bedeli, aylık asgari net ücretten yüksek olan konutların sayısı: ", kira_yuksek)
    print("o ay kiralanan konutlardan kira bedeli, aylık asgari net ücretten yüksek olan konutların kiralanan konutlar icindeki oranı: ",kira_asg_oran)

    print("o ay hiç satış yapamayan danışmanların sayısı: ", satis_yok)
    print("O ay hiç satış yapmayan danışmanların tüm danışmanlar içindeki oranı: ",satis_yok_oran)




    print("O ay kotasını dolduran danışmanların sayısı: ",kota_dan)
    print("O ay kotasını dolduran danışmanların tüm danışmanlar içindeki oranı: ", kota_dan_oran)

    print("o ay primi maaşından yüksek olan danışmanların sayısı: ",prim_dan)
    print("O ay primi maaşından yüksek olan danışmanların tüm danışmanlar içindeki oranı: ", prim_dan_oran)

    print("o ay en az 10 adet veya en az 25000 TL tutarında emlak kiralayan danışmanların sayısı:", adet_para)







