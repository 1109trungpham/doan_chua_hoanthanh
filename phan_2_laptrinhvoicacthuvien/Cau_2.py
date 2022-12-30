#Câu 2:
from sympy import symbols, Eq, solve, pi
from sympy import *

#2.1 Viết hàm giải hệ phương trình
x,y,z = symbols('x y z')
pt1 = Eq(2*x - 5*y + z + 5,0)
pt2 = Eq(4*x + 2*y -2*z - 2,0)
pt3 = Eq(x + y  - z,0)
ketqua = solve((pt1,pt2,pt3),(x,y,z))
print(ketqua)

#2.2 Viết hàm tính giới hạn
x = symbols('x')
b = (x**3-3*x**2)**(1/3) + (x**2-2*x)**(1/2)
gioihan = limit(b,x,oo)
print(gioihan)

#2.3 Viết hàm tính đạo hàm
x = symbols('x')
c = (2*x-1)/(x+2)
daoham = diff(c,x)
print(daoham)

#2.4 Viết hàm tính nguyên hàm
x = symbols('x')
d = x/(x**2+1)
nguyenham = integrate(d,x)
print(nguyenham)

#2.5 Viết hàm tính tích phân
x = symbols('x')
f = (1-x*tan(x))/(x*x*cos(x)+x)
tichphan = integrate(f,(x,2*pi/3,pi))
print(tichphan)