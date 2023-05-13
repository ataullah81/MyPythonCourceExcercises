initial_hour, initial_minute, final_hour, final_minute = list(map(int, input().split()))

intial_time = initial_hour*60+initial_minute
final_time = final_hour*60+final_minute

if (final_time>initial_time):
    duration = final_time-intial_time
else:
    duration_hour = final_hour-initial_hour
    duration_minute = final_minute+60-initial_minute
    print(f"O JOGO DUROU {duration_hour} HORA(S) E {duration_minute} MINUTO(S)")

    #duration_hour = final_hour + 24 - initial_hour
