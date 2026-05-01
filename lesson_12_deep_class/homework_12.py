class Safe:

    def __init__(self, password):
        self.__password = password
        self.__items = []
        self._max = 5
        self.__locked = True
    
    def __str__(self):
        status = "locked" if self.__locked else "unlocked"
        return f"Safe with {len(self.__items)}/{self._max} items ({status})"
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return len(self.__items)

    def __contains__(self, item):
        return item in self.__items
    
    def __getitem__(self, index):
        return self.__items[index]

    def __setitem__(self, index, value):
        if self.__locked:
            raise PermissionError("Cannot add item. Safe is locked.")
        
        if len(self.__items) >= self._max:
            raise OverflowError(f"Safe is full. Maximum {self._max} items allowed")
        self.__items.append(value)

        if index < 0:
            raise IndexError("Negative index not allowed")
        
        self.__items[index] = value

    def unlock(self, password):
        if password == self.__password:
            self.__locked = False
            print("Safe unlocked")
        else:
            raise ValueError("Wrong password")

    def lock(self):
        self.__locked = True
        print("Safe locked")

safe = Safe("1234")

try:
    safe.unlock("1111")  # невірний пароль
except ValueError as e:
    print(e)

safe.unlock("1234")

safe[0] = "gold"
safe[1] = "documents"
safe[2] = None
safe[3] = 1234
safe[4] = ["test"]

print(safe)
print("gold" in safe)
print("documents" in safe)
print("platinum" in safe)
print("silver" in safe)
print("diamonds" in safe)

print(len(safe))

try:
    for i in range(5):
        safe[i] = f"item_{i}"
except Exception as e:
    print("Error:", e)

safe.lock()

try:
    safe[0] = "diamonds"  # сейф закрито
except Exception as e:
    print("Error:", e)