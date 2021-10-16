#!/usr/bin/python3

# Федорова Алина, 11-902

import random
import os
import sys

print("Введите количество дочерних процессов больше 1")
arg = sys.argv
if len(arg) > 1:
    n = int(arg[1])
    process = []
    for i in range(n):
        pid = os.fork()
        if pid > 0:
            exit_number = os.wait()
            print('Дочерний процесс с PID {} завершился. Статус завершения {}.'.format(pid, exit_number))
        else:
            os.execl("./child.py", "child.py", str(random.randint(5, 10)))
else:
    print("Количество дочерних процессов неверное")
