'''
python bitwise operators works only on integers
The integers are first converted into binary and then operations are performed on bit by bit,
 hence the name bitwise operators. Then the result is returned in decimal format.

'''



class Bitwise():
    def __init__(self, value):
        self.value = value

    def __and__(self, obj):
        print("And operator overloaded")
        if isinstance(obj, Bitwise):
            return self.value & obj.value
        else:
            raise ValueError("Must be a object of class")

    def __or__(self, obj):
        print("Or operator overloaded")
        if isinstance(obj, Bitwise):
            return self.value | obj.value
        else:
            raise ValueError("Must be a object of class")

    def __xor__(self, obj):
        print("Xor operator overloaded")
        if isinstance(obj, Bitwise):
            return self.value ^ obj.value
        else:
            raise ValueError("Must be a object of class")

    def __lshift__(self, obj):
        print("lshift operator overloaded")
        if isinstance(obj, Bitwise):
            return self.value << obj.value
        else:
            raise ValueError("Must be a object of class")

    def __rshift__(self, obj):
        print("rshift operator overloaded")
        if isinstance(obj, Bitwise):
            return self.value & obj.value
        else:
            raise ValueError("Must be a object of class")

    def __invert__(self):
        print("Invert operator overloaded")
        return ~self.value




if __name__ == "__main__":
    a = Bitwise(10)
    b = Bitwise(12)
    print(a & b)
    print(a | b)
    print(a ^ b)
    print(a << b)
    print(a >> b)
    print(~a)