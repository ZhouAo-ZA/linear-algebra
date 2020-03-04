import numpy as np

if __name__=="__main__":
    #矩阵的创建
    A=np.array([[1,2],[3,4]])
    print(A)

    #矩阵的属性
    print(A.shape)
    print(A.T)

    print(A[1,1])
    print(A[0])
    print(A[:,0])
    print(A[1,:])



    #单位矩阵
    I=np.identity(2)
    print(I)

    #逆矩阵
    invA=np.linalg.inv(A)
    print(invA)
    print(invA.dot(A))


    