# import datetime
# import threading
# import time

# now = datetime.datetime.now()
# print("현재시간:", now)
# def Alarm():
#     now = datetime.datetime.now()

#     if(now.hour>12):
#         realTime_Hour=now.hour
#     else:
#         realTime_Hour=now.hour

#     realTime_minute=now.minute
#     myHour=int(myHour_Input)
#     myMinute=int(myMinute_Input)

#     print(realTime_Hour,realTime_minute)
#     print(myHour,myMinute)
        
#     if(realTime_Hour==myHour and realTime_minute==myMinute):
#         print("지금이다")
#         quit()

#     timer = threading.Timer(3,Alarm)
#     timer.start()


# myHour_Input = input("알람설정할 시(H): ")
# myMinute_Input = input("알람설정할 분(M):")


# Alarm()