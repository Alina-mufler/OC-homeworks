#!/usr/bin/python3

# Федорова Алина, 11-902

import random
import time
import os
import sys

arg = sys.argv[1]
pid = os.getpid()
print('Запущена программа Child в процессе с PID {} с аргументом {}'.format(pid, arg))
time.sleep(int(arg))
print('Завершился процесс с PID {}'.format(pid))
exit_number = random.randint(0, 1)
os._exit(exit_number)
