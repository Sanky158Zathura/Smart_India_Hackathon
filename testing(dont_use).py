import threading

from pygame.time import delay


def drive(speed_queue):
    while True:
        delay(1000)
        print("speed:", speed_queue)

def main():
    speed_queue = 1
    threading.Thread(target=drive, args=(speed_queue,)).start()
    delay(10000)
    while True:
        speed_queue = 3
        threading.Thread(target=drive, args=(speed_queue,)).start()
main()