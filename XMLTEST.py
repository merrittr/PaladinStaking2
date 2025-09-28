import xml.etree.ElementTree as ET
tree = ET.parse('D:\code\Arcgis\FissionStaking2\interface.XML')
root = tree.getroot()



for child in root:
    print(child.tag, child.attrib)
