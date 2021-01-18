n = int(input())

for _ in range(n):
    msg = input()

    sq = int(len(msg) ** 0.5)

    box_square = [msg[i:i+sq] for i in range(0, len(msg), sq)]

    encoded_msg = [""] * len(msg)

    for i in range(len(box_square)):
        start = i
        rev = box_square[i][::-1]
        for a in rev:
            encoded_msg[start] = a
            start += sq

    print("".join(encoded_msg))