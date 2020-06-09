import pyscreenshot as ImageGrab
import numpy as np
import cv2


import gtk.gdk

w = gtk.gdk.get_default_root_window()
sz = w.get_size()

width ,height =sz


while(True):
    img = ImageGrab.grab(bbox=(0,0,width-100,height-100)) #bbox specifies specific region (bbox= x1,x2,y1 (width),y2(height))
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow("test", frame)
    cv2.waitKey(0)
cv2.destroyAllWindows()