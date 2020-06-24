"""模拟主程序"""
from print_task.printer import Printer
from print_task.task import Task
from my_queue import MyQueue


def simulation(seconds, print_speed):
    printer = Printer(print_speed)
    print_queue = MyQueue()
    wait_time_list = []

    for current_second in range(seconds):
        if Task.new_task():
            task = Task(current_second)
            print_queue.enqueue(task)
        if printer.busy() or print_queue.is_empty():
            pass
        else:
            new_task = print_queue.dequeue()
            wait_time_list.append(new_task.wait_time(current_second))
            printer.start_next(new_task)
        printer.tick()

    average_wait_time = sum(wait_time_list)/len(wait_time_list)
    print(f'Average wait {average_wait_time:6.2f}, {print_queue.size():3d} tasks remaining')


for i in range(20):
    simulation(3600, 5)

print('\n===========================================\n')

for i in range(20):
    simulation(3600, 10)
