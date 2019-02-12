'''f_n = open('test_file.txt', 'w')
f_n.write('сетевое программирование\n сокет\n декоратор')
f_n.close()
print(f_n)
'''

with open ('test_file.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str)