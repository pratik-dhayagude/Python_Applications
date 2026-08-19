import pandas as pd
from sklearn.linear_model import LinearRegression,LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib 
from sklearn.metrics import accuracy_score,confusion_matrix



#Step1 :Load The Data

#------------------------------------------------------------------------------
#   Function Name:LoadData
#   Description :Load the Data from CSV
#   Input: Name of CSV File
#   Output: Data Frame
#   Author: Pratik Narule
#   Date:16/08/2026
#------------------------------------------------------------------------------

def LoadData(filename):
    df=pd.read_csv(filename)

    print("DataSet Loaded Sucessfully")
    print(df.head())


#------------------------------------------------------------------------------
#   Function Name:main
#   Description :Entry point function
#   Input: Name of CSV File
#   Output: Data Frame
#   Author: Pratik Narule
#   Date:16/08/2026
#------------------------------------------------------------------------------
def main():
    LoadData("MarvellousTitanicDataset.csv")

if __name__=="__main__":
    main()