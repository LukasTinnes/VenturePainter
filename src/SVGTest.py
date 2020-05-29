import xml.etree.ElementTree as ET
root = ET.parse("../Resources/test.svg").getroot()
print(root.attrib)