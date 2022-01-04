# ObjectDetection
![image_detected](https://user-images.githubusercontent.com/89344186/148072481-11677450-6e36-4431-a2e2-4f45a4a087c4.jpg)
Download weights dan file cfg yang akan digunakan melalui https://pjreddie.com/darknet/yolo/.
Pada line 15, ubah (608, 608) sesuai weights yang digunakan. Pada tugas ini digunakan YOLOv3-608.
line 15:
```
blob=cv2.dnn.blobFromImage(img, 1/255, (608,608), (0,0,0), swapRB=True, crop=False)
```

Masukkan nama file gambar yang akan dideteksi pada line 10, RUN.



Pada video detection, masukkan nama file video pada line 9. Jika menggunakan webcam masukkan 0.
line 9:
```
cap = cv2.VideoCapture(0)
```
