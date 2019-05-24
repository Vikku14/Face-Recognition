import cv2
import os
import numpy as np



class FaceRecognition:
	boolian_list = list()
	subjects = ["",'vivek',"Unknown"]
	FLAG=0
	TOTAL_FACES=0

	def __init__(self):
		pass

	def predict_faces(self):

		faces = np.load('/home/vikku/PycharmProjects/face_recognition/face_data.npy')
		labels = np.load('/home/vikku/PycharmProjects/face_recognition/label_data.npy')

		self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()

		self.face_recognizer.train(faces, np.array(labels))


		print("Predicting image...")

		self.fetching_user()

		print("Prediction complete")

		if any(FaceRecognition.boolian_list):
			print("autenticated Person")

		else:
			print("unauterised Access")
			FaceRecognition.FLAG =1

	# display both images
	# cv2.imshow("Deduction", predicted_img1)
	# cv2.imshow(subjects[2], predicted_img2)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	def detect_face(self,img):

		gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		face_cascade= cv2.CascadeClassifier('/usr/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
		faces= face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors= 5)

		if len(faces) == 0:


			FaceRecognition.boolian_list.append(False)
			return None, None

		(x,y,w,h)= faces[0]

		return gray[y:y+w,x:x+h], faces[0]

	def prepare_training_data(self,data_folder_path):
		dirs= os.listdir(data_folder_path)
		faces=[]
		labels= []
		for dir_name in dirs:
			if not dir_name.startswith("s"):
				continue
			label= int(dir_name.replace("s",""))

			subject_dir_path= data_folder_path + "/" + dir_name
			subject_images_names= os.listdir(subject_dir_path)

			for image_name in subject_images_names:
				if image_name.startswith("."):
					continue
				image_path= subject_dir_path + "/" + image_name

				image=cv2.imread(image_path)
				cv2.imshow("Appreciating Your Beauty..", image)
				cv2.waitKey(100)

				face, rect=  self.detect_face(image)
				if face is not None:
					faces.append(face)
					labels.append(label)
				cv2.destroyAllWindows()
				cv2.waitKey(1)
		cv2.destroyAllWindows()
		return faces, labels

	def draw_rectangle(self,img, rect):
		(x,y,w,h) = rect
		cv2.rectangle(img,(x,y), (x+w,y+h),(0,255,0),2)

	def draw_text(self,img, text, x,y):
		cv2.putText(img,text, (x,y),cv2.FONT_HERSHEY_PLAIN, 1.5,(255,0,255),2)

	def predict(self, test_img):
		img = test_img.copy()
		face,rect = self.detect_face(img)
		label, confidence= self.face_recognizer.predict(face)
		label_text= FaceRecognition.subjects[label]

		if label_text is not "vivek":
			FaceRecognition.boolian_list.append(False)
		else:
			FaceRecognition.boolian_list.append(True)

		self.draw_rectangle(img,rect)
		self.draw_text(img, label_text, rect[0],rect[1]-5)
		return img


	def populate_face(self):
		print("preparing data...")
		faces,labels=self.prepare_training_data("/home/vikku/PycharmProjects/face_recognition/trainning_data")
		print("Data_prepared")
		np.save('face_data',faces)
		np.save('label_data',labels)
		print("total faces ",len(faces))
		print("total labels ",len(labels))
		FaceRecognition.TOTAL_FACES = len(faces)

	def fetching_user(self):
		images= os.listdir('/home/vikku/Pictures/face/')
		for image in images:
			try:
				self.predict(cv2.imread('/home/vikku/Pictures/face/'+image))
				# predicted_image = self.predict(cv2.imread('/home/vikku/Pictures/face/'+image))
				# cv2.imshow(subjects[1], predicted_image)
				# cv2.waitKey(0)
				# cv2.destroyAllWindows()
			except:
				continue
