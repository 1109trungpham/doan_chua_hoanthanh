#Câu 2:

#2.1 Viết hàm sinh ngẫu nhiên các giá trị cho 1 list các số thực trong khoảng [a, b]
def sinh():
    a = int(input('nhập giá trị a: '))
    b = int(input('nhập giá trị b: '))
    n = int(input('số phần tử: '))
    print('list được sinh ngẫu nhiên trong (', a, ',', b, ')', 'với',n,'phần tử số thực')
    global x
    x = (b - a) * np.random.random_sample(n) + a
    print('list x cần tạo =', x)

#2.2 Viết hàm sắp xếp list các số thực ở trên theo chiều:
# tăng dần (nếu tham số reverse= True),giảm dần (nếu tham số reverse= False)
def sapxep(list,rev):
    print('list cần sắp xếp =',list)
    if rev == True:
        print('sắp xếp tăng dần =',sorted(list))
    else:
        print('sắp xếp giảm dần =',sorted(list, reverse = True))

#2.3 Viết hàm tìm kiếm số n trong list:
#- Nếu không tìm thấy thì thông báo ra màn hình là không tìm thấy số n trong list
#- Nếu tìm thấy thì hiển thị ra màn hình tất cả các vị trí trong list có giá trị bằng với n.
def tim(list, n):
    vitri = []
    for i in range(len(list)):
        if list[i] == n:
            vitri.append(i)
    if len(vitri) != 0:
        print('đã tìm thấy',n,'trong list')
        print('vị trí lần lượt: ',vitri)
    else:
        print('không tìm thấy',n,'trong list')

#2.4 Viết hàm lưu list vào tập tin có tùy chọn tham số để xác định là lưu tập tin văn bản hay tập tin nhị phân
def luu(list):
    path = str(input('nhập đường dẫn: '))
    filename = str(input('nhập tên tập tin: '))
    print('nhập số 0 nếu bạn muốn lưu kiểu text')
    print('nhập số nguyên khác 0 nếu bạn muốn lưu kiểu binary')
    nhap = int(input('nhập kiểu: '))

    if nhap == 0:
        with open(os.path.join(path, filename), 'a') as f:
            f.write(str(list))
    else:
        with open(os.path.join(path, filename), 'ab') as f:
            array = bytearray(list)
            f.write(array)