import cv2
import numpy as np

net=cv2.dnn.readNet('yolov3.weights','yolov3.cfg.txt')
classes = []
with open('coco.names.txt','r') as f:
    classes = f.read().splitlines()

#Mengambil gambar yang akan dideteksi
image_name='image.jpg'
img=cv2.imread(image_name)

height,width,_=img.shape

blob=cv2.dnn.blobFromImage(img, 1/255, (608,608), (0,0,0), swapRB=True, crop=False)
net.setInput(blob)
output_layers_names=net.getUnconnectedOutLayersNames()
layerOutputs=net.forward(output_layers_names)

boxes = []
confidences = []
class_ids = []

for output in layerOutputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.1:
            center_x = int(detection[0]*width)
            center_y = int(detection[1]*height)
            w = int(detection[2]*width)
            h = int(detection[3]*height)

            x = int(center_x - w/2)
            y = int(center_y - h/2)

            boxes.append([x,y,w,h])
            confidences.append(float(confidence))
            class_ids.append(class_id)


indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

#Font label dan warna kotak yang digunakan
font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size=(len(boxes), 3))

for i in indexes.flatten():
    x, y, w, h = boxes[i]
    label = str(classes[class_ids[i]])
    confidence = str(round(confidences[i],2))
    color = colors[i]
    cv2.rectangle(img,(x, y), (x+w, y+h), color, 2)
    cv2.putText(img, label +" "+ confidence, (x+20, y+20), font, 1, (255,255,255), 2)

#Menyimpan gambar hasil deteksi
if image_name[-4]=='.':
    cv2.imwrite(image_name[:-4]+"_detected.jpg", img)
else:
    cv2.imwrite(image_name[:-5]+"_detected.jpg", img)

#Menampilkan gambar hasil deteksi
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()