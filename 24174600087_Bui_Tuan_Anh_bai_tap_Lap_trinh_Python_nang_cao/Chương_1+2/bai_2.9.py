import json

du_lieu_json = '''
[
    {"ten": "An", "tuoi": 21},
    {"ten": "Bình", "tuoi": 25},
    {"ten": "Hà", "tuoi": 20}
]
'''
danh_sach = json.loads(du_lieu_json)

danh_sach_sap_xep = sorted(danh_sach, key=lambda x: x["tuoi"])

print("Danh sách sau khi sắp xếp theo tuổi:")
for nv in danh_sach_sap_xep:
    print(nv)
