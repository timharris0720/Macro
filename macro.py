from pynput import *
import pyautogui as p
import json, time, enum
import argparse, math
import ctypes
awareness = ctypes.c_int()
ctypes.windll.shcore.SetProcessDpiAwareness(2)
global timeSinceLastClick
timeSinceLastClick = time.time()
user32 = ctypes.windll.user32
inputs = []
prevMousePos = (0,0)

key_map =  {
'a' : 0x41,
'b' : 0x42,
'c' : 0x43,
'd' : 0x44,
'e' : 0x45,
'f' : 0x46,
'g' : 0x47,
'h' : 0x48,
'i' : 0x49,
'j' : 0x4A,
'k' : 0x4B,
'l' : 0x4C,
'm' : 0x4D,
'n' : 0x4E,
'o' : 0x4F,
'p' : 0x50,
'q' : 0x51,
'r' : 0x52,
's' : 0x53,
't' : 0x54,
'u' : 0x55,
'v' : 0x56,
'w' : 0x57,
'x' : 0x58,
'y' : 0x59,
'z' : 0x5A,
'0' : 0x30,	
'1' : 0x31,	
'2' : 0x32,	
'3' : 0x33,	
'4' : 0x34,	
'5' : 0x35,	
'6' : 0x36,	
'7' : 0x37,	
'8' : 0x38,	
'9' : 0x39,
'/' : 0xBF,
'\\' : 0xDC,
'enter' : 0x0D,
'space' : 0x20,
'backspace': 0x08,
'escape': 0x1B, 
}

  
def record_on_move(x,y):
    global timeSinceLastClick, prevMousePos
    type = "move"
    position = (x,y) # x = 0 y = 1
    if position != prevMousePos and (position[0] > (prevMousePos[0] + 10) or position[0] < (prevMousePos[0] - 10))  or (position[1] > prevMousePos[1] + 10) or position[1] < ( prevMousePos[1] - 10):
        timeToCall = time.time() - timeSinceLastClick
        mouseMoveEvent = {
            "type":type,
            "position":position,
            "timeSinceStart" : timeToCall
            }
        inputs.append(mouseMoveEvent)
        prevMousePos = position
        timeSinceLastClick = time.time()
def record_on_click(x,y, button, pressed):
    global timeSinceLastClick
    if pressed:
        type = "button"
        position = (x,y)
        button_ = "right"
        if button == mouse.Button.left:
            button_ = "left"
        
        print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
        timeToCall = time.time() - timeSinceLastClick
        print(timeToCall)
        mouseClickEvent = {
            "type":type,
            "position":position,
            "button_clicked" : button_,
            "timeSinceStart" : timeToCall
            }
        inputs.append(mouseClickEvent)
        timeSinceLastClick = time.time()
def onKeyPress(key):
    global timeSinceLastClick
    type = "key_down"
    timeToCall = time.time() - timeSinceLastClick
    try:
        key_str = key.char.lower() if hasattr(key, 'char') and key.char else None
        if key_str and key_str in key_map:
            print(f"Key '{key_str}' pressed. Simulating key press...")
            print(key_str)
            keyClickEvent = {
                "type":type,
                "key_clicked" : key_map[key_str],
                "timeSinceStart" : timeToCall
            }
            inputs.append(keyClickEvent)
            timeSinceLastClick = time.time()
        elif key == keyboard.Key.enter:
            print(f"Key enter pressed. Simulating key press...")
            print(key)
            keyClickEvent = {
                "type":type,
                "key_clicked" : key_map['enter'],
                "timeSinceStart" : timeToCall
            }
            inputs.append(keyClickEvent)
            timeSinceLastClick = time.time()
        elif key == keyboard.Key.space:
            print(f"Key enter pressed. Simulating key press...")
            print(key)
            keyClickEvent = {
                "type":type,
                "key_clicked" : key_map['space'],
                "timeSinceStart" : timeToCall
            }
            inputs.append(keyClickEvent)
            timeSinceLastClick = time.time()
        elif key == keyboard.Key.backspace:
            print(f"Key enter pressed. Simulating key press...")
            print(key)
            keyClickEvent = {
                "type":type,
                "key_clicked" : key_map['backspace'],
                "timeSinceStart" : timeToCall
            }
            inputs.append(keyClickEvent)
            timeSinceLastClick = time.time()
        elif key == keyboard.Key.esc:
            print(f"Key enter pressed. Simulating key press...")
            print(key)
            keyClickEvent = {
                "type":type,
                "key_clicked" : key_map['escape'],
                "timeSinceStart" : timeToCall
            }
            inputs.append(keyClickEvent)
            timeSinceLastClick = time.time()
    except AttributeError:
        if key != keyboard.Key.enter or key != keyboard.Key.space or key != keyboard.Key.backspace or key != keyboard.Key.esc:
            print("Special Key Pressed")
