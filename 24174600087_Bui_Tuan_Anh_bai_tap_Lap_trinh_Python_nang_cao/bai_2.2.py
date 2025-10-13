import xml.etree.ElementTree as ET
root = ET.Element("students")
student1 = ET.SubElement(root, "student")
ET.SubElement(student1, "id").text = "SV001"
ET.SubElement(student1, "name").text = "Trần Minh Đức"
ET.SubElement(student1, "birth_year").text = "2004"
ET.SubElement(student1, "class").text = "18A2"
ET.SubElement(student1, "gender").text = "Nam"
student2 = ET.SubElement(root, "student")
ET.SubElement(student2, "id").text = "SV002"
ET.SubElement(student2, "name").text = "Nguyễn Thị Hoa"
ET.SubElement(student2, "birth_year").text = "2005"
ET.SubElement(student2, "class").text = "18A2"
ET.SubElement(student2, "gender").text = "Nữ"
tree = ET.ElementTree(root)
tree.write("students.xml", encoding="utf-8", xml_declaration=True)
