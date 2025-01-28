'''
Уявіть, що вам на технічному інтерв'ю дають наступну задачу, яку треба розв'язати за допомогою купи.

Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, використовуючи з'єднувачі, у порядку, який призведе до найменших витрат. Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів.

Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.

'''

import heapq

def minimize_costs(cable):
    heapq.heapify(cable)
    
    total_costs = 0
    
    while len(cable) > 1:     
        min_1 = heapq.heappop(cable)
        min_2 = heapq.heappop(cable)
        value = min_1 + min_2
        total_costs += value
        heapq.heappush(cable, value)
    
    return total_costs

cables_length = [4, 13, 5, 6, 9, 1]
result = minimize_costs(cables_length)
print(f"Мінімальні витрати =", result,"$")
