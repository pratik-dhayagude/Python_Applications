import psutil
import sys
import os
import time
import schedule
import smtplib
from email.message import EmailMessage

sender_mail = "mail"
Password = "Pass"

def send_mail(reciver,filename,data):
	msg = EmailMessage()
	msg["From"] = sender_mail
	msg["To"] = reciver
	msg["Subject"] = "System_Report"
	
	body = f"""
	System Report Summary
	
	RAM
	HDD 
	CPU
	NETWORK USAGE
	
	Please cheak they attch log file 
	"""
	
	msg.set_content(body)
	
	fobj = open(filename,"rb")
	
	filedata = fobj.read()
	
	msg.add_attachment(filedata,
						maintype ="Application",
						subtype = "octet-stream",
						filename = os.path.basename(filename)
						)

	smpt = smtplib.SMTP_SSL("smtp.gmail.com",465)	


	smpt.login(sender_mail,Password)

	print("Receiver Email:",reciver)
	print("Message To:", msg["To"])

	smpt.send_message(msg)
		
    	
	smpt.quit()

	print("Email sent")

	fobj.close()
	


def ProcessScan():
	############# Process Information ##############################
	ListProcess = []
	for proc in psutil.process_iter():
		info = proc.as_dict(attrs = ["pid","name","username","status"])
		info["cpu_percent"] = proc.cpu_percent(None)
		info["Memory_percent"] = proc.memory_percent()
		
		ListProcess.append(info)
		
	return ListProcess
		
		
def PlatForm_Survillance(FolderName,ReciverEmail):
	
	Border = "-"*50
	Ret = False
	
	
	Ret = os.path.exists(FolderName)
	
	if Ret == True:
		Ret = os.path.isdir(FolderName)
		if Ret == False:
			print("Name is here but there is no such existing directory")
			return
			
	else:
		os.mkdir(FolderName)
		print("Directory for the log file gets created successfully")
		
	#################################################################################
	
	timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
	FileName = os.path.join(FolderName,"Marvellous_%s.log"%timeStamp)
	fobj = open(FileName,"w")

	print(f"Log file gets successfully created with name {FileName}")
	fobj.write(Border+"\n")
	fobj.write("Marvellous Platform survillance\n")
	fobj.write("LogFile gets created as:"+timeStamp+"\n")
	fobj.write(Border+"\n\n")
	########################################################################
	fobj.write("----System report----\n")
	
	############### CPU Information ##############################
	fobj.write("Number of active CpuCore:%s \n"%psutil.cpu_count())	
	fobj.write("CPU percentage:%s %%\n"%psutil.cpu_percent())
	fobj.write(Border+"\n")
	
	################# RAM Information ###############################
	Memory = psutil.virtual_memory()
	fobj.write("RAM Usage:%s %%\n"% Memory.percent)
	fobj.write("Total RAM avalible:%s\n"% Memory.total)
	fobj.write(Border+"\n")
	
	############# NetWork Usage #####################################
	netobj = psutil.net_io_counters()
	fobj.write("NetWork Usage Report:\n")
	fobj.write("Sent: %.2f MB\n"%(netobj.bytes_sent /(1024 *1024)))
	fobj.write("recive: %.2f MB\n"%(netobj.bytes_recv /(1024 *1024)))
	fobj.write(Border+"\n")
	
	########### Process Information ##################################
	data = ProcessScan()
	for info in data:
		#fobj.write(f"{info}\n") 
		fobj.write("PID:%s\n"%info.get("pid"))
		fobj.write("Name:%s\n"%info.get("name"))
		fobj.write("UserName:%s\n"%info.get("username"))
		fobj.write("status:%s\n"%info.get("status"))
		fobj.write("CPU Percentage:%s\n"%info.get("cpu_percent"))
		fobj.write("MemoryPercentage:%s\n"%info.get("Memory_percent"))
		fobj.write(Border+"\n")
		
		

	fobj.write("\n"*15)
	fobj.write(Border+"\n")
	
	fobj.write(Border+"\n")
	fobj.write("----End of log file----")
	fobj.write(Border+"\n\n")
	
	fobj.close()
	
	send_mail(ReciverEmail,FileName,data)

	
	

def main():	
	
	Border = "-"*50
	print(Border)
	print(".....Marvellous Platform Servilance System.....")
	print(Border)
	
	if(len(sys.argv) == 2):
		if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
			print("This automitation script is use to perform")
			print("1:It fetch they information of running process")
			print("2:It fetch information about Primary Storage ram")
			print("3:It fetch Information about Secondary Storage HDD")
			print("4:It fetch information about CPU")
			print("5:It gets Auto schedule periodically")
			print("6:It mentaion all records into log file")
			print("7:It sends they log file through mail periodically")
		elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
			print("Use they Automitation script as :")
			print(f"python {sys.argv[0]} Time_Interval Folder_Name ")
			print("Time_Interval : Time in minutes for periodic excution")
			print("Folder_Name : Name of folder")
		else:
			print("Unable to proced as there is no matching arguments")
			print("Please use --h and --u flag for getting more details")
		
	elif(len(sys.argv) == 3):
		#print("CPU usage:",psutil.cpu_percent())
		print("Schedular started successfully")
		print("Press ctrl + c to abort they Automitation Script")
		schedule.every(int(sys.argv[1])).minutes.do(PlatForm_Survillance,sys.argv[2])
		while(1):
			schedule.run_pending()
			time.sleep(1)
			
	elif(len(sys.argv) == 4):
		time_Schedular = sys.argv[1]
		foldername = sys.argv[2]
		ReciverEmail = sys.argv[3]
		
		#schedular
		schedule.every(int(time_Schedular)).seconds.do(PlatForm_Survillance,foldername ,ReciverEmail)
		while(1):
			schedule.run_pending()
			time.sleep(1)
			
	else:
		print("Invalid Arguments")
		print("Unable to proced as arguments are not matching")
		print("Please use --h and --u flag for getting more details")
		
		
	
	print(Border)
	print("Thanku For using Marvellous Servilance system")
	print(Border)

if __name__ == "__main__":
	main()
