durationInSecond = int(input())

hour = durationInSecond/3600
remainderHour = durationInSecond % 3600
minute = remainderHour/60
second = remainderHour % 60

print("%d" % hour + ":" + "%d" % minute + ":" + "%d" % second)
