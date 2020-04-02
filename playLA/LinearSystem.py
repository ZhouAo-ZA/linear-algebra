from .Matrix import Matrix
from .Vector import Vector
from ._global import is_zero


class LinearSystem:

    def __init__(self, A, b=None):  # A:系数矩阵   b:右侧结果向量

        assert b is None or A.row_num() == len(b), \
            "row number of a must be equal to the length of b"
        self._m = A.row_num()
        self._n = A.col_num()
        if b is None:
            self.Ab = [A.row_vector(i) for i in range(self._m)]
        if isinstance(b, Vector):
            self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]])
                       for i in range(self._m)]
        if isinstance(b, Matrix):
            self.Ab = [Vector(A.row_vector(i).underlying_list() + b.row_vector(i).underlying_list())
                       for i in range(self._m)]

        # underlying_list = list,便于在向量中添加元素
        self.pivorts = []

    # 选择当前这列元素主元最大的换行
    def _max_row(self, index_i, index_j, n):
        # best=当前主元，ret=具体的行数
        best, ret = self.Ab[index_i][index_j], index_i
        for i in range(index_i + 1, n):
            if self.Ab[i][index_j] > best:
                best, ret = self.Ab[i][index_j], i
        return ret

    def _forward(self):

        i, k = 0, 0
        while i < self._m and k < self._n:
            # 看Ab[i][i]位置是否可以为主元
            max_row = self._max_row(i, k, self._m)
            # 找到了当前主元列最大的元素所在行数，进行换行
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]

            if is_zero(self.Ab[i][k]):
                k += 1
            else:
                # 将主元归为一
                self.Ab[i] = self.Ab[i] / self.Ab[i][k]
                for j in range(i + 1, self._m):
                    self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]
                self.pivorts.append(k)
                i += 1

    def _backward(self):
        n = len(self.pivorts)

        for i in range(n - 1, -1, -1):
            k = self.pivorts[i]
            # Ab[i][k]作为主元
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]

    def gauss_jordan_elimination(self):

        self._forward()
        self._backward()
        for i in range(len(self.pivorts), self._m):
            if not is_zero(self.Ab[i][-1]):
                return False
        return True

    def fancy_print(self):
        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end=" ")
            print("|", self.Ab[i][-1])


def inv(A):
    if A.row_num() != A.col_num():
        return None
    n = A.row_num()
    ls = LinearSystem(A, Matrix.identity(n))
    if not ls.gauss_jordan_elimination():
        return None
    invA = [[row[i] for i in range(n, 2 * n)] for row in ls.Ab]
    return Matrix(invA)

def rank(A):
    ls=LinearSystem(A)
    ls.gauss_jordan_elimination()
    zero = Vector.zero(A.col_num())
    return sum([row != zero for row in ls.Ab])