import sys

# libaspcm.so 
def sub_47a8(buffer):
    for i in range(len(buffer)):
        buffer[i] ^= 8

def main():
    b = bytearray(sys.stdin.read()[16:])
    sub_47a8(b)
    sys.stdout.write(b)

if __name__ == '__main__':
    main()
