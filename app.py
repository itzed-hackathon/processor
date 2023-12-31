#!/usr/bin/env python

import json
import asyncio
from websockets.server import serve
import pyautogui
import mouse
import time
from threading import Thread

# 1536, 864
size = pyautogui.size()
midp = (size.width // 2, size.height // 2)
sw = 1536
sh = 864
bs = 300
bsy = 200

walking = False

def fwd():
    global walking
    if not walking:
        pyautogui.keyDown('alt')
        pyautogui.keyDown('w')
        walking = True

def unfwd():
    global walking
    if walking:
        pyautogui.keyUp('alt')
        pyautogui.keyUp('w')
        walking = False

async def echo(websocket):
    async for message in websocket:
        data = json.loads(message)
        if 'blink' in data: 
            print('BLINK')
            pyautogui.click()
            continue
        x = data['x']
        y = data['y']
        pos = mouse.get_position()

        if x < sw/2-bs:
            print('left')
            mouse.move(-9, 0, False, 0)
        elif x > sw/2+bs:
            print('right')
            mouse.move(9, 0, False, 0)
        else:
            print('xmid')
            #mouse.move(midp[0], pos[1], True, 0)

        print(y, sh/2+bsy)
        # y -= 20
        if y > sh/2+bsy/2:
            print('down')
            mouse.move(0, 9, False, 0)
        elif y < sh/2-bsy:
            print('up')
            mouse.move(0, -9, False, 0)
        else:
            print('ymid')
            #mouse.move(pos[0], midp[1], True, 0)

        if y < sh/2+bsy and y > sh/2-bsy and x > sw/2-bs and x < sw/2+bs:
            print('onward!')
            fwd()
        else:
            unfwd()

async def main():
    async with serve(echo, "localhost", 5001):
        await asyncio.Future()  # run forever

asyncio.run(main())
