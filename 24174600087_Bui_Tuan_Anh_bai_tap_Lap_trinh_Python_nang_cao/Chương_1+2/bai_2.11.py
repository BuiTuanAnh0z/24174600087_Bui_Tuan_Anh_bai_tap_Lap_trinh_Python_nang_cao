import json
from datetime import datetime
so_tien = float(input("Nhập số tiền giao dịch: "))
ghi_vao = int(input("Bạn có muốn lưu giao dịch không? (1=Có, 0=Không): "))

if ghi_vao == 1:
    ten_file = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".json"
    giao_dich = {
        "so_tien": so_tien,
        "thoi_gian": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    with open(ten_file, "w", encoding="utf-8") as f:
        json.dump(giao_dich, f, ensure_ascii=False, indent=4)
    print("Đã ghi giao dịch vào:", ten_file)
else:
    print("Không lưu giao dịch.")
