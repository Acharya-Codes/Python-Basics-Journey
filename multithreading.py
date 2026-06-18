#Used to perfrom multi-tasking
import threading
import time
def walk_dog(name):
    time.sleep(12)
    print(f"You finished walking {name} 🐕‍🦺")
def listen_music(music_name):
    time.sleep(3)
    print(f"You finished listening to {music_name} 🎶")
def look_for_crush(luver_name):
    time.sleep(7)
    print(f"You found {luver_name} 😏💘")

work1 = threading.Thread(target=walk_dog,args=("Jimmy",))
work1.start()
work2 = threading.Thread(target=listen_music,args=("Faded",))
work2.start()
work3 = threading.Thread(target=look_for_crush,args=("LDS🐖",))
work3.start()

work1.join()
work2.join()
work3.join()  # Bascially makes the line 28 print at last

time.sleep(2)
print("Morning routine done 😃")