import os
import sys
import time
dir = os.path.dirname(os.path.abspath(__file__))
for file in os.listdir(dir):
    if file != __file__:
        unixfiletime = os.path.getctime(os.path.join(dir, file))
        ymd = time.strftime("%Y%m%d", time.localtime(unixfiletime))
        print(file + ": " + ymd)
        try:
            os.mkdir(os.path.join(dir, ymd))
        except:
            pass
        os.rename(os.path.join(dir, file), os.path.join(os.path.join(dir, ymd), file))
