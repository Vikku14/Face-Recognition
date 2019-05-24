import os
import datetime
f= open('/home/vikku/PycharmProjects/face_recognition/face_file.txt','w+')
f.write(str(datetime.datetime.now())+"\n")
f.close()
Datafile_location='/home/vikku/PycharmProjects/face_recognition/face_file.txt'
os.system("python3 /home/vikku/PycharmProjects/face_recognition/startupProgram.py >> {}".format(Datafile_location))