import json

import matplotlib.pyplot as plt


def get_data_from_json(memory: list, cpu: list) -> None:
    '''Берет данные из Json и парсит их'''
    with open('outout.json', 'r') as file:
        data = json.load(file)
        for item in data:
            memory.append((item[1], item[2]))
            cpu.append((item[0], item[2]))


def draw_graph(lst: list, name: str) -> None:
    '''
    Строит график
    lst: list - список в котором хранятся данные
    name: strin - название графика
    '''

    x, y = [i[0] for i in lst], [i[1] for i in lst]
    plt.plot(y, x)
    plt.title(f'{name} graph')
    plt.xlabel('Time')
    plt.ylabel(f'{name}')

    plt.show()


if __name__ == '__main__':
    memory_time = []
    cpu_time = []
    get_data_from_json(memory_time, cpu_time)
    draw_graph(memory_time, 'Memory')
    draw_graph(cpu_time, 'CPU')

