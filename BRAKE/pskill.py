file = (open('ps.txt',encoding="utf-8"))
store= file.read().split('\n') 
lts = '%s'*len(store) % tuple(store) 
psk=[]
ans =[]
astr=''
i =32

for s in range(len(store)):
    lts = '%s'*len(store[s]) % tuple(store[s])
    for tk in range(len(lts)):
        while i < 127:
            if lts[tk] == chr(i):
              astr = astr + chr(i)
            i = i+1
        i =32
    ans.append(astr)
    astr=''
print('ANSWER IS:',ans)     
       
      
    
    
    
  
            
