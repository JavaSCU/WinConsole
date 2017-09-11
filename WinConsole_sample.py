# encoding: utf-8

# cody by github@wangjia.net

import WinConsole
import time

c = WinConsole.WinConsoleClass()

default_colors = c.get_console_color()

c.set_console_color(c.FOREGROUND_YELLOW, c.BACKGROUND_BLACK)
print("yellow font")

c.restore_console_color()
print("origin font and background color")

c.set_console_color(c.FOREGROUND_RED | c.FOREGROUND_INTENSITY, c.BACKGROUND_GREY | c.BACKGROUND_INTENSITY)
print("intensity red font with blue background")

c.restore_console_default_color()
print("origin font and background color")

print("=================================================")

i = 0
while (i <= 5):
	c.print_in_one_line("counter: %d" %(i), end='\n')
	i = i + 1
	time.sleep(0.1)