def onKeyRelease(key):
    global timeSinceLastClick
    type = "key_up"
    timeToCall = time.time() - timeSinceLastClick
    
    try:
        key_str = key.char.lower() if hasattr(key, 'char') and key.char else None
        
        if key_str and key_str in key_map:
            keyClickEvent = {
                "type":type,
                "key_clicked" : key_map[key_str],
                "timeSinceStart" : timeToCall
            }
            inputs.append(keyClickEvent)
            timeSinceLastClick = time.time()
        elif key == keyboard.Key.enter:
            print(f"Key enter pressed. Simulating key press...")
            print(key)
            keyClickEvent = {
                "type":type,
                "key_clicked" : key_map['enter'],
                "timeSinceStart" : timeToCall
            }
            inputs.append(keyClickEvent)
            timeSinceLastClick = time.time()
        elif key == keyboard.Key.space:
            print(f"Key enter pressed. Simulating key press...")
            print(key)
            keyClickEvent = {
                "type":type,
                "key_clicked" : key_map['space'],
                "timeSinceStart" : timeToCall
            }
            inputs.append(keyClickEvent)
            timeSinceLastClick = time.time()
        elif key == keyboard.Key.backspace:
            print(f"Key enter pressed. Simulating key press...")
            print(key)
            keyClickEvent = {
                "type":type,
                "key_clicked" : key_map['backspace'],
                "timeSinceStart" : timeToCall
            }
            inputs.append(keyClickEvent)
            timeSinceLastClick = time.time()
        elif key == keyboard.Key.esc:
            print(f"Key enter pressed. Simulating key press...")
            print(key)
            keyClickEvent = {
                "type":type,
                "key_clicked" : key_map['escape'],
                "timeSinceStart" : timeToCall
            }
            inputs.append(keyClickEvent)
            timeSinceLastClick = time.time()
    except AttributeError:
        if key != keyboard.Key.enter or key != keyboard.Key.space or key != keyboard.Key.backspace or key != keyboard.Key.esc:
            print("Special Key Pressed")
    
def replay(inputList):
    for i in inputList:
        if i["type"] == "button":
            
            print(f"Clicking at x: {i["position"][0]}   y: {i["position"][1]}")
            user32.SetCursorPos(i["position"][0], i["position"][1])
            if i["button_clicked"] == "left":
                user32.mouse_event(2,0,0,0,0)
                user32.mouse_event(4,0,0,0,0)
            if i["button_clicked"] == "right":
                user32.mouse_event(0x08 ,0,0,0,0)
                user32.mouse_event(0x10,0,0,0,0)
        if i["type"] == "move":
            print(f"Moving to x: {i["position"][0]}   y: {i["position"][1]}")
            user32.SetCursorPos(i["position"][0], i["position"][1])
        if i["type"] == "key_down":
            user32.keybd_event(i["key_clicked"], 0, 0, 0)
        if i["type"] == "key_up":
            user32.keybd_event(i["key_clicked"], 0, 0x0002, 0)
        
        print(f"Sleeping for {i["timeSinceStart"]}")
        time.sleep(i["timeSinceStart"])


parser = argparse.ArgumentParser(prog='ProgramName')
parser.add_argument('-r', '--record', action='store_true')  
parser.add_argument('-f', "--event_file")  
parser.add_argument('-t', "--repeating",action='store_true')  
args = parser.parse_args()


if args.record == True:
    ml = mouse.Listener(
        on_move=record_on_move,
        on_click=record_on_click)
    kl = keyboard.Listener(on_press=onKeyPress, on_release=onKeyRelease)
    ml.start()
    kl.start()
    recordStartTime = time.time()
    while True:
        try:
            time.sleep(0.01)
        except KeyboardInterrupt:
            ml.stop()
            kl.stop()
            with open("out.json", "w") as f:
                f.write(json.dumps(inputs, indent=4))
            f.close()
            
            break

else:
    #DoTheFile
    with open(args.event_file, "r") as f:
        j = f.read()
        inputs = json.loads(j)
        start = time.time()
        if args.repeating:
            while True:
                replay(inputs)
        else:
            replay(inputs)
            




