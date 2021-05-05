def main():
    with open('hex.txt', 'r') as r:
        with open('bin', 'wb') as wb:
            line = r.readline()
            while line:
                wb.write(bytearray(map(lambda e: int(e, 16), line[12:59].split(' '))))
                line = r.readline()

if __name__ == '__main__':
    main()
