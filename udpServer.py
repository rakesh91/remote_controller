# UDP server example
import socket
import string
import time
import uinput
import os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("", 5001))


print"UDPServer Waiting for client on port 5000"

def emitCharacter(character):
	if (character == ''):
		return
	elif (character == 'A'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_A, 1)
		device.emit(uinput.KEY_A, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'B'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_B, 1)
		device.emit(uinput.KEY_B, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'C'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_C, 1)
		device.emit(uinput.KEY_C, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'D'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_D, 1)
		device.emit(uinput.KEY_D, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'E'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_E, 1)
		device.emit(uinput.KEY_E, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'F'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_F, 1)
		device.emit(uinput.KEY_F, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'G'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_G, 1)
		device.emit(uinput.KEY_G, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'H'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_H, 1)
		device.emit(uinput.KEY_H, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'I'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_I, 1)
		device.emit(uinput.KEY_I, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'J'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_J, 1)
		device.emit(uinput.KEY_J, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'K'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_K, 1)
		device.emit(uinput.KEY_K, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'L'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_L, 1)
		device.emit(uinput.KEY_L, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'M'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_M, 1)
		device.emit(uinput.KEY_M, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'N'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_N, 1)
		device.emit(uinput.KEY_N, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'O'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_O, 1)
		device.emit(uinput.KEY_O, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'P'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_P, 1)
		device.emit(uinput.KEY_P, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'Q'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_Q, 1)
		device.emit(uinput.KEY_Q, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'R'):
		device.emit(uinput.KEY_CAPSLOCK, 1)
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_R, 1)
		device.emit(uinput.KEY_R, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'S'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_S, 1)
		device.emit(uinput.KEY_S, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'T'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_T, 1)
		device.emit(uinput.KEY_T, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'U'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_U, 1)
		device.emit(uinput.KEY_U, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'V'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_V, 1)
		device.emit(uinput.KEY_V, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'W'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_W, 1)
		device.emit(uinput.KEY_W, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'X'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_X, 1)
		device.emit(uinput.KEY_X, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'Y'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_Y, 1)
		device.emit(uinput.KEY_Y, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1)
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'Z'):
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
		device.emit(uinput.KEY_Z, 1)
		device.emit(uinput.KEY_Z, 0)
		device.emit(uinput.KEY_CAPSLOCK, 1) 
		device.emit(uinput.KEY_CAPSLOCK, 0)
	elif (character == 'a'):
		device.emit(uinput.KEY_A, 1)
		device.emit(uinput.KEY_A, 0)
	elif (character == 'b'):
		device.emit(uinput.KEY_B, 1)
		device.emit(uinput.KEY_B, 0)
	elif (character == 'c'):
		device.emit(uinput.KEY_C, 1)
		device.emit(uinput.KEY_C, 0)
	elif (character == 'd'):
		device.emit(uinput.KEY_D, 1)
		device.emit(uinput.KEY_D, 0)
	elif (character == 'e'):
		device.emit(uinput.KEY_E, 1)
		device.emit(uinput.KEY_E, 0)
	elif (character == 'f'):
		device.emit(uinput.KEY_F, 1)
		device.emit(uinput.KEY_F, 0)
	elif (character == 'g'):
		device.emit(uinput.KEY_G, 1)
		device.emit(uinput.KEY_G, 0)
	elif (character == 'h'):
		device.emit(uinput.KEY_H, 1)
		device.emit(uinput.KEY_H, 0)
	elif (character == 'i'):
		device.emit(uinput.KEY_I, 1)
		device.emit(uinput.KEY_I, 0)
	elif (character == 'j'):
		device.emit(uinput.KEY_J, 1)
		device.emit(uinput.KEY_J, 0)
	elif (character == 'k'):
		device.emit(uinput.KEY_K, 1)
		device.emit(uinput.KEY_K, 0)
	elif (character == 'l'):
		device.emit(uinput.KEY_L, 1)
		device.emit(uinput.KEY_L, 0)
	elif (character == 'm'):
		device.emit(uinput.KEY_M, 1)
		device.emit(uinput.KEY_M, 0)
	elif (character == 'n'):
		device.emit(uinput.KEY_N, 1)
		device.emit(uinput.KEY_N, 0)
	elif (character == 'o'):
		device.emit(uinput.KEY_O, 1)
		device.emit(uinput.KEY_O, 0)
	elif (character == 'p'):
		device.emit(uinput.KEY_P, 1)
		device.emit(uinput.KEY_P, 0)
	elif (character == 'q'):
		device.emit(uinput.KEY_Q, 1)
		device.emit(uinput.KEY_Q, 0)
	elif (character == 'r'):
		device.emit(uinput.KEY_R, 1)
		device.emit(uinput.KEY_R, 0)
	elif (character == 's'):
		device.emit(uinput.KEY_S, 1)
		device.emit(uinput.KEY_S, 0)
	elif (character == 't'):
		device.emit(uinput.KEY_T, 1)
		device.emit(uinput.KEY_T, 0)
	elif (character == 'u'):
		device.emit(uinput.KEY_U, 1)
		device.emit(uinput.KEY_U, 0)
	elif (character == 'v'):
		device.emit(uinput.KEY_V, 1)
		device.emit(uinput.KEY_V, 0)
	elif (character == 'w'):
		device.emit(uinput.KEY_W, 1)
		device.emit(uinput.KEY_W, 0)
	elif (character == 'x'):
		device.emit(uinput.KEY_X, 1)
		device.emit(uinput.KEY_X, 0)
	elif (character == 'y'):
		device.emit(uinput.KEY_Y, 1)
		device.emit(uinput.KEY_Y, 0)
	elif (character == 'z'):
		device.emit(uinput.KEY_Z, 1)
		device.emit(uinput.KEY_Z, 0)


	elif character == '1':
		device.emit(uinput.KEY_1, 1) 
		device.emit(uinput.KEY_1, 0)
	elif character == '2':
	     device.emit(uinput.KEY_2, 1) 
	     device.emit(uinput.KEY_2, 0)
	elif character == '3':
	     device.emit(uinput.KEY_3, 1) 
	     device.emit(uinput.KEY_3, 0)
	elif character == '4':
	     device.emit(uinput.KEY_4, 1) 
	     device.emit(uinput.KEY_4, 0)
	elif character == '5':
	     device.emit(uinput.KEY_5, 1) 
	     device.emit(uinput.KEY_5, 0)
	elif character == '6':
	     device.emit(uinput.KEY_6, 1) 
	     device.emit(uinput.KEY_6, 0)
	elif character == '7':
	     device.emit(uinput.KEY_7, 1) 
	     device.emit(uinput.KEY_7, 0)
	elif character == '8':
	     device.emit(uinput.KEY_8, 1) 
	     device.emit(uinput.KEY_8, 0)
	elif character == '9':
	     device.emit(uinput.KEY_9, 1) 
	     device.emit(uinput.KEY_9, 0)
	elif character == '0':
	     device.emit(uinput.KEY_0, 1) 
	     device.emit(uinput.KEY_0, 0) 
	elif character == '-':
	     device.emit(uinput.KEY_MINUS, 1) 
	     device.emit(uinput.KEY_MINUS, 0)     
	elif character == '=':
	     device.emit(uinput.KEY_EQUAL, 1) 
	     device.emit(uinput.KEY_EQUAL, 0)
	elif character == 'BACKSPACE':
	     device.emit(uinput.KEY_BACKSPACE, 1) 
	     device.emit(uinput.KEY_BACKSPACE, 0)
	elif character == 'TAB':
	     device.emit(uinput.KEY_TAB, 1) 
	     device.emit(uinput.KEY_TAB, 0)
	elif character == 'LEFTBRACE':
	     device.emit(uinput.KEY_LEFTBRACE, 1) 
	     device.emit(uinput.KEY_LEFTBRACE, 0)    
	elif character == 'RIGHTBRACE':
	     device.emit(uinput.KEY_RIGHTBRACE, 1) 
	     device.emit(uinput.KEY_RIGHTBRACE, 0)
	elif character == 'ENTER':
	     device.emit(uinput.KEY_ENTER, 1) 
	     device.emit(uinput.KEY_ENTER, 0)     
	elif character == ',':
	     device.emit(uinput.KEY_COMMA, 1) 
	     device.emit(uinput.KEY_COMMA, 0)     
	elif character == '.':
	     device.emit(uinput.KEY_DOT, 1) 
	     device.emit(uinput.KEY_DOT, 0)     
	elif character == '/':
	     device.emit(uinput.KEY_SLASH, 1) 
	     device.emit(uinput.KEY_SLASH, 0)
	elif character == 'RIGHTSHIFT':
	     device.emit(uinput.KEY_RIGHTSHIFT, 1) 
	     device.emit(uinput.KEY_RIGHTSHIFT, 0)
	elif character == 'LEFTALT':
	     device.emit(uinput.KEY_LEFTALT, 1) 
	     device.emit(uinput.KEY_LEFTALT, 0)
	elif character == 'SPACE':
	     device.emit(uinput.KEY_SPACE, 1) 
	     device.emit(uinput.KEY_SPACE, 0)
	elif character == 'CAPSLOCK':
	     device.emit(uinput.KEY_CAPSLOCK, 1) 
	     device.emit(uinput.KEY_CAPSLOCK, 0)
	elif character == 'LEFTCTRL':
	     device.emit(uinput.KEY_LEFTCTRL, 1)
	     device.emit(uinput.KEY_LEFTCTRL,0)
	     print "ctrl clicked" 
	     #device.emit(uinput.KEY_LEFTCTRL, 0)
	     c=get_additional_key()
	     if c == 'V':
	     	os.system("xdotool key Ctrl+V")	     
	     sleep(0.1)	    
	if character == 'LEFTMETA':
	     device.emit(uinput.KEY_LEFTMETA, 1) 
	     device.emit(uinput.KEY_LEFTMETA, 0)  
	if character == 'RIGHTALT':
	     device.emit(uinput.KEY_RIGHTALT, 1) 
	     device.emit(uinput.KEY_RIGHTALT, 0) 
	if character == 'RIGHTCTRL':
	     device.emit(uinput.KEY_RIGHTCTRL, 1) 
	     device.emit(uinput.KEY_RIGHTCTRL, 0) 
	if character == 'LEFT':		
	     device.emit(uinput.KEY_LEFT, 1)
	     print "left arrow" 
	     device.emit(uinput.KEY_LEFT, 0)
	if character == 'DOWN':
	     #sleep(1)
	     device.emit(uinput.KEY_DOWN, 1)
	     print "DOWN arrow" 
	     device.emit(uinput.KEY_DOWN, 0) 
	if character == 'RIGHT':
	     device.emit(uinput.KEY_RIGHT, 1)
	     print "right arrow" 
	     device.emit(uinput.KEY_RIGHT, 0)  
	if character == 'COMMA':
		 device.emit(uinput.KEY_COMMA,1)
		 device.emit(uinput.KEY_COMMA,0)
	if character == 'DOT':
		 device.emit(uinput.KEY_DOT,1)
		 device.emit(uinput.KEY_DOT,0)
	if character == 'DEL':
		 device.emit(uinput.KEY_DELETE,1)
		 device.emit(uinput.KEY_DELETE,0)
	if (character == 'UP'):
		device.emit(uinput.KEY_UP, 1)
		device.emit(uinput.KEY_UP, 0)





