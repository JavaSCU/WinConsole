# Introduce #
**WinConsole** is a simple Python3 tool for windows console control, such as font color, backgroud color, cursor position. You can print something within one line, such as a percent of progress.

It call win32 api for implementation, so it could just work with Windows "Command Line Console".

This is a custom library of my Python experiment. I just use/test it under Windows 7.
![WinConsole sample](https://github.com/JavaSCU/WinConsole/blob/master/WinConsole_sample.png?raw=true)

----
# How to use #
Here is an example "WinConsole_sample.py", the main steps include:

1) download "WinConsole.py" and put it with your codes or libs

2) import this module

```Python
import WinConsole
```

3) create a object of WinConsole

```Python
c = WinConsole.WinConsoleClass()
```

4) call some functions of WinConsole, such as

```Python
c.get_console_color()
```

----
# API #
## get\_console\_color() ##

get current console backgroud color and foregroud color

*input: nothing*

*return: a dict with "bg_color", "fg_color" elements.*
</br>
## set\_console\_color(fg_color, bg_color) ##

set current console backgroud color and foregroud color

*input: foregroud color as "fg_color", backgroud color as "bg_color"*

*return: nothing*
</br>
## restore\_console\_color() ##

restore backgroud color and foregroud color when you create the object of WinConsole

*input: nothing*

*return: nothing*
</br>
## restore\_console\_default\_color() ##

restore the console defautl backgroud color(FOREGROUND_GREY) and foregroud (BACKGROUND_BLACK) color.

*input: nothing*

*return: nothing*
</br>
## get\_console\_cursor\_pos() ##

get current console cursor position

*input: nothing*

*return: a coordinate dict with "x", "y" elements.*
</br>
## set\_console\_cursor\_pos(x, y) ##

set current console cursor position

*input: horizontal axis as "x", vertical axis as "y"*

*return: nothing*
</br>
## print\_in\_one\_line(str, \*\*kwargs) ##

you can print something within one line, such as a percent of progress.

*input: as build in method "print"*

*return: nothing*


----
# Colors #
## foregroud (font) color ##

- FOREGROUND_BLACK
- FOREGROUND_BLUE
- FOREGROUND_GREEN
- FOREGROUND_CYAN
- FOREGROUND_RED
- FOREGROUND_MAGENTA
- FOREGROUND_YELLOW
- FOREGROUND_GREY
- FOREGROUND_INTENSITY	

## backgroud color ##
- BACKGROUND_BLACK
- BACKGROUND_BLUE
- BACKGROUND_GREEN
- BACKGROUND_CYAN
- BACKGROUND_RED
- BACKGROUND_MAGENTA
- BACKGROUND_YELLOW
- BACKGROUND_GREY
- BACKGROUND_INTENSITY


*FOREGROUND_INTENSITY / BACKGROUND_INTENSITY used to intensify color, make or operation with other colors. eg. FOREGROUND_RED | FOREGROUND_INTENSITY, BACKGROUND_GREY | BACKGROUND_INTENSITY*


