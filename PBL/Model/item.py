
class Item:


    def __init__(self,name,weight,status,amazon_url,imgPath):
        """
        :param name: Name of the item
        :param quantity: How many items need to be ordered
        :param status: Status of the order
                        - InStock: There are enough of this item in stock
                        - Ordered: More items have been ordered
                        - Low: There is not enough of this item in stock currently
                        - Disabled: The User deactivated the system for this order
        """
        self.name = name
        self.weight = weight
        self.status = status #InStock, Ordered, Low, Disabled
        self.amazon_url = amazon_url
        self.imgPath = imgPath