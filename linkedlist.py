class ObjList:
    def __init__(self, data: str):
        self.__next = None
        self.__prev = None
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, self.__class__) or obj is None:
            self.__next = obj
        else:
            raise AttributeError

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        if isinstance(obj, self.__class__) or obj is None:
            self.__prev = obj
        else:
            raise AttributeError

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data


class LinkedList:
    def __init__(self):
        self.head: ObjList | None = None
        self.tail: ObjList | None = None

    def add_obj(self, obj: ObjList) -> None:
        if self.tail is None:
            self.tail = obj
            self.head = obj
        else:
            obj.prev = self.tail
            self.tail.next = obj
            self.tail = obj

    def remove_obj(self) -> None:
        if self.tail is not None:
            self.tail = self.tail.prev
            self.tail.next = None

    def get_data(self) -> list[str]:
        lst = []
        next_obj = self.head
        while next_obj:
            lst.append(next_obj.data)
            next_obj = next_obj.next
        return lst
