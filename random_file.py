import random 
listt= ['Welcome',
'Munna bhai MBBS',
'Singh is bling', 
'no issue lelo na tissue',
'Carry on jata',
'Andaz apna apna',
'Golmaal']
dict_ = {'Welcome':0,
'Munna bhai MBBS':0,
'no issue lelo na tissue':0,
'Singh is bling':0,
'Carry on jata':0,
'Andaz apna apna':0,
'Golmaal':0}
for i in range(50):

    key = random.choice(listt)
    
    dict_[key]+=1
max_ =  0
name_str = " "
for k,v in dict_.items():
    if v>max_:
        max_ = v
        name_str = k
print(name_str)
