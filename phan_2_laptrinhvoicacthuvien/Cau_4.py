#Câu 4:

#4.1 Viết hàm vẽ đồ thị mặt yên ngựa
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
%matplotlib inline

def yen_ngua():
  x = np.linspace(start=-10, stop=10, num=1000)
  y = np.linspace(start=-10, stop=10, num=1000)
  x, y = np.meshgrid(x, y)
  z = (x/3)**2 - (y/2)**2
  fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
  rosen_surf = ax.plot_surface(x, y, z,cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
  ax.set_zlim(-30, 30)
  fig.colorbar(rosen_surf, shrink=0.5,aspect=5)
  plt.show()

yen_ngua()

#4.2 Viết hàm vẽ đồ thị mặt hyperbolic 1 tầng
def hyperbols():
  m = np.linspace(start=-10, stop=10, num=1000)
  n = np.linspace(start=-10, stop=10, num=1000)
  m, n = np.meshgrid(m, n)
  p1 = 2*((m/3)**2 + (n/5)**2 - 1)**(1/2)
  p2 = -2*((m/3)**2 + (n/5)**2 - 1)**(1/2)
  fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
  rosen_surf1 = ax.plot_surface(m, n, p1,cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
  rosen_surf2 = ax.plot_surface(m, n, p2,cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
  fig.colorbar(rosen_surf1, shrink=0.5,aspect=30)
  fig.colorbar(rosen_surf2, shrink=0.5,aspect=30)
  plt.show()

hyperbols()

#4.3 Viết hàm vẽ đồ thị mặt cầu
def mat_cau():
    a = np.linspace(start=-5, stop=5, num=80)
    b = np.linspace(start=-5, stop=5, num=80)
    a, b = np.meshgrid(a, b)

    c1 = 4 + (4 - (a + 2) ** 2 - (b - 1) ** 2) ** (1 / 2)
    c2 = 4 - (4 - (a + 2) ** 2 - (b - 1) ** 2) ** (1 / 2)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    matcau1 = ax.plot_surface(a, b, c1, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
    matcau2 = ax.plot_surface(a, b, c2, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
    fig.colorbar(matcau1, shrink=0.5, aspect=5)
    fig.colorbar(matcau2, shrink=0.5, aspect=5)
    plt.show()

mat_cau()