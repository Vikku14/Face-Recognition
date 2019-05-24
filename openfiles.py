import subprocess, os, platform
def openfile(filepath):
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(filepath)
    else:                                   # linux variants
        subprocess.call(('cheese',))


openfile('/home/vikku/trainning_data/s1/1.jpg')