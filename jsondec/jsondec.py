import json
''' Простой скрипт'''

with open('cDqLD89j.json', 'r', encoding='utf-8') as fh:
    all_file = fh.read()
    all_file = all_file.replace('},','}$$')
    split_file = all_file.split('$$')
    new_list = []
    for i in split_file:
        i = i.replace('\n', '')
        #print(i)
        new_list.append(i)

data = [json.loads(line) for line in new_list]
res = []
for k, v in enumerate(data):
    k += 1
    dic = {}
    dic["model"] = "vendors.Vendor"
    dic["pk"] = k
    dic["fields"] = v
    dic["fields"]["title"] = dic["fields"]["name"]
    del dic["fields"]["name"]
    dic["fields"]["siteUrl"] = ''
    dic["fields"]["logo"] = ''
    del dic["fields"]["retread"]
    res.append(dic)
    #print(dic["fields"])
new_res = []
for i in res:
    new_res.append(i)

#print(new_res)
with open('data_fix.json', 'w', encoding='utf-8') as f:
    json.dump(new_res, f, ensure_ascii=False, indent=4)
#print(new_res)

