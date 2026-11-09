packets = input("Введите строку из 0 и 1: ")
while len(packets) < 5 or packets.count("0") + packets.count("1") != len(packets):
    print("Ошибка! Введите только 0 и 1, минимум 5 символов.")
    packets = input("Введите строку ещё раз: ")
total = len(packets)
lost = packets.count("0")
longest = 0
current = 0
for packet in packets:
    if packet == "0":
        current = current + 1
        if current > longest:
            longest = current
    else:
        current = 0
loss_percent = lost / total * 100
if loss_percent <= 1:
    quality = "отличное"
elif loss_percent <= 5:
    quality = "хорошее"
elif loss_percent <= 10:
    quality = "удовлетворительное"
elif loss_percent <= 20:
    quality = "плохое"
else:
    quality = "критическое состояние сети"
print()
print("Общее количество пакетов:", total)
print("Количество потерянных пакетов:", lost)
print("Длина самой длинной последовательности потерянных пакетов:", longest)
print("Процент потерь:", round(loss_percent, 1), "%")
print("Качество связи:", quality)