word1 = 'разработка'
en_word1 = word1.encode('utf-8')
print(en_word1)
word1_b = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
de_word1 = bytes.decode(word1_b, 'utf-8')
print(de_word1)

word2 = 'администрирование'
en_word2 = word2.encode('utf-8')
print(en_word2)
word2_b = b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'
de_word2 = bytes.decode(word2_b, 'utf-8')
print(de_word2)

word3 = 'protocol'
en_word3 = word3.encode('utf-16')
print(en_word3)
word3_b = b'\xff\xfep\x00r\x00o\x00t\x00o\x00c\x00o\x00l\x00'
de_word3 = bytes.decode(word3_b, 'utf-16')
print(de_word3)

word4 = 'standart'
en_word4 = word4.encode('utf-16')
print(en_word4)
word4_b = b'\xff\xfes\x00t\x00a\x00n\x00d\x00a\x00r\x00t\x00'
de_word4 = bytes.decode(word4_b, 'utf-16')
print(de_word4)