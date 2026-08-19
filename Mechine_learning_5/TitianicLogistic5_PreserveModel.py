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
    return df



#Step 2: Data Preprocessing
#------------------------------------------------------------------------------
#   Function Name:PreProcess
#   Description :It Performs  Data Analysis
#   Input: Data Frame
#   Output: Updated DataFrame
#   Author: Pratik Narule
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



#Step 3:Spilt Data
#------------------------------------------------------------------------------
#   Function Name:SplitData
#   Description :It Performs  Spilting Activity
#   Input: Dataframe
#   Output: 4 Subset for training and testing 
#   Author: Pratik Narule
#   Date:16/08/2026
#------------------------------------------------------------------------------

def SplitData(df):
    X=df.drop("Survived",axis=1)
    Y=df["Survived"]
    X_Train,X_Test,Y_Train,y_test=train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42

    )
    print("Data set Spilting Completed Sucessfully")

    return X_Train,X_Test, Y_Train,y_test





#Step 4:Train Model
#-----------------------------------------------------------------------------
#   Function Name:TrainModel
#   Description :It Perform model Training
#   Input: Training Features and Labels
#   Output: Trained the model 
#   Author: Pratik Narule
#   Date:16/08/2026
#------------------------------------------------------------------------------
def TrainModel(X_Train,Y_Train):
    model=LogisticRegression(max_iter=1000)
    model= model.fit(X_Train,Y_Train)
    print("Model Trained SucessFully")

    return model




#Step 5:Evaluate Model
#-----------------------------------------------------------------------------
#   Function Name:EvaluateModel
#   Description :It Performs Model Testing
#   Input: model,testing Data(features ,labels)
#   Output: None
#   Author: Pratik Narule
#   Date:16/08/2026
#------------------------------------------------------------------------------

def EvaluateModel(model,X_Test,Y_Test):
    Y_Pred=model.predict(X_Test)
    accuracy= accuracy_score(Y_Test,Y_Pred)

    print("Accuarcy is :",accuracy)

    print(confusion_matrix(Y_Test,Y_Pred))


#Step 6:Perserve Model
#-----------------------------------------------------------------------------
#   Function Name:PreserveModel
#   Description :It Perform Model Preservation
#   Input: model,testing Data(features ,labels)
#   Output: None
#   Author: Pratik Narule
#   Date:16/08/2026
#------------------------------------------------------------------------------

def PreserveModel(model,filename):
    joblib.dump(model,filename)

    print("Model Preseved with name :",filename)



#------------------------------------------------------------------------------
#   Function Name:main
#   Description :Entry point function
#   Input: Name of CSV File
#   Output: Data Frame
#   Author: Pratik Narule
#   Date:16/08/2026
#------------------------------------------------------------------------------

def main():
    #Step  1
    df=LoadData("MarvellousTitanicDataset.csv")
    #Step2
    df=PreprocessData(df)

    #Step 3
    X_Train,X_Test, Y_Train,y_test=SplitData(df)

    #Step4
    model=TrainModel(X_Train,Y_Train)

    #Step5
    EvaluateModel(model,X_Test,y_test)

    #Step 6
    PreserveModel(model,"MarvellousTitanic.pkl")



if __name__=="__main__":
    main()