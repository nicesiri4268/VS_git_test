def test():
    print ('yes')

def init(data):
    'data is a dict'
    data["fist"]={}
    data["middle"]={}
    data["last"]={}

def lookup(data,label,name):
    return data[label].get(name)

def store(data,full_name):
    names = full_name.split()
    if len(names)==2:
        names.insert(1," ")
    labels = ("fist","middle","last")
    for label ,name in zip (labels,names):
        people = lookup(data,label,name)
        if people:
            people.append(full_name)
        else :
            data[label][name]=[full_name]

def store_1(data,*full_names):
    "允许多个姓名输入"
    for full_name in full_names :
        names = full_name.split()
        if len(names)==2:
            names.insert(1," ")
        labels = ("fist","middle","last")
        for label ,name in zip (labels,names):
            people = lookup(data,label,name)
            if people:
                people.append(full_name)
            else :
                data[label][name]=[full_name]
    