class Sensor:
    """
    センサーの測定結果から商品の在庫が少なくなってきたことを検知する
    商品の在庫が少なくなったとき商品をオーダーする
    """
    def __init__(self, item, weight, min_stock ):
        """
        :param name: Name of the item
        :param weight: the item's unit weight
        :param min_stock: it orders the item when the stock < min_stock
        """
        self.item = item
        self.weight = weight
        self.min_stock = min_stock
        pass
    
    def stockcheck( self, measure ):
        """
        :param measure: output from sensor
        """
        min_weight = self.weight * self.min_stock
        if measure < min_weight:
            Order()


