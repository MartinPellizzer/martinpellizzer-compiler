import os

keyword = 'sterilizer'
output_file = 'keywords/sterilizer.txt'

if not os.path.exists(output_file):
    with open(output_file, 'w') as f: pass

with open('keywords/ozone-scrape.txt', encoding='utf-8') as f:
    lines = f.readlines()

lines_sorted = sorted(lines)

match_list = []
unmatch_list = []

for line in lines_sorted:
    if keyword in line: match_list.append(line)
    else: unmatch_list.append(line)



with open(output_file, encoding='utf-8') as f:
    lines_output = f.readlines()

match_list_new = []
for line in match_list:
    found = False
    for line_output in lines_output:
        if line.strip() == line_output.strip():
            found = True
    if not found:
        match_list_new.append(line)

with open(output_file, 'a', encoding='utf-8') as f:
    for keyword in match_list_new:
        f.write(keyword)

with open('keywords/ozone-scrape.txt', 'w', encoding='utf-8') as f:
    for keyword in unmatch_list:
        f.write(keyword)

print(len(match_list))
print(len(unmatch_list))
