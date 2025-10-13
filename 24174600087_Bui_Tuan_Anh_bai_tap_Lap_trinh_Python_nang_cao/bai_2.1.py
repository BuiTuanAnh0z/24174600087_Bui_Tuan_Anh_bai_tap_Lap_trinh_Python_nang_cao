import xml.etree.ElementTree as ET
company = ET.Element("company")
director = ET.SubElement(company, "director")
director.text = "Nguyễn Văn A"
address = ET.SubElement(company, "address")
address.text = "Số 10, Đường Láng, Hà Nội"
phone = ET.SubElement(company, "phone")
phone.text = "0123456789"
code = ET.SubElement(company, "code")
code.text = "CT001"
tree = ET.ElementTree(company)
tree.write("company.xml", encoding="utf-8", xml_declaration=True)
