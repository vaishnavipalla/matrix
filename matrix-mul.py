import numpy
def mat_multiply(A,B):
	c={}
	print("Matrix C is")
	for i in range(m1):
		for j in range(n2):
			c[i,j]=0
			for k in range(n1):
				c[i,j]+=(A[i,k]*B[k,j])
			print(c[i,j]),'\t',
		print('\n')
m1=input("No.of rows in matrix1:")
n1=input("No.of columns in matrix1:")
print("Enter matrix A")
A=numpy.empty((m1,n1))
for i in range(m1):
	for j in range(n1):
		A[i,j]=input("")
print("Matrix A is")
for i in range(m1):
	for j in range(n1):
		print(A[i,j]),'\t',
	print
print('\n')
m2=input("No.of rows in matrix2:")
n2=input("No.of columns in matrix2:")
B=numpy.empty((m2,n2))
print("Enter matrix B")
for i in range(m2):
	for j in range(n2):
		B[i,j]=input("")
print("Matrix B is")
for i in range(m2):
	for j in range(n2):
		print(B[i,j]),'\t',
	print
print('\n')
mat_multiply(A,B)
