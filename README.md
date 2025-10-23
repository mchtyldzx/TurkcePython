# Türkçe Python

Bu projede Python kodları belirli Türkçe anahtar kelime ve fonksiyon isimleriyle yazılabilir ve geliştirilme aşamasındadır. Kod arka planda Python diline çevrilir ve standart Python yorumlayıcısı ile çalıştırılır.

## Nasıl Kullanılır

1. Türkçe yazılmış bir `.trpy` dosyası hazırlanabilir.
2. Aşağıdaki komutla çalıştırılabilir:

```bash
python turkcepython.py dosyan.trpy
```

Örneğin:
```bash
python turkcepython.py modultesti.trpy
```

## Kısa Kod Örneği

```
ata x 10
eğer x > 5 ise:
    yaz("x büyük 5'ten")
değilse:
    yaz("x küçük veya eşit 5")
```
Bu dosya yukarıdaki gibi çalıştırılabilir.

## Türkçe Anahtar Kelimeler

**Kontrol Yapıları:**
- `eğer ... ise:` → if
- `değilse:` → else
- `yoksa_eğer ... ise:` → elif
- `tekrar ... kadar:` → for döngüsü
- `döndür ... ise:` → while döngüsü
- `kır` → break
- `geç` → continue
- `geçer` → pass

**Değerler:**
- `doğru` → True
- `yanlış` → False
- `boş` → None

**Operatörler:**
- `eşittir` → ==
- `eşit_değil` → !=
- `büyüktür` → >
- `büyük_eşit` → >=
- `küçüktür` → <
- `küçük_eşit` → <=
- `ve` → and
- `veya` → or
- `değil` → not
- `kalan` → %

**Diğer:**
- `tanımla` → def (fonksiyon)
- `geri_dön` → return
- `sınıf` → class
- `yaz()` → print()
- `içe_aktar` → import
- `içinde` → in

## Örnekler

### While Döngüsü
```python
sayac = 1
döndür sayac küçüktür 10 ise:
    yaz(sayac)
    sayac = sayac + 1
```

### Break ve Continue
```python
tekrar i 1'den 10'e kadar:
    eğer i eşittir 5 ise:
        kır
    yaz(i)
```

### Liste Döngüsü
```python
meyveler = ["elma", "armut", "muz"]
tekrar meyve meyveler içinde:
    yaz(meyve)
```

### Karşılaştırma
```python
eğer puan büyük_eşit 50 ve puan küçük_eşit 100 ise:
    yaz("Geçti")

sonuc = sayi kalan 2
eğer sonuc eşittir 0 ise:
    yaz("Çift sayı")
```

## Modüller

Proje ile birlikte bazı Türkçe modüller de kullanılabilir:
- **matematik.trpy** (kare alınabilir, toplanabilir, çarpılabilir vb.)
- **dize.trpy** (büyük/küçük harfe dönüştürülebilir, ters çevrilebilir)
- **dosya.trpy** (dosya okunabilir, yazılabilir)
- **rastgele.trpy** (rastgele sayı veya seçim yapılabilir)
- **yardımcı.trpy** (renkli yazı yazılabilir, bekletilebilir, saat alınabilir)
- **modultesti.trpy** (projeyle birlikte gelen test dosyası)


Herhangi bir modül projeye eklenerek aşağıdaki gibi kullanılabilir:
```python
içe_aktar matematik
yaz(matematik.kare(8))

içe_aktar dize
metin = "merhaba"
yaz(dize.büyüt(metin))  # MERHABA
```

## Yardım

```bash
python turkcepython.py yardım
python turkcepython.py --sürüm
```

## Test

Projeyle birlikte gelen test dosyası çalıştırılabilir:
```bash
python turkcepython.py modultesti.trpy
```
