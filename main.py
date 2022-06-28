
def contain(data,var):
    '''Contain@ stanum e 2 parametr, arajiny lst : veradarcnum e true ete
    tvyal zangvacum ka tvyal popoxakany'''
    if data.count(var) >=1:
        return True
    else :
        return False

#test
#print(contain([1,2,3,4,5,6,56],4))

def pop(data,i=None):
    '''parametreric arajiny petq e lini list, ete trvum e rekrord parametr ev
    erkrord parametry goyutyun uni listum apa jijum e ete chka erkroprd
    parametr apa jnjvum e listi verjin arjeqy'''
    return data.pop() if i == None else  data.pop(i)


#test
#print(pop([1,2,3,4],0))


def remove_all(data,value):
    '''stanum e list ev jnjum trvac arjeqin havasar bolor andamnery'''
    for i in data:
          data.remove(value)
    return data

#test
#print(remove_all([1,2,3,1,2,1,1,21,1],1))

def reverse(data):
    '''stanum e list ev shrjum e ajn ir texum'''
    data.reverse()
    return data
#test
#print(reverse([1,2,3,1,5]))

def min(data):
    '''stanum e list ev veradarcnum e listi poqraguyn arjeqy'''
    min = data[0]
    for i in data:
        if i < min:
            min =i
    return min

#test
#print(min([123,555,3,5]))

def max(data):
    '''stanum e list ev veradarcnum e listi mecaguyn arjeqy'''
    max = data[0]
    for i in data:
        if i > max:
            max =i
    return max

#test
#print(max([123,555,3,5]))



