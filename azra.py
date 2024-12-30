# Öğrenci Bilgi Sistemi ve Not Analizi

# Öğrenci bilgilerini saklamak için boş bir liste
ogrenci_listesi = []

def ogrenci_ekle():
    isim = input("Öğrencinin adı: ")
    soyisim = input("Öğrencinin soyadı: ")
    numara = input("Öğrenci numarası: ")
    not1 = float(input("1. Notu girin: "))
    not2 = float(input("2. Notu girin: "))
    ortalama = (not1 + not2) / 2
    durum = "Geçti" if ortalama >= 50 else "Kaldı"
    ogrenci = {
        "isim": isim,
        "soyisim": soyisim,
        "numara": numara,
        "not1": not1,
        "not2": not2,
        "ortalama": ortalama,
        "durum": durum
    }
    ogrenci_listesi.append(ogrenci)
    print(f"{isim} {soyisim} başarıyla sisteme eklendi!")

def ogrencileri_listele():
    if not ogrenci_listesi:
        print("Sistemde kayıtlı öğrenci yok.")
    else:
        print("\nKayıtlı Öğrenciler ve Notlar:")
        for i, ogrenci in enumerate(ogrenci_listesi, start=1):
            print(f"{i}. {ogrenci['isim']} {ogrenci['soyisim']} - "
                  f"Numara: {ogrenci['numara']} - Notlar: {ogrenci['not1']}, {ogrenci['not2']} - "
                  f"Ortalama: {ogrenci['ortalama']:.2f} - Durum: {ogrenci['durum']}")

def not_analizi():
    if not ogrenci_listesi:
        print("Sistemde kayıtlı öğrenci yok.")
    else:
        ortalamalar = [ogrenci["ortalama"] for ogrenci in ogrenci_listesi]
        genel_ortalama = sum(ortalamalar) / len(ortalamalar)
        gecenler = [ogrenci for ogrenci in ogrenci_listesi if ogrenci["durum"] == "Geçti"]
        kalanlar = [ogrenci for ogrenci in ogrenci_listesi if ogrenci["durum"] == "Kaldı"]
        
        print("\nNot Analizi:")
        print(f"Genel Ortalama: {genel_ortalama:.2f}")
        print(f"Geçen Öğrenci Sayısı: {len(gecenler)}")
        print(f"Kalan Öğrenci Sayısı: {len(kalanlar)}")

# Ana Menü
while True:
    print("\nÖğrenci Bilgi Sistemi ve Not Analizi")
    print("1. Öğrenci Ekle")
    print("2. Öğrencileri Listele")
    print("3. Not Analizi")
    print("4. Çıkış")
    secim = input("Seçiminizi yapın (1-4): ")

    if secim == "1":
        ogrenci_ekle()
    elif secim == "2":
        ogrencileri_listele()
    elif secim == "3":
        not_analizi()
    elif secim == "4":
        print("Sistemden çıkış yapılıyor. Hoşça kal!")
        break
    else:
        print("Geçersiz seçim yaptınız, lütfen tekrar deneyin.")
