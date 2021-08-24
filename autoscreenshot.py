import pyautogui
import time



while True:
    img_name = time.strftime('_%Y%m%d_%H%M%S')
    time.sleep(2)
    pyautogui.screenshot(f'spongebob{img_name}.png',
                         region=(32, 58, 1280, 720))