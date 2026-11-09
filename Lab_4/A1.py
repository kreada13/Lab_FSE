import random
import time
N = int(input("Введите количество примеров: "))
correct = 0
example = 1
total_time = 0
for i in range(N):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    start_time = time.time()
    print(f"Вопрос {example}/{N}")
    example = example + 1
    while True:
        try:
            answer = int(input(f"{a} × {b} = "))
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")
    end_time = time.time()
    time_spend = time.time() - start_time
    total_time = total_time + (end_time - start_time)
    if answer == a * b:
        print(f"Верно! (Время: {time_spend:.1f} сек.)")
        correct = correct + 1
    else:
        print(f"Неверно! Правильно: {a * b} (Время: {time_spend:.1f} сек.)")
print("==================================================")
print("СТАТИСТИКА:")
print("==================================================")
print("Общее время:", round(total_time, 1), "секунд")
print("Среднее время на вопрос:", round(total_time / N, 1), "сек")
print("Правильных ответов:", correct, "/", N)
print("Процент правильных:", round(correct / N * 100, 1), "%")