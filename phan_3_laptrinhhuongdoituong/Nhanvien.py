#Câu 1:

#1.1 Xây dựng lớp NhanVien có các thuộc tính là hoten, tuoi, luong
class NhanVien:
  def __init__(self, name, age, money):
      self.hoten = name
      self.tuoi = age
      self.luong = money

# 1.2 Viết hàm nhập dữ liệu cho 1 list các đối tượng thuộc lớp NhanVien.
  def __str__(self, ):
    info = 'tên: ' + self.hoten + ', ' + 'tuổi: ' + str(self.tuoi) + ', ' + 'lương: ' + str(self.luong)
    return info
  def __gt__(self, obj):
    return (self.tuoi > obj.tuoi)

  def __ge__(self, obj):
    return (self.tuoi >= obj.tuoi)

  def __lt__(self, obj):
    return (self.tuoi < obj.tuoi)

  def __le__(self, obj):
    return (self.tuoi <= obj.tuoi)

  def __eq__(self, obj):
    return (self.tuoi == obj.tuoi)
