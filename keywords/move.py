import sys

def move(keyword):

    with open('keywords-todo.txt', errors='ignore') as f:
        keywords_new = f.readlines()

    with open('_tmp_keywords.txt', errors='ignore') as f:
        keywords_old = f.readlines()

    keywords_new_filtered = [k for k in keywords_new if keyword in k]
    keywords_new_filtered = [k for k in keywords_new_filtered if k not in keywords_old]
    keywords_old_filtered = [k for k in keywords_new if k not in keywords_new_filtered]

    print(len(keywords_new))
    print(len(keywords_new_filtered))
    print(len(keywords_old_filtered))

    with open('_tmp_keywords.txt', 'a', errors='ignore') as f:
        for k in keywords_new_filtered:
            f.write(k)

    with open('keywords-todo.txt', 'w', errors='ignore') as f:
        for k in keywords_old_filtered:
            f.write(k)
            


move(sys.argv[1])