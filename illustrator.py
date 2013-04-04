import string
import sys
import re

def filename_to_illustrator(filename):
    pattern = '.*_by_(\D*)\d*'
    match = re.search(pattern, filename)
    if not match:
        return "UNKNOWN"
    group = match.group(1)
    #print group
    group = string.replace(group, '_', ' ')
    group = group.title()
    return group

fname = sys.argv[1]
#print fname

with open(fname) as f:
    content = f.readlines()

card_pattern = '^card'
image_pattern = '\simage: local_image_file\(\"(.*)\"\)'
illustrator_pattern = '\sillustrator: \"(.*)\"'

modified_list = []
corrected_illustrator = None

for c in content:
    card_match = re.search(card_pattern, c)
    image_match = re.search(image_pattern, c)
    illustrator_match = re.search(illustrator_pattern, c)

    #print card_match, image_match, illustrator_match
    if illustrator_match:
        continue

    if image_match:
        modified_list.append(c)
        modified_list.append("\tillustrator: \"" + filename_to_illustrator(image_match.group(1)) + "\"\n")
        continue

    modified_list.append(c)

for m in modified_list:
    sys.stdout.write(m)
