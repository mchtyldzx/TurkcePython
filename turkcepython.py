# -*- coding: utf-8 -*-
# Türkçe Python
# Özellikler: Modül desteği, renkli hata mesajları, yardım & sürüm komutları, içe_aktar sistemi

import sys
import re
import traceback
import importlib.util
import os
from colorama import init, Fore, Style

init(autoreset=True)

SURUM = "1.1"

SOZLUK = {
    "tanımla ": "def ",
    "eğer ": "if ",
    "yoksa_eğer": "elif",
    "değilse": "else",
    "tekrar ": "for ",
    "döndür ": "while ",
    "arasında": "in range",
    "içinde": "in",
    "geri_dön": "return",
    "kır": "break",
    "geç": "continue",
    "geçer": "pass",
    "sınıf ": "class ",
    "deneme": "try",
    "hata": "except",
    "doğru": "True",
    "yanlış": "False",
    "boş": "None",
    # Operatörler - Sıralama önemli (uzun olanlar önce)
    "eşit_değil": "!=",
    "büyük_eşit": ">=",
    "küçük_eşit": "<=",
    "eşittir": "==",
    "büyüktür": ">",
    "küçüktür": "<",
    " kalan ": " % ",
    # Boolean operatörler - Kelime sınırları ile
    " ve ": " and ",
    " veya ": " or ",
    "değil ": "not ",
    " yaz(": " print(",
    "içe_aktar ": "import ",
    "doğru": "True",
    "yanlış": "False",
    "sor": "input",
    "hiçbiri": "None",
}

KALIPLAR = [
    (r"eğer (.*?) ise:", r"if (\1):"),
    (r"yoksa_eğer (.*?) ise:", r"elif (\1):"),
    (r"döndür (.*?) ise:", r"while (\1):"),
    (r"tekrar (\w+) (\d+)['']?den (\d+)['']?e kadar:", r"for \1 in range(\2, \3):"),
    (r"tekrar (\w+) (.*?) içinde:", r"for \1 in \2:"),
    (r"ata (\w+) = (.*)", r"\1 = \2"),
]

def hata_mesaji_cevir(e):
    if isinstance(e, SyntaxError):
        return Fore.RED + "Yazım hatası: Kodun sözdiziminde bir sorun var." + Style.RESET_ALL
    elif isinstance(e, NameError):
        return Fore.RED + "Tanımlama hatası: Tanımlanmamış bir değişken veya isim kullanıldı." + Style.RESET_ALL
    elif isinstance(e, TypeError):
        return Fore.YELLOW + "Tür hatası: Uyumlu olmayan türler arasında işlem yapıldı." + Style.RESET_ALL
    elif isinstance(e, ZeroDivisionError):
        return Fore.YELLOW + "Hata: Bir sayı sıfıra bölünemez." + Style.RESET_ALL
    elif isinstance(e, FileNotFoundError):
        return Fore.YELLOW + "Dosya bulunamadı: içe_aktar edilen modül eksik olabilir." + Style.RESET_ALL
    elif isinstance(e, ModuleNotFoundError):
        return Fore.YELLOW + "Modül bulunamadı: içe_aktar edilen .trpy dosyası yok." + Style.RESET_ALL
    else:
        return Fore.RED + f"Hata: {e}" + Style.RESET_ALL

def turkce_to_python(kod: str) -> str:
    # // yorumları kaldır
    kod = re.sub(r"//.*", "", kod)

    # Kelime bazlı çeviri (string içini bozmaz)
    for tr, en in SOZLUK.items():
        tr_esc = re.escape(tr.strip())
        kod = re.sub(rf"\b{tr_esc}\b", en.strip(), kod)

    # yaz( → print(
    kod = re.sub(r"\byaz\s*\(", "print(", kod)

    # arttır / azalt
    kod = re.sub(r"(\w+)\s+arttır\s+(\d+)", r"\1 += \2", kod)
    kod = re.sub(r"(\w+)\s+azalt\s+(\d+)", r"\1 -= \2", kod)

    return kod


