import xml.dom.minidom

# Tên tệp XML đã tạo ở bài 2.3
# Thay thế dòng này:
# file_name = "sample.xml"

# Bằng đường dẫn bạn vừa sao chép (đảm bảo dùng dấu / hoặc \\)
file_name = r"C:\Users\Admin\Desktop\DHKL 18A2HN\24174600087_Bui_Tuan_Anh_bai_tap_Lap_trinh_Python_nang_cao\sample.xml"

try:
    # BÀI 2.4: Tải và phân tích tệp XML, xây dựng DOM
    dom_tree = xml.dom.minidom.parse(file_name)
    print(f" Đã tải và phân tích tệp '{file_name}' thành công.")
    
    # Lấy phần tử gốc (root element)
    root_node = dom_tree.documentElement
    
    # Lấy tên công ty (ví dụ minh họa)
    company_name = root_node.getElementsByTagName("name")[0].childNodes[0].data
    print(f"Tên công ty: {company_name}\n")
    
    # BÀI 2.5: Sử dụng getElementsByTagName() để lấy danh sách phần tử <staff>
    staff_elements = root_node.getElementsByTagName("staff")
    
    print("--- Thống kê nhân viên (Bài 2.5) ---")
    
    # Duyệt và in ra các phần tử
    for staff in staff_elements:
        # Lấy thuộc tính 'id' của thẻ <staff>
        staff_id = staff.getAttribute("id")
        
        # Lấy nội dung của thẻ <name> con
        # getElementsByTagName("name")[0] lấy thẻ <name> đầu tiên trong <staff>
        # .childNodes[0].data lấy nội dung văn bản bên trong thẻ
        staff_name = staff.getElementsByTagName("name")[0].childNodes[0].data
        
        # Lấy nội dung của thẻ <salary> con
        staff_salary = staff.getElementsByTagName("salary")[0].childNodes[0].data
        
        # In thông tin đã lấy được
        print(f"ID: {staff_id}")
        print(f"Tên: {staff_name}")
        print(f"Lương: {staff_salary}")
        print("-" * 15)

except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy tệp {file_name}. Vui lòng kiểm tra vị trí tệp.")
except Exception as e:
    # Lỗi phân tích cú pháp (như "no element found") sẽ bị bắt ở đây
    print(f"Lỗi khi xử lý tệp XML: {e}")