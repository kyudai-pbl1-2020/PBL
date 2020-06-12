import time
import random

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
        if measure <= min_weight:
            return False
        else:
            return True


def main():
    item = "Water"
    weight = 500 # g
    min_stock = 3
    water_sensor = Sensor( item, weight, min_stock )
    for _ in range( 5 ): # while True:
        measure = random.randrange( 1000, 3000, 1 ) # output from sensor
        print( measure, water_sensor.stockcheck( measure ) )
        time.sleep( 1 )

if __name__ == "__main__":
    main()