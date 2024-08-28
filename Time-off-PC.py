import time
import os

def shutdown_computer():
    os.system('shutdown /s /t 0')

def countdown_timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds

    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        hrs, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hrs, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("Время истекло! Выключение компьютера...")
    shutdown_computer()

if __name__ == "__main__":
    try:
        print('Таймер обратного отчета для выключения ПК.\n')
        hours = int(input("Введите ЧЧ: "))
        minutes = int(input("Введите ММ: "))
        seconds = int(input("Введите СС: "))
        countdown_timer(hours, minutes, seconds)
    except ValueError:
        print("Пожалуйста, введите корректные числа.")
