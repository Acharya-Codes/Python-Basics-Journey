import time
import datetime
import pygame
def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    print("Waiting.....")

if __name__ == "__main__":
    alarm_time = input("Enter the time (HH:MM:SS): ")
    set_alarm(alarm_time)
    sound_file = "q24_soundeffect.mp3"
    is_running=True
    while is_running:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,end="\r")
        
        if current_time == alarm_time:
            print("\n\nWake Up")
            
            pygame.mixer.init()  # mixer is used to play sounds
            try:
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            except:
                print("Sound file not found,Alarm triggered anyway")
            is_running=False
        time.sleep(1)
