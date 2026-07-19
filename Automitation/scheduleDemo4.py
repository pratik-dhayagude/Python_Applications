import schedule
import datetime 
import time
import os
def Display():
	print("Jay Ganesh...",datetime.datetime.now())
	
	
def main():
	print("Automitation script started")
	schedule.every(10).seconds.do(Display)
	
	while(True):
		schedule.run_pending()
		time.sleep(1)
		
	print("End of automitation script")

if __name__ == "__main__":
	main()
	
