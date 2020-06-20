import xml.etree.ElementTree as ET
import re
import os

for image in os.listdir("../Resources"):

    root = ET.parse(str.format("../Resources/{0}", image)).getroot()
    print(root.tag, root.attrib)
    # Print all the cool parts of the picture
    for child in root:
        # Remove namespace in tag via unneccesary reg expression because reeeeee
        tag = re.sub(r"{http://www\.w3\.org/2000/svg}", "", child.tag)
        child.tag = tag
        print(child.tag, child.attrib)
