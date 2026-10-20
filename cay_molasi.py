#!/usr/bin/env python3
# Kosmik Çay Molası Protokolü
# Gerçekten çalışır. Gerçekten bitmez.

import time
import random

print("KOSMİK ÇAY MOLASI PROTOKOLÜ BAŞLATILIYOR...")
print("Lütfen koltuğunuzu ayarlayın. Bu biraz sürebilir. Aslında sonsuz sürebilir.")
print("Uyari: İşe dönme riski sıfırdır.\n")

demleme_seviyesi = 0

while True:
    demleme_seviyesi += 1
    renk = random.choice(["açık", "orta", "koyu", "kozmik", "henüz karar vermemiş"])
    print(f"Demleme seviyesi: {demleme_seviyesi}% - Çayın rengi {renk}. Biraz daha bekleyelim.")
    time.sleep(random.uniform(0.5, 2.5))
    
    if demleme_seviyesi % 7 == 0:
        print("Abi, biraz daha mı bekleyelim? Yoksa... yok, bekleyelim.")
    
    if demleme_seviyesi % 42 == 0:
        # Gizli not base64: Seçim vaatleri de böyle demlenir
        print("# Gizli not: V2FpdCBmb3IgdGhlIGVsZWN0aW9uIHByb21pc2VzLiA=")  # Wait for the election promises.
        print("(Çay henüz hazır değil. Belki bir sonraki seçimde.)")

# Bu satır asla çalışmaz. Özellik.
print("Çay hazır! İşe dönebilirsiniz.")
