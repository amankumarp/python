import ctypes
import os
import time 
cwdir=os.getcwd()
cwdir+='\Wallpaper'
os.chdir(cwdir)
arr=os.listdir()
for img in arr:
    w=cwdir+r'\\'+img
    print(w);
    ctypes.windll.user32.SystemParametersInfoW(20,0,w,0)
    time.sleep(30)
