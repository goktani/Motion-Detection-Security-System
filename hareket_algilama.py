import cv2

# Kamera başlatma
kamera = cv2.VideoCapture(0)

# Arka plan çıkarıcıyı başlat
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, kare = kamera.read()
    if not ret:
        break

    # Arka planı çıkar
    fgmask = fgbg.apply(kare)

    # Maskeyi threshold ile filtrele
    _, fgmask = cv2.threshold(fgmask, 25, 255, cv2.THRESH_BINARY)

    # Konturları bul
    konturlar, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    hareket_var = False
    for kontur in konturlar:
        if cv2.contourArea(kontur) > 500:  # Küçük hareketleri göz ardı et
            (x, y, w, h) = cv2.boundingRect(kontur)
            cv2.rectangle(kare, (x, y), (x + w, y + h), (0, 255, 0), 2)
            hareket_var = True

    if hareket_var:
        print("🚨 Hareket Algılandı!")
    else:
        print("✅ Hareket Yok.")

    # Görüntüyü göster
    cv2.imshow('Hareket Algılama', kare)

    # 'q' tuşuna basınca çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
