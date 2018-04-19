import xml.etree.ElementTree as ET

tree = ET.parse('list_of_users.xml')
root = tree.getroot()
# print(root.tag)

for branch in root:
	# print(branch.tag , branch.attrib,': \
		# ' + branch.text)
	if branch.tag == 'adress':
		for sibling in branch:
			print(sibling.tag + ': ' +sibling.text)
		# print(branch.tag + ': ' + branch.text)

new_root = ET.Element('Menu')
new_branch_1 = ET.SubElement(new_root, 'Main')
new_branch_2 = ET.SubElement(new_root, 'News')
new_branch_3 = ET.SubElement(new_root, 'About')
new_branch_1.text = 'Main text'
new_branch_2.text = 'Telegram in block'
new_branch_3.text = 'PrOxy fans'
# ET.dump(new_root)

for_file = ET.tostring(new_root)
f = open('New_list_of_users.xml', 'wb')
f.write(for_file)

