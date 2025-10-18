import json
data_json = '''
{
    "company": "GeeksForGeeks",
    "employees": [
        {"name": "Amar Pandey", "salary": "8.5 LPA"},
        {"name": "Akbhar Khan", "salary": "6.5 LPA"},
        {"name": "Anthony Walter", "salary": "3.2 LPA"}
    ]
}
'''
data = json.loads(data_json)
print("Công ty:", data["company"])
print("Danh sách nhân viên:")
for emp in data["employees"]:
    print("-", emp["name"], ":", emp["salary"])
