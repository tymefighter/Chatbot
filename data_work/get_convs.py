import pickle

def main():

    fl = open('../data/chatbot_data/crude_convs.txt', 'r', encoding="utf8", errors='ignore')
    fl_ip = open('../data/chatbot_data/input_data', 'w')
    fl_op = open('../data/chatbot_data/output_data', 'w')

    count = 0

    for line in fl.readlines():
        arr = (line.split())[8:]
        line = ""
        for x in arr:
            line += str(x) + " "
        
        if count % 2 == 0:
            fl_ip.write(line + '\n')
        else:
            fl_op.write(line + '\n')
        
        count += 1
    if count % 2 == 1:
        fl_op.write('nothing\n')

    fl.close()
    fl_ip.close()
    fl_op.close()

if __name__ == '__main__':
    main()