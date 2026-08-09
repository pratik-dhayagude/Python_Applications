import pandas as pd
	
def main():
	Data = {
	
		"Name" : ["Sagar","Amit","Pooja"],
		"Age":[27,28,29],
		"City" :["Pune","Kolapur","Satara"]
	}
	
	dobj = pd.DataFrame(Data)
	
	print(dobj)
	# Not allowed
	
	#print(dobj[0])
	
	
	print(dobj["Age"])
if __name__ == "__main__":
	main()
