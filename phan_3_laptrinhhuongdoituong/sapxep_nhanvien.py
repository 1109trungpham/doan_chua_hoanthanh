from Nhanvien import NhanVien

#Viết hàm sắp xếp list các đối tượng thuộc lớp NhanVien theo chiều giảm dần của độ tuổi.

def main():
    nv = [NhanVien('Phạm Bá Trung',23,1500),NhanVien('Phạm Tuấn',24,2000),NhanVien('Phạm Tú Anh',22,1300)]
    nv = sorted(nv,reverse=True)
    for item in nv:
        print(item)
if __name__=='__main__':
  main()