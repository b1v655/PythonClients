import msvcrt
import time
import sys
def is_ascii(s):
    return all(ord(c) < 128 for c in s)
def readInput(timeout = 1):
        start_time = time.time()
	input = ''
	while True:
		if msvcrt.kbhit():
                        sys.stdout.write('\r')
                        sys.stdout.write(input)
                        sys.stdout.write(' ')
                        sys.stdout.write('\r')
                        sys.stdout.write(input) 
			chr = msvcrt.getche()
			if ord(chr) == 13: # enter_key
				break
			elif ord(chr) >= 32: #space_char
				input += chr
                                sys.stdout.write('\r')
                                sys.stdout.write(input)
                                sys.stdout.write(' ')
                                sys.stdout.write('\r')
                                sys.stdout.write(input)
			elif ord(chr) == 8: #backspace_char
				input = input[:-1]
                                sys.stdout.write('\r')
                                sys.stdout.write(input)
                                sys.stdout.write(' ')
                                sys.stdout.write('\r')
                                sys.stdout.write(input)               
		if len(input) == 0 and (time.time() - start_time) > timeout:
			break

	#print ''  # needed to move to next line
	if len(input) > 0:
		return input
	else:
		return ''
