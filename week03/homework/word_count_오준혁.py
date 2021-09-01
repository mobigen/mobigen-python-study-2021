count_dict = {}
count_list = []
with open('../wiki_python.txt', 'r', encoding='UTF-8') as f:
    for i in f.readlines():
        count_list.extend(i.replace('\t', ' ').replace('\n', ' ').split(' '))

    count_list = list(filter(('').__ne__, count_list))

    for word in count_list:
        if word in count_dict.keys():
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    print(count_dict)

count = sorted(count_dict.values(), reverse=True)[:10]
order_dict = {}

for k, v in count_dict.items():
    if v in count:
        order_dict[k] = v
print(order_dict)


