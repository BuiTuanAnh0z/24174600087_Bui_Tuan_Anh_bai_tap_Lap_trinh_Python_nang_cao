import json
nhan_vien = {
    "ten": "Nguyen Van A",
    "tuoi": 28,
    "phong_ban": "IT",
    "luong": 1200
}
chuoi_json = json.dumps(nhan_vien, ensure_ascii=False, indent=4)
print("Chuỗi JSON:")
print(chuoi_json)
