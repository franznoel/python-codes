data={'a':[3,4,5],
      'b':{'c':[5,6,7],
           'd':[8,9,10],
           'e':{'f':11, 'g':12, 'h':13}
           },
      'i':{'j':[14,15,{'k':16,'l':17} ],
           'l':['m', 'n', ['o', 'p', 'q']]}}

def foo(d,pre=(),res={}) :
    if isinstance(d,dict) :
        for i in d :
            foo(d[i], pre=pre+(i,), res=res)
    elif isinstance(d,list) :
        for i in enumerate(d) :
            foo(i[1], pre=pre+(i[0],), res=res)
    else :
        res[pre] = d
    return res
   
r = foo(data)

print(r)