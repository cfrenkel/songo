from random import randint
import cv2
import sys
import os
      
CASCADE="Face_cascade.xml"
FACE_CASCADE=cv2.CascadeClassifier(CASCADE)

def detect_faces(image_path):
	print(image_path)
	image = cv2.imread(image_path)
	image_grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


	faces = FACE_CASCADE.detectMultiScale(image_grey,scaleFactor=1.16,minNeighbors=5,minSize=(25,25),flags=0)
	count_of_face = 0

	for x,y,w,h in faces:
	    sub_img=image[y-10:y+h+10,x-10:x+w+10]
	    os.chdir("extracted")
	    cv2.imwrite(str(randint(0,10000))+".png",sub_img)
	    os.chdir("../")
	    cv2.rectangle(image,(x,y),(x+w,y+h),(255, 255,0),2)
	count_of_face = print(len(faces))



	# cv2.imshow("Faces Found",image)
	# if (cv2.waitKey(0) & 0xFF == ord('q')) or (cv2.waitKey(0) & 0xFF == ord('Q')):
	# 	cv2.destroyAllWindows()

	return count_of_face

# print(detect_faces('fa.png'))
