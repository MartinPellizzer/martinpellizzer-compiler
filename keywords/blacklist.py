from tkinter import *  
  
root = Tk()  
root.geometry("800x600")

with open('words-count.txt', encoding='utf-8') as f:
    lines1 = f.readlines()

with open('words-blacklist.txt', encoding='utf-8') as f:
    lines2 = f.readlines()

listbox1 = Listbox(root, width=32)  
listbox1.pack(side='left', fill='y', padx=32, pady=32)  

lines2_keyword = [x.split(',')[0] for x in lines2]
# TODO filter blacklisted keywords
lines_filtered = [x for x in lines1 if x.split(',')[0] not in lines2_keyword]

for l in lines_filtered:
    listbox1.insert('end', l)




listbox2 = Listbox(root, width=32)  
listbox2.pack(side='left', fill='y', padx=32, pady=32)  

for l in lines2:
    listbox2.insert('end', l)


def blacklist_item(e):
    item_index = listbox1.curselection()
    item_value = listbox1.get(item_index)
    listbox2.insert('end', item_value)
    listbox1.delete(item_index)
    listbox1.selection_set(item_index)

    with open('words-blacklist.txt', 'a', encoding='utf-8') as f:
        f.write(item_value)


listbox1.bind('x', blacklist_item) 


def save():
    with open('keywords-todo.txt', encoding='utf-8') as f:
        tmp_lines1 = f.readlines()

    with open('words-blacklist.txt', encoding='utf-8') as f:
        tmp_lines2 = f.readlines()
    
    # print(tmp_lines1[:10])
    
    tmp_lines2_keyword = [x.split(',')[0] for x in tmp_lines2]
    # tmp_lines_filtered = [x for x in tmp_lines1 if x not in tmp_lines2_keyword]

    # for i, k1 in enumerate(tmp_lines1):
    #     if i > 10: break
    #     print(k1)
        
    # for j, k2 in enumerate(tmp_lines2):
    #     if j > 10: break
    #     print(k2)

    total_filtered = 0
    tmp_filtered_keywords = []
    for k1 in tmp_lines1:
        found = False
        for k2 in tmp_lines2:
            word, occurence = k2.split(',')
            if word in k1:
                found = True
                total_filtered += 1
                break
        if not found:
            tmp_filtered_keywords.append(k1) 

    print(tmp_filtered_keywords[:10])
    print(len(tmp_filtered_keywords))
    print(total_filtered)
    print(len(tmp_filtered_keywords) + total_filtered)
    print(len(tmp_lines1))
    
    with open('keywords-todo.txt', 'w', encoding='utf-8') as f:
        for k in tmp_filtered_keywords:
            f.write(k)



button = Button(text='Save', command=save)
button.pack(side='left', padx=32, pady=32)



root.mainloop()