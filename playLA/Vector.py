import math
from ._global import is_zero


class Vector:

    def __init__(self,lst):
        self._values = list(lst)


    # 返回一个dim维的零向量
    @classmethod
    def zero(cls,dim):
        return cls([0]*dim)

    #返回向量的底层列表
    def underlying_list(self):
        return self._values[:]

    #向量点乘，返回结果标量
    def dot(self,another):
        assert len(self)==len(another),\
            "error in dot product.lenth of vectors must be same."
        return sum(a*b for a,b in zip(self,another))

    # 返回一个向量的模
    def norm(self):
        return math.sqrt(sum(e**2 for e in self))

    # 返回向量的单位向量
    def normalize(self):
        # return Vector([e / self.norm() for e in self])
        #return 1 / self.norm()*Vector(self._values)
        if is_zero(self.norm()):
            raise ZeroDivisionError("normalize error,norm is zero")
        return Vector(self._values)/self.norm()

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    # 向量减法，返回结果向量
    def __sub__(self, other):
        assert len(self)==len(other),\
            "error in subtracting,length of vectors must be same."
        return Vector([a-b for a,b in zip(self,other)])

    # 返回数量乘法的结果向量，self*other
    def __mul__(self, other):
        return Vector([other*e for e in self])

    # 返回结果取正的结果向量
    def __pos__(self):
        return 1*self

    # 返回结果取负

    def __neg__(self):
        return -1*self

    # 返回数量乘法的结果向量：k * self
    def __rmul__(self, other):
        return self*other

    # 向量数量除法  self/k

    def __truediv__(self, k):
        return (1/k)*self

    # 向量加法
    def __add__(self, another):
        assert len(self)==len(another),\
            "error in adding,length of vectors must be same."
        return Vector([a+b for a,b in zip(self, another)])

    # 迭代器
    def __iter__(self):
        return self._values.__iter__()