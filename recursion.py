import os

def disk_usage(path):
    """return the number of byts used by a ile/folder and descendents"""
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path,filename)
            total += disk_usage(childpath)
        
    print('{0:<7}'.format(total), path)
    return total


parent = 'C:\\Users\\jorh\\Desktop\\python-execise'

#disk_usage(parent)


"""
This function is to calculate the multiple by the Add algorithm 
"""
def multiple(m,n):
    total = 0
    if m == 1:
        total = n
    elif m < 1:
        total = 0
    else:
        total += n                 #add the num everytime
        total += multiple(m-1,n)
    print(m,n,total)
    return total

print("the multiple is :",multiple(0,4.2))


