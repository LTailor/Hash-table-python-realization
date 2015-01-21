__author__ = 'Dzhambulat'


class HashTable:

    class Node:
        def __init__(self,key,object):
            self.key=key
            self.object=object

    def __init__(self):

        self.length=100
        self.elems=[[] for i in range(self.length)]
        self.loadFactor=10

    def get_hash(self,key):
        k=str(key)
        key_array=[128**i*int(ord(x)) for i, x in enumerate(k)]
        hash_value=sum(key_array)

        return hash_value%self.length

    def put(self,key,object):
        if self.get(key)!=None:
            return False
        node=HashTable.Node(key,object)
        key=self.get_hash(key)
        self.elems[key].append(node)
        return True

    def find_by_key(self,elems,key):
        if len(elems)!=0:
            for node in elems:
                if node.key==key:
                    return node
        return None

    def get(self,key):
        index=self.get_hash(key)
        elems=self.elems[index]

        node= self.find_by_key(elems,key)
        if node!=None:
            return node.object
        return None

    def delete(self,key):
        index=self.get_hash(key)
        elems=self.elems[index]

        node=self.find_by_key(elems,key)
        if node!=None:
            elems.remove(node)



ht=HashTable()
ht.put("one",1)
ht.put("two",2)
assert ht.get("one")==1
ht.delete("one")
assert ht.get("one")==None