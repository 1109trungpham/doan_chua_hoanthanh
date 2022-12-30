from Nhanvien import NhanVien
import os
import pickle

#Viết hàm lưu list các đối tượng thuộc lớp NhanVien vào tập tin nhị phân

def luu_nhanvien(thumuc: str, ten_taptin: str, objs: list[NhanVien]):
    try:
        with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
            pickle.dump(objs, f)
        print('Hoàn thành quá trình lưu dữ liệu vào tập tin')
    except Exception as e:
        print(e)
        print('Xảy ra lỗi trong quá trình lưu file')

#Viết hàm đọc list các đối tượng thuộc lớp NhanVien từ tập tin nhị phân

def doc_nhanvien(thumuc: str, ten_taptin: str) -> list[NhanVien]:
    try:
        with open(os.path.join(thumuc, ten_taptin), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        return None

def in_list_nhanvien(content: list[NhanVien]):
    for item in content:
        print(item)

#Viết chương trình chính gọi thực hiện các hàm trên

def main():
    path = '/Users/trung/data'
    filename = 'nhanvien'
    nv1 = [NhanVien('Bá Trung', 19, 2000),
           NhanVien('Phạm Tuấn', 20, 2300),
           NhanVien('Diễm Trang', 18, 4000)]
    luu_nhanvien(path, filename, nv1)
    noidung = doc_nhanvien(path, filename)
    in_list_nhanvien(noidung)
    print('Kết thúc chương trình')

if __name__ == '__main__':
    main()