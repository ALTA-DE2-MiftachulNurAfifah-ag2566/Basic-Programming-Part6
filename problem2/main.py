def caesar(offset, input_str):
    huruf = {chr(i + ord('a')): chr((i + offset) % 26 + ord('a')) for i in range(26)}
    huruf.update({chr(i + ord('A')): chr((i + offset) % 26 + ord('A')) for i in range(26)})
    return "".join(huruf.get(c, c) for c in input_str)

if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl