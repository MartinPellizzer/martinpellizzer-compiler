keyword = 'adventures'

with open('keywords/ozone-scrape.txt', encoding='utf-8') as f:
    lines = f.readlines()

lines_sorted = sorted(lines)

match_list = []
unmatch_list = []

for line in lines_sorted:
    if keyword in line: match_list.append(line)
    else: unmatch_list.append(line)

with open('keywords/ozone-scrape.txt', 'w', encoding='utf-8') as f:
    for keyword in unmatch_list:
        f.write(keyword)

print(len(match_list))
print(len(unmatch_list))
