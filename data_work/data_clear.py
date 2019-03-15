def main():

    fl = open('../data/corpus1', 'r')
    fl2 = open('../data/corpus1_clear', 'w')

    for line in fl.readlines():
        s = ""
        for c in line:
            if c in ".,:;'?":
                s += ' '
            else:
                s += c
        fl2.write(s)
    
    fl.close()
    fl2.close()

if __name__ == '__main__':
    main()