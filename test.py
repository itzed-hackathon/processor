#!/usr/bin/env python3
import time 
import mouse 

time.sleep(3)

pos = mouse.get_position()
mouse.move(5, 0, False, 1)