# Türkçe modül yükleyici (içe_aktar satırlarını da çeviriyor)
def yukle_modul(modul_adi):
    dosya = modul_adi + ".trpy"
    if not os.path.exists(dosya):
        raise FileNotFoundError(f"{dosya} bulunamadı.")
    with open(dosya, "r", encoding="utf-8") as f:
        kod = f.read()

    kod = turkce_to_python(kod)  # Çeviri eklendi
    py_dosya = modul_adi + "_temp.py"
    with open(py_dosya, "w", encoding="utf-8") as f:
        f.write(kod)

    spec = importlib.util.spec_from_file_location(modul_adi, py_dosya)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    os.remove(py_dosya)
    return modul

def isle_içe_aktar(kod: str, ortam):
    moduller = re.findall(r"içe_aktar (\w+)", kod)
    yuklu = {}
    for m in moduller:
        try:
            yuklu[m] = yukle_modul(m)
            print(Fore.GREEN + f"# içe_aktar {m} (yüklendi)" + Style.RESET_ALL)
        except Exception as e:
            print(hata_mesaji_cevir(e))
    return yuklu

YARDIM_METNI = f"""
{Fore.CYAN}Türkçe Python Yardım (v{SURUM}){Style.RESET_ALL}
---------------------------------------
ata x 5                      → Değişken tanımlar
yaz("Merhaba")               → Ekrana metin yazar
eğer x > 3 ise:              → Koşul başlatır
değilse:                     → Alternatif koşul
tekrar i 1'den 5'e kadar:    → Döngü başlatır (for)
döndür x < 10 ise:           → While döngüsü
kır                          → Döngüden çık (break)
geç                          → Sonraki adıma geç (continue)
tekrar x liste içinde:       → Liste/dizi üzerinde döngü

Operatörler:
  eşittir (==), eşit_değil (!=)
  büyüktür (>), büyük_eşit (>=)
  küçüktür (<), küçük_eşit (<=)
  kalan (%)
  ve (and), veya (or), değil (not)

içe_aktar matematik          → Modül ekler (.trpy dosyası)
yardım                       → Bu ekranı gösterir
--sürüm                      → Sürüm bilgisini gösterir
"""

def main():
    # Windows için UTF-8 encoding
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')
    
    print(Fore.CYAN + f"Türkçe Python v{SURUM}" + Style.RESET_ALL)
    if len(sys.argv) < 2:
        print(Fore.YELLOW + "Kullanım: trpython dosya.trpy" + Style.RESET_ALL)
        sys.exit(1)

    arg = sys.argv[1]
    if arg in ("yardım", "--yardım", "-h"):
        print(YARDIM_METNI)
        sys.exit(0)
    if arg in ("--sürüm", "-v"):
        print(Fore.GREEN + f"Sürüm: v{SURUM}" + Style.RESET_ALL)
        sys.exit(0)

    dosya = arg
    with open(dosya, "r", encoding="utf-8") as f:
        kod = f.read()

    yuklu_moduller = isle_içe_aktar(kod, globals())
    temiz_kod = re.sub(r"^içe_aktar\s+\w+\s*$", "", kod, flags=re.MULTILINE)
    py_kod = turkce_to_python(temiz_kod)

    print(Fore.MAGENTA + "----- ÇEVRİLMİŞ PYTHON KODU -----" + Style.RESET_ALL)
    print(py_kod)
    print(Fore.MAGENTA + "---------------------------------" + Style.RESET_ALL)

    try:
        ortam = globals()
        ortam.update(yuklu_moduller)
        for ad, mod in yuklu_moduller.items():
            globals()[ad] = mod
        exec(py_kod, ortam)
    except Exception as e:
        print(hata_mesaji_cevir(e))
        print(Fore.LIGHTBLACK_EX + "\nDetay :" + Style.RESET_ALL)
        traceback.print_exc(limit=1)

if __name__ == "__main__":
    main()


