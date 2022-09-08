import os
import threading

#
# sth = [0]
#
#
# def count(sth, threshold):
#     for i in range(threshold):
#
#         print("{}".format(threading.current_thread().name))
#
#         sth[0] += 1
#
#
#
#
# t1 = threading.Thread(target = count, args = (sth,10), name = 't1')
#
# t2 = threading.Thread(target = count, args = (sth,20), name = 't2')
#
# t1.start()
#
#
# t2.start()
#
#
# for i in range(10):
#     print(sth)
#
# t1.join()
#
# t2.join()


txt = "Name: SThh\nAge: wwww\nWwww: iiiii"

x = txt.split("\n")

print(x.split(" "))
