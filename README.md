# prog_frog_slog_dog
Learning how to code!

#cool writing effect 
import sys
def typewrite(str):
	import sys
	from time import sleep

	for char in str:
		sleep(0.03)
		sys.stdout.write(char)
		sys.stdout.flush()
