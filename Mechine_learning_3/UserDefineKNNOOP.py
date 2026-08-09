import math
class Point:
    def __init__(self, Point, X, Y, Label):
        self.Point = Point
        self.X = X
        self.Y = Y
        self.Label = Label
        self.Distance = 0

    def EuclideanDistance(self, OtherPoint):
        self.Distance = math.sqrt(
            (self.X - OtherPoint.X) ** 2 +
            (self.Y - OtherPoint.Y) ** 2
        )

        return self.Distance

    def Display(self):
        print(
            "Point:", self.Point,
            "X:", self.X,
            "Y:", self.Y,
            "Label:", self.Label,
            "Distance:", self.Distance
        )


class KNNClassifier:

    def __init__(self):
        self.Data = [
            	{"Point":"A","X":1,"Y":2,"Label":"Red"},
                {"Point":"B","X":2,"Y":3,"Label":"Red"},
                {"Point":"C","X":3,"Y":1,"Label":"Blue"},
                {"Point":"D","X":5,"Y":6,"Label":"Blue"},
                {"Point":"E","X":6,"Y":6,"Label":"Blue"},
                {"Point":"F","X":3,"Y":4,"Label":"Red"},
                {"Point":"G","X":3,"Y":2,"Label":"Red"}
    ]

    def DisplayData(self):

        for point in self.Data:
            point.Display()

    def CalculateDistances(self, NewPoint):

        for point in self.Data:
            point.EuclideanDistance(NewPoint)

    def SortData(self):

        self.Data = sorted(
            self.Data,
            key=lambda point: point.Distance
        )

    def GetNearestNeighbours(self, K):

        return self.Data[:K]

    def Voting(self, Neighbours):

        Votes = {}

        for point in Neighbours:

            Label = point.Label

            Votes[Label] = Votes.get(Label, 0) + 1

        return Votes

    def Predict(self, Votes):

        MaxVotes = 0
        Prediction = ""

        for Label in Votes:

            if Votes[Label] > MaxVotes:
                MaxVotes = Votes[Label]
                Prediction = Label

        return Prediction


def main():

    Border = "-" * 30

    print(Border)
    print("Marvellous KNN Classifier")
    print(Border)

    Classifier = KNNClassifier()

    print("Training Data:")
    Classifier.DisplayData()

    NewPoint = Point("New", 3, 3, "Unknown")

    print(Border)
    print("Calculating Distances")

    Classifier.CalculateDistances(NewPoint)

    Classifier.DisplayData()

    Classifier.SortData()

    print(Border)
    print("Sorted Data:")

    Classifier.DisplayData()

    K = 3

    Neighbours = Classifier.GetNearestNeighbours(K)

    print(Border)
    print("Nearest 3 Neighbours:")

    for point in Neighbours:
        point.Display()

    Votes = Classifier.Voting(Neighbours)

    print(Border)
    print("Voting Result:")

    for Label in Votes:
        print("Name:", Label, "Number of votes:", Votes[Label])

    Prediction = Classifier.Predict(Votes)

    print(Border)
    print("Final Prediction is:", Prediction)


if __name__ == "__main__":
    main()