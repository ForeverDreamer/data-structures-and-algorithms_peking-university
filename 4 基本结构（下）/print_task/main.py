"""模拟主程序"""
from print_task.printer import Printer
from print_task.task import Task
from my_queue import MyQueue


def simulation(seconds, print_speed):
    printer = Printer(print_speed)
    print_queue = MyQueue()
    wait_time_list = []

    for current_second in range(seconds):
        # 是否有新任务提交
        if Task.new_task():
            task = Task(current_second)
            print_queue.enqueue(task)
        # 是否开始新任务
        if (not printer.busy()) and (not print_queue.is_empty()):
            new_task = print_queue.dequeue()
            wait_time_list.append(new_task.wait_time(current_second))
            printer.start_next(new_task)
        # 时间流逝一个单位
        printer.tick()
    average_wait_time = sum(wait_time_list)/len(wait_time_list)
    print(f'Average wait {average_wait_time:6.2f}, {print_queue.size():3d} tasks remaining')


for i in range(20):
    # 模拟1小时，打印速度每分钟5页(5pages/60seconds)
    simulation(3600, 5)

print('\n===========================================\n')

for i in range(20):
    # 模拟1小时，打印速度每分钟10页
    simulation(3600, 10)
