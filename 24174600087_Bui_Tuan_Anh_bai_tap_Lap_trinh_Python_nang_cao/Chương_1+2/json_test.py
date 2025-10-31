# import json
# data = {"name": "Ng Văn A", "age": 23, "skills": ["AI", "Python"]}
# json_str = json.dumps(data)
# print(json_str)
# json_str = json.dumps(data)
# print(json_str)
# import json
# def complex_handler(obj):
#     if isinstance(obj, complex):
#         return [obj.real, obj.imag]
#     raise TypeError(repr(obj) + " không thể mã hóa JSON")
# data = {"z": 2 + 3j}
# complex_obj = json.dumps(data, default=complex_handler)
# print(complex_obj)
# import json
# data = {"name": "A", "age": 35, "company": "Đất Việt"}
# json_string = json.dumps(data, ensure_ascii=False)
# print(json_string)
# print(type(json_string))
# import json

# # Đối tượng Python (đối tượng dict)
# data = {
#     "Ho_va_ten": "Nguyễn Văn A",
#     "Nam_sinh": 2025,
#     "Gioi_tinh": "Nam",
#     "So_dt": "0123456789",
#     "email": "nguyenvana@uneti.edu.vn"
# }

# # Sử dụng 'with open' để mở tệp 'thongtin.json' với chế độ ghi (w)
# # Hàm json.dump() sẽ ghi đối tượng Python (dict) vào tệp JSON
# with open("thongtin.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)

# print("Dữ liệu đã được ghi thành công vào tệp 'thongtin.json'.")

# # (Tùy chọn) In nội dung tệp để kiểm tra
# with open("thongtin.json", "r", encoding="utf-8") as f:
#     print("\nNội dung tệp 'thongtin.json' —>")
#     print(f.read())
# import json

# # Hàm kiểm tra chuỗi JSON có chứa đối tượng phức (complex object) hay không
# def is_complex(object):
#     # Kiểm tra xem trong đối tượng có tồn tại khóa '__complex__' hay không
#     if '__complex__' in object:
#         # Nếu có, tạo một số phức từ thông tin trong đối tượng
#         return complex(object['real'], object['img'])
#     # Nếu không có khóa '__complex__', đối tượng không phải là đối tượng phức,
#     # trả về đối tượng gốc
#     return object


# def main():
#     # Sử dụng hàm json.loads() với object_hook để kiểm tra và chuyển đổi đối tượng
#     # phức trong chuỗi JSON
#     complex_object = json.loads('{"__complex__": true, "real": 4, "img": 5}', 
#                                 object_hook=is_complex)
#     simple_object = json.loads('{"real": 6, "img": 7}', 
#                                object_hook=is_complex)

#     # In kết quả phân tích chuỗi JSON cho đối tượng phức và đối tượng thường
#     print("Đối tượng số phức......:", complex_object)
#     print("Đối tượng bình thường......:", simple_object)


# if __name__ == "__main__":
#     main()
# import json
# # Import lớp JSONDecoder từ module json.decoder
# from json.decoder import JSONDecoder

# # Chuỗi JSON chứa dữ liệu màu sắc
# colour_string = '{"colour": ["red", "yellow"]}'

# #  Sử dụng JSONDecoder để giải mã chuỗi JSON thành đối tượng Python.
# # JSONDecoder là lớp con của json.JSONDecoder, cho phép tùy chỉnh quá trình giải mã.
# # Phương thức decode() sẽ giải mã chuỗi JSON và trả về đối tượng Python tương ứng.
# decoded_object = JSONDecoder().decode(colour_string)

# # In đối tượng Python đã giải mã và kiểu dữ liệu của đối tượng đó
# print(decoded_object)
# print(type(decoded_object))

