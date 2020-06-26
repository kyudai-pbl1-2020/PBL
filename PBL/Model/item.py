
class Item:


    def __init__(self,name,weight,unit_price,quantity,status,amazon_url,imgPath):
        """
        :param name: Name of the item
        :param weight: Weight threshold for the item. Under this weight, new items must be ordered
        :param status: Status of the order
                        - Active: This item is on the the scale. The weight is being measured
                        - Inactive: Another item is on the scale. The weight is not being measured
        :param amazon_url: Amazon url of the product page
        :param imgPath: Path on the client machine where the picture of the item is stored
        """
        self.name = name
        self.weight = weight
        self.unit_price = unit_price
        self.quantity = quantity
        self.status = status #Active,Inactive
        self.amazon_url = amazon_url
        self.imgPath = imgPath


    #Format used to write in the csv file
    def fileData(self):
        headers = ['name','weight','unit_price','quantity','status','amazon_url','img']
        data = [self.name,self.weight,self.unit_price,self.quantity,self.status,self.amazon_url,self.imgPath]

        headers_data = {}
        headers_data['headers'] = headers
        headers_data['data'] = data
        return headers_data