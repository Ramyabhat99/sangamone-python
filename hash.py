import hashlib as hs
hash_md5 = hs.md5()
with open('E:/Assignments/assgnmnt_19-Mar-2022/abc.txt', 'rb') as file:
    buffer = file.read()
    hash_md5.update(buffer)
print('Hash of file is:', hash_md5.hexdigest())
