import cv2

# Kamerayı aç
kamera = cv2.VideoCapture(0)

while True:
    ret, kare = kamera.read()
    if not ret:
        break
    
    # Kameradan gelen görüntüyü göster
    cv2.imshow("Canlı Kamera", kare)

    # 'q' tuşuna basınca çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()