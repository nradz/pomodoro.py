#!/usr/bin/python3

import argparse, time, os

def main():

	parser = argparse.ArgumentParser(description="Set parameters.")
	parser.add_argument("-p", help="Duration of a 'pomodoro'", 
		type=int, default=25)
	parser.add_argument("-b", help="Duration of a simple break",
	 	type=int, default=5)
	parser.add_argument("-lb", help="Duration of the long break",
		type=int, default=20)
	parser.add_argument("-t", help="Pomodoro times until a long break",
		type=int, default=4)
	args = parser.parse_args()

	while True:
		for x in range(args.t):
			print("Working!")
			countdown(args.p)
			beep()
			print("Resting!")
			if x != (args.t-1):
				countdown(args.r)
			else:
				countdown(args.lr)
			beep()
			input("Again?(press enter):")


def countdown(min):
	count = min * 60
	while count > 0:
		print("%i:%i  " % (count//60, count%60), end="\r")
		count -= 1
		time.sleep(1)

	
def beep():
	os.system("beep -f 1000 -r 2 && sleep 0.5 && beep -f 1000 -r 2")






if __name__=="__main__":
	try:
		main()
	except KeyboardInterrupt:
		pass
