
def FilterX(Task,Elements):
	Result = list()
	for no in Elements:
		Ret = Task(no)	#call to cheak Evevn
		if(Ret):
			Result.append(no)
			
	return Result
	
def MapX(Task,Elements):
	Result = list()
	
	for no in Elements:
		Ret = Task(no)
		Result.append(Ret)
		
def ReduceX(Task,Elements):

	Sum = 0
	
	for no in Elements:
		
		Sum = Task(Sum,no)
		
	return Sum
