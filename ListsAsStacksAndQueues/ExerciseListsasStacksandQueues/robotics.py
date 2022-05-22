from collections import deque


def read_robots():
    result = {}
    robots_input = input().split(';')
    for robot_input in robots_input:
        struct = robot_input.split('-')
        name, sec = struct[0], int(struct[1])
        result[name] = sec
    return result


def to_seconds(hours, minutes, sec):
    return hours * 60 * 60 + minutes * 60 + sec


def read_products():
    result = deque()
    while True:
        command = input()
        if command == 'End':
            break
        result.append(command)
    return result


def to_time_string(time_in_seconds):
    hours = time_in_seconds // 3600
    minutes = (time_in_seconds % 3600) // 60
    seconds = (time_in_seconds % 3600) % 60
    return f'[{hours:02d}:{minutes:02d}:{seconds:02d}]'


robots = read_robots()
available_robots = [r for r in robots.keys()]
procesing_robots = {}
starting_times_parts = [int(x) for x in input().split(':')]
time_in_seconds = to_seconds(starting_times_parts[0], starting_times_parts[1], starting_times_parts[2])
products = read_products()

while products:
    time_in_seconds = (time_in_seconds + 1) % (24 * 60 * 60)
    for robot_name in [k for k in procesing_robots.keys()]:
        procesing_robots[robot_name] -= 1
        if procesing_robots[robot_name] == 0:
            procesing_robots.pop(robot_name)
    current_products = products.popleft()
    for robot_name in available_robots:
        if robot_name not in procesing_robots:
            print(f'{robot_name} - {current_products} {to_time_string(time_in_seconds)}')
            procesing_robots[robot_name] = robots[robot_name]
            break
    else:
        products.append(current_products)
