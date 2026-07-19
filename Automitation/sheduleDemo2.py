def Display():
	print("Jay Ganesh...",datetime.datetime.now())
	
	
def main():
	print("Automitation script started")
	schedule.every(1).do.minute(Display)
	
	#issue

if __name__ == "__main__":
	main()
	
