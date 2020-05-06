Mydic = {'China':'Beijing','UK':'London','US':'WashtonDC'}#字典类型key不可重，否则结对以后一个key对应的value 为准
Mydic['FN']='London'
Mydic['US']='Lostangle'
print(Mydic.get('FN','None'))
print(Mydic.items())


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
