words = ["food","was","not","good"]


hidden_State = "Empty Memory"


print("Input Tokens:",words)
print("Initial Hidden_state:",hidden_State)

for index,word in enumerate(words):
	print("TimeStep",index+1)
	print("Current Word:",word)
	print("Previous Memory:",hidden_State)
	
	
	print("---------------------------------------------------------")
	hidden_State = "Memory After Reading " + " " .join(words[:index+1])+ " "
	print("Updated State Will be:",hidden_State)
	print("---------------------------------------------------------")
