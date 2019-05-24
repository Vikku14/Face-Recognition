from PIL import Image
file_path='/home/vikku/PycharmProjects/face_recognition/animated.gif'
picture = Image.open(file_path)
picture.save("{}".format(file_path), "GIF", optimize=True, quality=85)
