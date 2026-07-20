def Display():
	print("Jay Ganesh...",datetime.datetime.now())
	
	
def main():
	print("Automitation script started")
	schedule.every(1).do.minute(Display)
	
	while(True):
		schedule.run_pending()
		time.sleep(1)
		
	print("End of automitation script")

if __name__ == "__main__":
	main()
	
