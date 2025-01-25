import heapq

def huffman_coding(text):
    # Подсчет частоты символов
    frequencies = {}
    for char in text:
        frequencies[char] = frequencies.get(char, 0) + 1

    # Преобразование частот в список
    freq_list = list(frequencies.values())
    heapq.heapify(freq_list)

    total_cost = 0
    while len(freq_list) > 1:
        first = heapq.heappop(freq_list)
        second = heapq.heappop(freq_list)
        total_cost += first + second
        heapq.heappush(freq_list, first + second)

    return total_cost;

print(huffman_coding("2h2.+.o2.=.2h2o"))
