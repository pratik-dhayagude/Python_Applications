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
#   Author: Pratik Dhananjay Dhayagude
#   Date:16/08/2026
#------------------------------------------------------------------------------

def LoadData(filename):
    df=pd.read_csv(filename)

    print("DataSet Loaded Sucessfully")
    print(df.head())
    return df



#Step 2: Data Preprocessing
#------------------------------------------------------------------------------
#   Function Name:PreProcess
#   Description :It Performs  Data Analysis
#   Input: Data Frame
#   Output: Updated DataFrame
#   Author: Pratik Dhananjay Dhayagude
#   Date:16/08/2026
#------------------------------------------------------------------------------

def PreprocessData(df):
    df=df.drop([
        "Passengerid",
        "zero",
    ],
    errors="ignore"
    )  
 

    # Handle Missing Values
    df["Age"]=df["Age"].fillna(df["Age"].median())
    df["Fare"]=df["Fare"].fillna(df["Fare"].median())
    df["Embarked"]=df["Embarked"].fillna(df["Embarked"].median())

    #Convert Categorical to Numeric Data
    df=pd.get_dummies(
        df,
        columns=["Embarked"],
        drop_first=True,
        dtype=int
    )

    print(df.head())

    print("Data Preprocessing is Completed")

    
    return df

#------------------------------------------------------------------------------
#   Function Name:main
#   Description :Entry point function
#   Input: Name of CSV File
#   Output: Data Frame
#   Author: Pratik Dhananjay Dhayagude
#   Date:16/08/2026
#------------------------------------------------------------------------------

def main():
    #Step  1
    df=LoadData("MarvellousTitanicDataset.csv")
    #Step2
    df=PreprocessData(df)
if __name__=="__main__":
    main()
