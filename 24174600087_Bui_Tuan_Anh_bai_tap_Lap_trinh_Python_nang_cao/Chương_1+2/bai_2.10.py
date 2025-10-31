import json
du_lieu = '''
{
    "cong_ty": "Công ty TNHH Đất Việt",
    "dia_chi": "Hải Phòng - Hà Nội",
    "nhan_vien": [
        {"ten": "An", "don_vi": "A1"},
        {"ten": "Bình", "don_vi": "A2"},
        {"ten": "Chi", "don_vi": "A1"},
        {"ten": "Dũng", "don_vi": "A3"},
        {"ten": "Hà", "don_vi": "A1"}
    ]
}
'''
data = json.loads(du_lieu)
print("Tên công ty:", data["cong_ty"])
print("Địa chỉ:", data["dia_chi"])
tong_nv = len(data["nhan_vien"])
thong_ke = {}
for nv in data["nhan_vien"]:
    don_vi = nv["don_vi"]
    thong_ke[don_vi] = thong_ke.get(don_vi, 0) + 1
print("----- Thống kê nhân viên theo đơn vị -----")
for dv, so_nv in thong_ke.items():
    ty_le = round(so_nv / tong_nv * 100, 2)
    print(f"Tên đơn vị: {dv}\nSố nhân viên: {so_nv}\nTỷ lệ: {ty_le}%\n")
