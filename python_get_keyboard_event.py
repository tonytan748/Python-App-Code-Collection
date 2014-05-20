#-*-coding:utf-8-*-
import pythoncom
import pyHook

def onMonseEvent(event):
	'''get mouse event'''
	print 'MessageName:',event.MessageName
	print 'Message:',event.Message
	print 'Time:',event.Time
	print 'Window:',event.Window
	print 'WindowName:',event.WindowName
	print 'Position:',event.Positon
	print 'Wheel:',event.Wheel
	print 'Injected:',event.Injected
	print '---'

	return True

def onKeyboardEvent(event):
	'''get keyboard event'''
	print 'MessageName',event.MessageName
	print 'Message',event.Message
	print 'Time:',event.Time
	print 'Window:',event.Window
	print 'WindowName',event.WindowName
	print 'Ascii:',event.Ascii,chr(event.Ascii)
	print 'Key:',event.Key
	print 'KeyID:',event.KeyID
	print 'ScanCode:',event.ScanCode
	print 'ScanCode:',event.Extended
	print 'Injected:',event.Injected
	print 'Alt',event.Alt
	print 'Transition',event.Transition
	print '---'
	return True

def main():
	'''create a management'''
	hm=pyHook.HookManager()
	'''monitor keyboard event'''
	hm.KeyDown=onKeyboardEvent
	'''set keyboard hook'''
	hm.HookKeyboard()
	'''monitor mouse event'''
	hm.MouseAll=onMouseEvent
	'''set mouse hook'''
	hm.HookMouse()
	'''go into loop, cannot stop if close by menul'''
	pythoncom.PumpMessages()

if __name__=='__main__':
	main()
