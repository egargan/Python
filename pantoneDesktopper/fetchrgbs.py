## Script to get list of pantone RGB values from specific .html file

import sys
import xml.etree.ElementTree as ET

def main():

    tree = ET.parse('panpage.html')
    root = tree.getroot()

    for row in root.iter('tr'):
        print(str(row[0].text) + "/" + str(row[1].text))

if __name__ == '__main__':
    main()
