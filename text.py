


def __lt__(x,y):
    return x<y

def __gt__(x,y):
    return x>y
# =============================================================================
#     if(x>y):
#         return True
#     else:
#         return False
# =============================================================================

def BbubbleSort(alist):
        for passnum in range(len(alist)-1,0,-1):
            for i in range(passnum):
                if __lt__(alist[i],alist[i+1]):
                    alist[i],alist[i+1] = alist[i+1],alist[i]
                    
def SbubbleSort(alist):
        for passnum in range(len(alist)-1,0,-1):
            for i in range(passnum):
                if __gt__(alist[i],alist[i+1]):
                    alist[i],alist[i+1] = alist[i+1],alist[i]             
                    
a = [54,26,93,17,77,31,44,55,20]
b = [54,26,93,17,77,31,44,55,20]
BbubbleSort(a)
SbubbleSort(b)

print('B Bubble: ',a) 
print('S Bubble: ',b) 


https://ithelp.ithome.com.tw/articles/10161285
    
    
    
    
 //main

import my_class

a = [54,26,93,17,77,31,44,55,20]

c = my_class.A(a)
print(c.BbubbleSort)
