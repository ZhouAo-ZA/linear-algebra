from playLA.Vector import Vector


class Matrix:

    def __init__(self,list2d):
        self._values=[row[:] for row in list2d]

    #返回一个r行c列的零矩阵
    @classmethod
    def zero(cls,r,c):
        return cls([[0]* c for _ in range(r)])

    #返回一个n行n列的单位矩阵
    @classmethod
    def identity(cls,n):
        m=[[0]*n for _ in range(n)]
        for i in range(n):
            m[i][i]=1
        return cls(m)

    #返回矩阵的元素个数
    def size(self):
        r,c=self.shape()
        return r*c

    #返回矩阵的行数
    def row_num(self):
        return self.shape()[0]

    #返回矩阵第index个行向量
    def row_vector(self,index):
        return Vector(self._values[index])


    #矩阵加法,返回结果
    def __add__(self, other):
        assert self.shape()==other.shape(), \
            "error in adding,shape of matrix must be same"
        return Matrix([[a+b for a,b in zip(self.row_vector(i),other.row_vector(i))]
                      for i in range(self.row_num())])

    # 矩阵减法,返回结果
    def __sub__(self, other):
        assert self.shape() == other.shape(), \
                "error in subtracting,shape of matrix must be same"
        return Matrix([[a - b for a, b in zip(self.row_vector(i), other.row_vector(i))]
                       for i in range(self.row_num())])

    #返回矩阵的数量乘结果：self*k
    def __mul__(self, k):
        return Matrix([[a*k for a in self.row_vector(i)]for i in range(self.row_num())])

    # 返回矩阵的数量乘结果：k*self
    def __rmul__(self, other):
        return self.__mul__(other)

    #返回矩阵的数量除法：self/k
    def __truediv__(self, other):
        return (1/other)*self

    #返回矩阵取正的结果
    def __pos__(self):
        return 1*self

    #返回矩阵取负的结果
    def __neg__(self):
        return -1*self

    #返回矩阵的乘法的结果
    def dot(self,another):
        if isinstance(another,Vector):
            #矩阵和向量的乘法
            assert self.col_num()==len(another),\
                "error in matrix vector multiplication."
            return Vector([self.row_vector(i).dot(another) for i in range(self.row_num())])
        if isinstance(another,Matrix):
            #矩阵和矩阵的乘法
            assert self.col_num()==another.row_num(),\
                "error in matrix matrix multiplication"
            #return Matrix([[self.dot(another.col_vector(i))]for i in range(another.col_num())])
            return Matrix([[self.row_vector(i).dot(another.col_vector(j))for j in range(another.col_num())]
                           for i in range(self.row_num())])


    #返回矩阵的转置
    def T(self):
        return Matrix([[e for e in self.col_vector(i)]for i in range(self.col_num())])
    #返回矩阵第index个列向量
    def col_vector(self,index):
        return Vector([row[index]for row in self._values])

    __len__ = row_num

    #返回矩阵pos位置的元素
    def __getitem__(self, pos):
        r,c=pos
        return self._values[r][c]

    #返回矩阵的列数
    def col_num(self):
        return self.shape()[1]

    #返回矩阵的形状（行数，列数）
    def shape(self):
        return len(self._values),len(self._values[0])
    def __repr__(self):
        return "Matrix({})".format(self._values)

    __str__=__repr__