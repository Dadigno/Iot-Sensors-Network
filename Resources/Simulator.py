import _thread
from Resources import Plugin
import time

UPDATE_TIME = 2 #s


def start_simulator():
    print("Start simulator")
    _thread.start_new_thread(update_sim, ("sensors", "payload",))


def stop_simulator():
    return 0

def update_sim(root, rawJson):
    value = 0
    while 1:
        print(f"Update resources {value}")
        value += 1
        payload = f'''
        {{
            "temp": {{
              "value": {value},
              "unit": "mt"
            }}
        }}
        '''
        Plugin.update_resource(root, payload)
        time.sleep(UPDATE_TIME)




