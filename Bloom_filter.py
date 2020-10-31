import mmh3
from bitarray import bitarray
BIT_SIZE=500*1024*1024
class BloomFilter:
    def __init__(self):
        bit_array=bitarray(BIT_SIZE)
        bit_array.setall(0)
        self.bit_array=bit_array
    def add(self,url):
        point_list=self.getpostions(url)
        for b in point_list:
            self.bit_array[b]=1
    def get_positions(self,url):
        point1 = mmh3.hash(url, 41) % BIT_SIZE
        point2 = mmh3.hash(url, 42) % BIT_SIZE
        point3 = mmh3.hash(url, 43) % BIT_SIZE
        point4 = mmh3.hash(url, 44) % BIT_SIZE
        point5 = mmh3.hash(url, 45) % BIT_SIZE
        point6 = mmh3.hash(url, 46) % BIT_SIZE
        point7 = mmh3.hash(url, 47) % BIT_SIZE
        return [point1, point2, point3, point4, point5, point6, point7]
    def in_or_not(self,url):
        point_list=self.get_positions(url)
        result=True
        for b in point_list:
            result=result and self.bit_array[b]
        return result
