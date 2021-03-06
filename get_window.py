import win32gui
import re
from mute import controlKeyboard
from mute import type_chat

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def mute_lol(): 
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
            if "zoom" in i[1].lower():
                # print(i)
                # win32gui.ShowWindow(i[0],5)
                win32gui.SetForegroundWindow(i[0])
                controlKeyboard()
                type_chat()
                break
    # print(top_windows)

mute_lol()
