a=[1,2,3,4,5]
b=[4,5,6,7,8]
def common_elements(a,b):
    common=[]
    for i in a:
        for j in b:
            if i==j:
                common.append(i)
    print(common)
common_elements(a,b)
