# Türkçe Python

Bu projede Python kodları belirli Türkçe anahtar kelime ve fonksiyon isimleriyle yazılabilir ve geliştirilme aşamasındadır. Kod arka planda Python diline çevrilir ve standart Python yorumlayıcısı ile çalıştırılır.


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

## Modüller
Proje ile birlikte bazı Türkçe modüller de kullanılabilir:
- matematik.trpy (kare alınabilir, toplanabilir, çarpılabilir vb.)
- dize.trpy (büyük/küçük harfe dönüştürülebilir, ters çevrilebilir)
- dosya.trpy (dosya okunabilir, yazılabilir)
- rastgele.trpy (rastgele sayı veya seçim yapılabilir)
- yardımcı.trpy (renkli yazı yazılabilir, bekletilebilir, saat alınabilir)

Herhangi bir modül projeye eklenerek aşağıdaki gibi kullanılabilir:
```
içe_aktar matematik
yaz(matematik.kare(8))
```

## Yardım ve Bilgi
```bash
python turkcepython.py yardım
python turkcepython.py --sürüm
```
