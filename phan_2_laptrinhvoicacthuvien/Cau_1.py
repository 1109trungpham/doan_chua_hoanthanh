#Câu 1:

#1.1 Cho x ∈ Rn và A ∈ Rm×n, hãy viết hàm tính tích x. A

import numpy as np
import random

#vector x ngẫu nhiên với 5 phần tử số nguyên
vector_x = np.random.randint(low=-10, high=10, size=3)
#matrix a ngẫu nhiên với 3 hàng 3 cột, số nguyên
matrix_a = np.random.randint(low=-10, high=10, size=(3,3))
matrix_b = np.random.randint(low=-10, high=10, size=(3,3))
#nhân matrix với vector
def nhan_matrix_vector(matrix,vector):
  a = matrix.dot(vector)
  print('kết quả: ',a)

#1.2 Cho A, B ∈ Rm×n, hãy viết hàm tính A°B và AT. B
#Phép nhân Hadamard 2 matrix
def nhan_hadamard(matrix1,matrix2):
  a = np.multiply(matrix1,matrix2)
  print('kết quả: ',a)

#Phép nhân với matrix chuyển vị
def nhan_matrix_chuyenvi(matran1, matran2):
  print('chuyển vị ma trận',matran1)
  matran_chuyenvi = matran1.T
  print('ma trận sau khi chuyển vị: ',matran_chuyenvi)
  a = np.dot(matran_chuyenvi,matran2)
  print('kết quả: ',a)

#1.3 Viết chương trình chính gội các hàm trên
#Chương trình chính
def main():
  nhan_matrix_vector(matrix_a,vector_x)
  nhan_hadamard(matrix_a,matrix_b)
  nhan_matrix_chuyenvi(matrix_a, matrix_b)
if __name__=='__main__':
  main()