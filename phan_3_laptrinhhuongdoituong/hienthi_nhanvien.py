from Nhanvien import NhanVien

#Viết hàm hiển thị list các đối tượng thuộc lớp NhanVien ra màn hình.

def main():
    nv = [NhanVien('Phạm Bá Trung',23,1500),NhanVien('Phạm Tuấn',24,2000),NhanVien('Phạm Tú Anh',22,1300)]
    for item in nv:
        print(item)
if __name__=='__main__':
    main()