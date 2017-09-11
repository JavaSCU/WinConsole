# encoding: utf-8

# cody by github@wangjia.net

import ctypes, sys
from mylibs import Utils


class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]


class SMALL_RECT(ctypes.Structure):
    _fields_ = [("Left", ctypes.c_short), ("Top", ctypes.c_short), ("Right", ctypes.c_short), ("Bottom", ctypes.c_short)]


class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
    _fields_ = [("dwSize", COORD), ("dwCursorPosition", COORD), ("wAttributes", ctypes.c_ushort), ("srWindow", SMALL_RECT), ("dwMaximumWindowSize", COORD)]


class EnvriomentError(Exception):
    pass


class RunError(Exception):
    pass


class WinConsoleClass:
	STD_INPUT_HANDLE		= -10
	STD_OUTPUT_HANDLE		= -11
	STD_ERROR_HANDLE		= -12

	INVALID_HANDLE_VALUE	= -1

	FOREGROUND_BLACK		= 0x0000
	FOREGROUND_BLUE			= 0x0001
	FOREGROUND_GREEN		= 0x0002
	FOREGROUND_CYAN			= 0x0003
	FOREGROUND_RED			= 0x0004
	FOREGROUND_MAGENTA		= 0x0005
	FOREGROUND_YELLOW		= 0x0006
	FOREGROUND_GREY			= 0x0007
	FOREGROUND_INTENSITY	= 0x0008

	BACKGROUND_BLACK		= 0x0000
	BACKGROUND_BLUE			= 0x0010
	BACKGROUND_GREEN		= 0x0020
	BACKGROUND_CYAN			= 0x0030
	BACKGROUND_RED			= 0x0040
	BACKGROUND_MAGENTA 		= 0x0050
	BACKGROUND_YELLOW		= 0x0060
	BACKGROUND_GREY			= 0x0070
	BACKGROUND_INTENSITY	= 0x0080

	h_console_output = None
	origin_fg_color = None
	origin_bg_color = None

	is_run_with_console = False


	def __init__(self):
		if (not (sys.platform == "win32")):
			raise(EnvriomentError("just for windows"))

		self.is_run_with_console = sys.stdout.isatty()
		# another way to detect envrioment:
		# import os
		# self.is_run_with_console = os.isatty(sys.stdin.fileno())

		if (not self.is_run_with_console):
			print("-----warn: not run with console-----")

		self.h_console_output = ctypes.windll.kernel32.GetStdHandle(self.STD_OUTPUT_HANDLE)
		if ((self.h_console_output == self.INVALID_HANDLE_VALUE)  or (self.h_console_output == None)):
			raise(RunError("GetStdHandle: invalid handle value"))

		color_color = self.get_console_color()
		self.origin_fg_color = color_color["fg_color"]
		self.origin_bg_color = color_color["bg_color"]


	def get_console_color(self):
		ret_data = {}

		if(self.is_run_with_console):
			lp_console_screen_buffer_info = CONSOLE_SCREEN_BUFFER_INFO()
			ret = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(self.h_console_output, ctypes.byref(lp_console_screen_buffer_info))
			if (ret == 0):
				error_data = Utils.get_last_error()
				raise(RunError("get_console_color - GetConsoleScreenBufferInfo error, code: %s, msg: %s" %(error_data["error_id"], error_data["error_msg"])))

			ret_data["bg_color"] = lp_console_screen_buffer_info.wAttributes & 0x0070
			ret_data["fg_color"]= lp_console_screen_buffer_info.wAttributes & 0x0007
		else:
			ret_data["bg_color"] = -1
			ret_data["fg_color"]= -1

		return ret_data


	def set_console_color(self, fg_color, bg_color):
		if(self.is_run_with_console):
			ret = ctypes.windll.kernel32.SetConsoleTextAttribute(self.h_console_output, fg_color | bg_color)
			if (ret == 0):
				error_data = Utils.get_last_error()
				raise(RunError("SetConsoleTextAttribute error, code: %s, msg: %s" %(error_data["error_id"], error_data["error_msg"])))


	def restore_console_color(self):
		self.set_console_color(self.origin_fg_color, self.origin_bg_color)


	def restore_console_default_color(self):
		self.set_console_color(self.FOREGROUND_GREY, self.BACKGROUND_BLACK)


	def get_console_cursor_pos(self):
		ret_data = {}

		if(self.is_run_with_console):
			lp_console_screen_buffer_info = CONSOLE_SCREEN_BUFFER_INFO()
			ret = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(self.h_console_output, ctypes.byref(lp_console_screen_buffer_info))
			if (ret == 0):
				error_data = Utils.get_last_error()
				raise(RunError("get_console_cursor_pos - GetConsoleScreenBufferInfo error, code: %s, msg: %s" %(error_data["error_id"], error_data["error_msg"])))

			ret_data["x"] = lp_console_screen_buffer_info.dwCursorPosition.X
			ret_data["y"] = lp_console_screen_buffer_info.dwCursorPosition.Y
		else:
			ret_data["x"] = -1
			ret_data["y"] = -1

		return ret_data


	def set_console_cursor_pos(self, x, y):
		if(self.is_run_with_console):
			dw_cursor_position = COORD()
			dw_cursor_position.X = x
			dw_cursor_position.Y = y
			ret = ctypes.windll.kernel32.SetConsoleCursorPosition(self.h_console_output, dw_cursor_position)
			if (ret == 0):
				error_data = Utils.get_last_error()
				raise(RunError("set_console_cursor_pos - SetConsoleCursorPosition error, code: %s, msg: %s" %(error_data["error_id"], error_data["error_msg"])))

		return


	def print_in_one_line(self, str, **kwargs):
		ret = self.get_console_cursor_pos()
		print(str, **kwargs)
		self.set_console_cursor_pos(ret["x"], ret["y"])