events = (
    uinput.REL_X,
    uinput.REL_Y,
    uinput.BTN_LEFT,
    uinput.BTN_RIGHT,uinput.KEY_A,uinput.KEY_B,uinput.KEY_C,uinput.KEY_D,uinput.KEY_E,uinput.KEY_F,uinput.KEY_G,uinput.KEY_H,uinput.KEY_I,uinput.KEY_J,uinput.KEY_K,uinput.KEY_L,uinput.KEY_M,uinput.KEY_N,uinput.KEY_O,uinput.KEY_P,uinput.KEY_Q,uinput.KEY_R,uinput.KEY_S,uinput.KEY_T,uinput.KEY_U,uinput.KEY_V,uinput.KEY_W, uinput.KEY_X, uinput.KEY_Y, uinput.KEY_Z,uinput.KEY_OPEN, uinput.KEY_ESC,
 uinput.KEY_1,
 uinput.KEY_2,
 uinput.KEY_3 ,
 uinput.KEY_4 ,
 uinput.KEY_5 ,
 uinput.KEY_6,
 uinput.KEY_7 ,
 uinput.KEY_8,
 uinput.KEY_9 ,
 uinput.KEY_0 ,
 uinput.KEY_MINUS,
 uinput.KEY_EQUAL,
 uinput.KEY_BACKSPACE,
 uinput.KEY_TAB,
 uinput.KEY_LEFTBRACE ,
 uinput.KEY_RIGHTBRACE,
 uinput.KEY_ENTER,
 uinput.KEY_LEFTCTRL,
 uinput.KEY_COMMA,
 uinput.KEY_DOT,
 uinput.KEY_SLASH,
 uinput.KEY_RIGHTSHIFT,
 uinput.KEY_KPASTERISK,
 uinput.KEY_LEFTALT,
 uinput.KEY_SPACE,
 uinput.KEY_CAPSLOCK,
 uinput.KEY_F1,
 uinput.KEY_F2,
 uinput.KEY_F3,
 uinput.KEY_F4,
 uinput.KEY_F5,
 uinput.KEY_F7,
 uinput.KEY_F8,
 uinput.KEY_F9,
 uinput.KEY_F10,
 uinput.KEY_NUMLOCK,
 uinput.KEY_SCROLLLOCK,
 uinput.KEY_KP7,
 uinput.KEY_KP8,
 uinput.KEY_KP9,
 uinput.KEY_KPMINUS,
 uinput.KEY_KP4,
 uinput.KEY_KP5,
 uinput.KEY_KP6,
 uinput.KEY_KPPLUS,
 uinput.KEY_KP1,
 uinput.KEY_KP2,
 uinput.KEY_KP3,
 uinput.KEY_KP0,
 uinput.KEY_KPDOT,
 uinput.KEY_102ND,
 uinput.KEY_F11,
 uinput.KEY_F12,
 uinput.KEY_KPJPCOMMA,
 uinput.KEY_KPENTER,
 uinput.KEY_RIGHTCTRL,
 uinput.KEY_KPSLASH ,
 uinput.KEY_SYSRQ ,
 uinput.KEY_RIGHTALT ,
 uinput.KEY_LINEFEED ,
 uinput.KEY_HOME ,
 uinput.KEY_UP ,
 uinput.KEY_PAGEUP ,
 uinput.KEY_LEFT ,
 uinput.KEY_RIGHT ,
 uinput.KEY_END ,
 uinput.KEY_DOWN ,
 uinput.KEY_PAGEDOWN ,
 uinput.KEY_INSERT ,
 uinput.KEY_DELETE ,
 uinput.KEY_MACRO ,
 uinput.KEY_MUTE ,
 uinput.KEY_VOLUMEDOWN ,
 uinput.KEY_VOLUMEUP ,
 uinput.KEY_POWER ,
 uinput.KEY_KPEQUAL ,
 uinput.KEY_KPPLUSMINUS ,
 uinput.KEY_PAUSE ,
 uinput.KEY_SCALE ,
 uinput.KEY_KPCOMMA ,
 uinput.KEY_HANGEUL ,
 uinput.KEY_HANJA ,
 uinput.KEY_YEN ,
 uinput.KEY_LEFTMETA ,
 uinput.KEY_RIGHTMETA ,
 uinput.KEY_COMPOSE ,
 uinput.KEY_STOP ,
 uinput.KEY_AGAIN ,
 uinput.KEY_PROPS ,
 uinput.KEY_UNDO ,
 uinput.KEY_FRONT ,
 uinput.KEY_COPY ,
 uinput.KEY_OPEN ,
 uinput.KEY_PASTE ,
 uinput.KEY_FIND ,
 uinput.KEY_CUT ,
 uinput.KEY_HELP ,
 uinput.KEY_MENU ,
 uinput.KEY_CALC ,
 uinput.KEY_SETUP,
 uinput.BTN_LEFT,
 uinput.BTN_RIGHT,
 uinput.ABS_X ,
 uinput.ABS_Y,
 uinput.KEY_SEMICOLON,
)
    
#For mouse clicks
    #device.emit(uinput.BTN_LEFT,1)
    #device.emit(uinput.BTN_LEFT,0)

device = uinput.Device(events)
    



while 1:
	data, address = server_socket.recvfrom(256)
	#print "( " ,address[0], " " , address[1] , " ) said : ", data
	data=string.split(data,"=")
	if data[0]=="M":
		print data[1]
		print data[2]
		device.emit(uinput.REL_X, int(data[1]), syn=False)
		device.emit(uinput.REL_Y, int(data[2]))
	elif data[0]=="C":
		print "clicked"
		device.emit(uinput.BTN_LEFT,1)
		device.emit(uinput.BTN_LEFT,0)
	elif data[0]=="K":
		
		if data[1]==str(1):
			print data[2],type(data[2])
			if data[2]==" ":
				emitCharacter("SPACE")
			elif data[2]=="\n":
				emitCharacter("ENTER")
			else:
				emitCharacter(data[2])
			
		else:
			os.system("xdotool key BackSpace")

	elif data[0]=="R":
		print "Right click"
		device.emit(uinput.BTN_RIGHT,1)
		device.emit(uinput.BTN_RIGHT,0)