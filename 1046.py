start_time, end_time = list(map(int,input().split()))

if (start_time<end_time):
    duration = end_time-start_time
else:
    duration = end_time+24-start_time
print(f"O JOGO DUROU {duration} HORA(S)")