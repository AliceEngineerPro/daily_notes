import pyautogui
import time
import pyperclip
from tqdm import tqdm

if __name__ == '__main__':
    while 1:
        print('2秒开始')
        time.sleep(5)
        pyautogui.click(1448, 448)
        pyperclip.copy('测试')
        time.sleep(2)
        pyautogui.hotkey('ctrl','v')
        pyautogui.click(1869, 638)
        # print(pyautogui.KEYBOARD_KEYS)
        for _  in tqdm(range(5)):
            time.sleep(1)
        