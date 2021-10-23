# используется для сортировки
from operator import itemgetter
 
class Computer:
    def __init__(self, id, name, browser_id):
        self.id = id
        self.name = name
        self.browser_id = browser_id

class Browser:
    def __init__(self, id, name, memory_on_disk):
        self.id = id
        self.name = name
        self.memory_on_disk = memory_on_disk

class CompBrowser:
    """
    'Браузеры компьютера' для реализации 
    связи многие-ко-многим
    """
 
    def __init__(self, comp_id, browser_id):
        self.comp_id = comp_id
        self.browser_id = browser_id
 
# Компьютеры
computers = [
    Computer(1, 'Ноутбук ASUS A540L',1),
    Computer(2, 'Компьютер HYPERPC NANO X',2),
    Computer(3, 'Компьютер HYPERPC VOLT',3),
    Computer(4, 'Ноутбук ASUS A540NV',5),
    Computer(5, 'Компьютер ASUS A8',4),
    Computer(6, 'Ноутбук ASUS A9',2),
]

# Браузеры
browsers = [
    Browser(1, 'Google Chrome', 350),
    Browser(2, 'Яндекс.Браузер', 250),
    Browser(3, 'Mozilla Firefox', 400),
    Browser(4, 'Opera', 300),
    Browser(5, 'Safari', 280),
]
 
comps_browsers = [
    CompBrowser(1, 1),
    CompBrowser(2, 3),
    CompBrowser(3, 2),
    CompBrowser(3, 4),
    CompBrowser(4, 1),
    CompBrowser(4, 3),
    CompBrowser(5, 2),
    CompBrowser(6, 3),
    CompBrowser(6, 4),
    CompBrowser(6, 5),
]
 
def main():
    """Основная функция"""
 
   # Соединение данных один-ко-многим
    one_to_many = [(b.name, b.memory_on_disk, c.name)
                   for c in computers
                   for b in browsers
                   if c.browser_id == b.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(b.name, cb.comp_id, cb.browser_id)
                         for b in browsers
                         for cb in comps_browsers
                         if b.id == cb.browser_id]

    many_to_many = [(c.name, b_name)
                    for b_name, comp_id, browser_id in many_to_many_temp
                    for c in computers if c.id == comp_id]
                    
    print('Задание Д1')
    res_11 = [( c.name, b.name, b.memory_on_disk) 
        for c in computers
        for b in browsers
        if c.browser_id == b.id and c.name.startswith('Компьютер')]
    print(res_11)
    
    print('Задание Д2')
    res_12_unsorted = []
    # Перебираем все компьютеры
    for c in computers:
        # Список браузеров компьютера
        c_browsers = list(filter(lambda i: i[2]==c.name, one_to_many))
        # Если компьютер не пустой        
        if len(c_browsers) > 0:
            # память на диске браузера
            b_memory = [memory_on_disk for _,memory_on_disk,_ in c_browsers]
            # Средняя память на диске
            b_memory_mean = sum(b_memory) / len(b_memory)
            res_12_unsorted.append((c.name, b_memory_mean))
            
    # Сортировка по памяти
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('Задание Д3')
    res_13 = {}
    # Перебираем все браузеры
    for b in browsers:
        if b.name.startswith('O'):
            # Список компьютеров браузера
            comps_of_b = list(filter(lambda i: i[1]==b.name, many_to_many))
            # Только названия компьютеров
            comps_names = [x for x,_ in comps_of_b]
            # Добавляем результат в словарь
            # ключ - браузер, значение - список названий
            res_13[b.name] = comps_names
 
    print(res_13)
if __name__ == '__main__':
    main()
