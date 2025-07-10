# import random

# import matplotlib.pyplot as plt


class BioTuringMachine:
    def __init__(self, rna_tape):
        self.tape = list(rna_tape)  # РНК-лента
        self.head_pos = 0  # Позиция головки
        self.state = "q0"  # Начальное состояние
        self.rules = {  # Таблица правил
            ("q0", "C"): ("q1", "C", 1),  # Нашли C → переходим в q1
            ("q0", "*"): ("q0", None, 1),  # Игнорируем другие символы
            ("q1", "A"): ("q1", "U", 1),  # Инверсия A → U
            ("q1", "U"): ("q1", "A", 1),  # Инверсия U → A
            ("q1", "G"): ("q0", "G", 1),  # Нашли G → возврат в q0
            ("q1", "*"): ("q1", None, 1),  # Пропускаем другие символы
        }

    def step(self):
        current_symbol = self.tape[self.head_pos]
        rule = None

        # Ищем подходящее правило
        for (state, symbol), (new_state, new_symbol, move) in self.rules.items():
            if state == self.state and (symbol == current_symbol or symbol == "*"):
                rule = (new_state, new_symbol, move)
                break

        if not rule:
            raise ValueError(f"No rule for state={self.state}, symbol={current_symbol}")

        # Применяем правило
        new_state, new_symbol, move = rule
        if new_symbol is not None:
            self.tape[self.head_pos] = new_symbol  # Заменяем символ
        self.state = new_state  # Меняем состояние
        self.head_pos += move  # Двигаем головку

        # Проверка конца ленты
        return self.head_pos < len(self.tape)

    def run(self):
        while self.step():
            print(f"Шаг: {self.head_pos}, Состояние: {self.state}, Лента: {''.join(self.tape)}")
        return "".join(self.tape)


# Пример использования
rna_tape = "CAAUGUCUUAG"  # Инвертируем участки между C и G
machine = BioTuringMachine(rna_tape)
result = machine.run()
print(f"Результат: {result}")


# class AdvancedBioTM(BioTuringMachine):
#     def __init__(self, rna_tape):
#         super().__init__(rna_tape)
#         self.error_rate = 0.05  # 5% вероятность ошибки

#     def step(self):
#         if random.random() < self.error_rate:
#             # Ошибка: головка пропускает шаг
#             self.head_pos += 1
#             return self.head_pos < len(self.tape)
#         return super().step()


# Тестируем с шумом
# noisy_machine = AdvancedBioTM("CAAUGUCUUAG")
# print(f"Результат с шумом: {noisy_machine.run()}")


# def plot_head_movement(machine):
#     positions = range(len(machine.tape))
#     plt.plot(positions, [ord(s) for s in machine.tape], "b-")
#     plt.xlabel("Позиция на РНК")
#     plt.ylabel("Нуклеотид (ASCII-код)")
#     plt.title("Движение головки машины Тьюринга")
#     plt.show()


# plot_head_movement(machine)
