from function import *

while True:
    msg : str = askMsg()
    if msg == "q" or msg == "Q":
        break
    num : int = askNum()
    for i in range(num):
        print(msg)