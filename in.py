import urllib
from pynput import keyboard
urllist=[]

def on_press(key):
    # 如果按下了 <Esc>鍵
    if key == keyboard.Key.esc:
        global is_stopped
        is_stopped = True

        # 停止監聽
        listener.stop()


is_stopped = False

listener = keyboard.Listener(on_press=on_press)
listener.start()

print("按下 <Esc> 退出程序~")
while True:
    urlstr=input("網址:")
    urllist.append(urlstr)
    
    # 如果停止了監聽則退出無窮
    if is_stopped:
        print("程序已退出")
        break

for  i in urllist:
    print(urllib.parse.unquote(i))
    

