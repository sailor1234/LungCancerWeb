import requests
 
r = requests.get('http://192.168.0.222:8999/nguyen_van_a')
#print(list1.text)
#print(list2.text)
data = r.json()
print(data)
print(data['nodule_annos'])
#print(data['predlist'])