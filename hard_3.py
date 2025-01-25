import math

def decode_hamming_code(message):
    answer = []
    error = 0
    control_bit = 0

    for i in range(len(message)):
        if message[i] == '1':
            error ^= i + 1
        if i + 1 == 1 << control_bit:
            control_bit += 1
            continue
        answer.append(message[i])

    # проверяем, что ошибка - это не контрольный бит
    if (error & (error - 1)) != 0:
        print(error)
        index = error - int(math.log(error, 2))
        answer[index] = '0' if answer[index] == '1' else '1'

    return ''.join(answer)

def format_output(decoded_message):
    pairs =  ' '.join(decoded_message[i:i+2] for i in range(0, len(decoded_message), 2))
    pairs = pairs.replace("00", "A").replace("01", "T").replace("10", "C").replace("11", "G")
    return pairs

print(format_output(decode_hamming_code("11100010111010101011000101001")))
