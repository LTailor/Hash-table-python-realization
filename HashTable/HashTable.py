__author__ = 'Dzhambulat'

class HashTable:

    def __init__(self):
        self.loadFactor=10
        self.elems=[]*100

    def get_hash(self,key):
        k=str(key)
        key_array=[128**i*x for i, x in enumerate(k)]
        hash_value=sum(key_array)

        return hash_value

    def put(self,key,object):

    def get(self,key):
        pass
    def delete(self,key):
        pass

