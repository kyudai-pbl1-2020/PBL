import os

def processCurrentWeight(scaleWeight,itemName):
    #Get the minimum weight for this item from the data file
    filepath = os.path.join(os.getcwd(),'testdata.txt')
    minimum_weight = None

    with open(filepath) as file:
        data = file.read()
        data = data.split("\n")
        for item in data:
            if itemName in item:
                (name,weight,status) = item.split("/")
                minimum_weight = weight

    if scaleWeight < minimum_weight:
        #send notification to User through the UI to notify that the number of item is low
        #notifyUser(itemName)
        pass

def orderFromAmazon(item):
    #logic to order from amazon..
    pass

