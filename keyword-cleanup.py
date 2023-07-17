with open('blacklist.txt', encoding='utf-8') as f:
    keywords = f.read().split(',')


with open('keywords/ozone-scrape.txt', encoding='utf-8') as f:
    lines = f.readlines()

lines_sorted = sorted(lines)

# lines_sorted.remove('aqua')

lines_sorted = [ x for x in lines_sorted if 'ozone' in x ]

for keyword in keywords:
    keyword = keyword.strip()
    if not keyword: continue
    lines_sorted = [ x for x in lines_sorted if keyword not in x ]


with open('keywords/ozone-scrape.txt', 'w', encoding='utf-8') as f:
    for keyword in lines_sorted:
        f.write(keyword)

print(len(lines_sorted))
