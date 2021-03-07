import time
def process(path):
    time.sleep(2)
    if path:
        print('Processing the file.')
        with open(path, 'r') as f:
            print(f)