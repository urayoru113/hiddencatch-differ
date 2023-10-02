from configparser import ConfigParser

import cv2
import numpy as np
import win32con
import win32gui
import win32ui
from PIL import Image


def screenshot(class_name):
    hwnd = win32gui.FindWindow(class_name, None)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top
    if w < 800 or h < 600:
        w = 806
        h = 629
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    cdc = mfcDC.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(mfcDC, w, h)
    cdc.SelectObject(bmp)
    cdc.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)

    bmp.GetInfo()
    bmpstr = bmp.GetBitmapBits(True)
    im = Image.frombytes("RGBA", (w, h), bmpstr)
    im = np.array(im)
    cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

    win32gui.DeleteObject(bmp.GetHandle())
    cdc.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    return im


CLASS_NAME = "Crazy Arcade"
CONFIG_FILE = "setting.ini"

if __name__ == "__main__":
    print("Please adjust file: setting.ini")

    config = ConfigParser()

    while True:
        config.read(CONFIG_FILE)

        position = config["POSITION"]
        panel = config["PANEL"]
        x1 = int(position["x1"])
        x2 = int(position["x2"])
        y = int(position["y"])
        w = int(panel["w"])
        h = int(panel["h"])

        img = screenshot(config["PROCESS"]["name"])
        img1 = img[y: y + h, x1: x1 + w]
        img2 = img[y: y + h, x2: x2 + w]
        diff = cv2.absdiff(img1, img2)

        cv2.rectangle(img, (x1, y), (x1 + w, y + h), (0, 0, 255), 1)
        cv2.rectangle(img, (x2, y), (x2 + w, y + h), (0, 0, 255), 1)

        cv2.imshow("diff", diff)
        cv2.imshow("rect", img)
        key = cv2.waitKey(10)
        if key == 27:
            break
        if cv2.getWindowProperty("diff", cv2.WND_PROP_VISIBLE) < 1:
            break
        if cv2.getWindowProperty("rect", cv2.WND_PROP_VISIBLE) < 1:
            break
    cv2.destroyAllWindows()
