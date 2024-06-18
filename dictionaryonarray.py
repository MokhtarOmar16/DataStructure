class Pair:
    def __init__(self,key ,value) -> None:
        self.key = key
        self.value = value

class Dictionary:
    def __init__(self) -> None:
        self.dic: list[Pair] = []

    def size(self):
        return len(self.dic)
    
    def update(self, key, value):
        for i in range(self.size()):
            if self.dic[i].key == key :
                self.dic[i].value = value
                return
        raise "Error: not found"
    
    def get(self, key):
        for i in range(self.size()):
            if self.dic[i].key == key :
                return self.dic[i].value
        raise "Error: not found"
    
    def set(self,key ,value):
        try: 
            self.update(key, value)
        except:
            newPair = Pair(key , value)
            self.dic.append(newPair)

    def print(self):
        print(f"[size] {self.size()}")
        print("{")
        for i in range(self.size()):
                print(f"{self.dic[i].key}:{self.dic[i].value}")
        print("}")
    
    def remove(self, key):
        for i in range(self.size()):
            if self.dic[i].key == key:
                self.dic.pop(i)
                return
        raise "Error: Nou Found"
            
