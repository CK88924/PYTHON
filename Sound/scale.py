import keyboard
import winsound
Sound={'d':261,'r':293,'m':329,'f':349,'s':392,'l':440,'i':493,'D':523}


'''
while True:  
    try:  
        if keyboard.is_pressed('d'): 
              winsound.Beep(Sound['d'],1000)
              
        if keyboard.is_pressed('r'):
             winsound.Beep(Sound['r'],1000)
             
        if keyboard.is_pressed('m'):
             winsound.Beep(Sound['m'],1000)
             
        if keyboard.is_pressed('f'):
             winsound.Beep(Sound['f'],1000)
             
        if keyboard.is_pressed('s'):
             winsound.Beep(Sound['s'],1000)
             
        if keyboard.is_pressed('l'):
             winsound.Beep(Sound['l'],1000)
             
        if keyboard.is_pressed('i'):
             winsound.Beep(Sound['i'],1000)
             
        if keyboard.is_pressed( 'c' ):
             winsound.Beep(Sound['D'],1000)
             
        if keyboard.is_pressed('Esc'):
            break
       
             
       
                  
            
    except:
        break  


'''
music=['1','1' ,'5' ,'5' ,'6' ,'6' ,'5' ,'4' ,'4','3' ,'3' ,'2' ,'2' ,'1',
       '5','5','4','4','3','3','2' ,'5','5','4','4','3','3','2' , 
       '1','1' ,'5' ,'5' ,'6' ,'6' ,'5' ,'4' ,'4','3' ,'3' ,'2' ,'2' ,'1'  
       ]
for m in music:
    if m== '1':
       winsound.Beep(Sound['d'],1000)
       
    if m== '2':
       winsound.Beep(Sound['r'],1000)
       
    if m== '3':
       winsound.Beep(Sound['m'],1000)
       
    if m== '4':
       winsound.Beep(Sound['f'],1000)
       
    if m== '5':
       winsound.Beep(Sound['s'],1000)
       
    if m== '6':
       winsound.Beep(Sound['l'],1000)
       
    if m== '7':
       winsound.Beep(Sound['i'],1000)
       
    if m== 'c':
       winsound.Beep(Sound['D'],1000)
       
#1155665 4433221 5544332 5544332 1155665 4433221
        
        
