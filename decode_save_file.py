import base64
import codecs
import magic

with open('output.txt', 'r') as file:
    lines = file.readlines()

hex = ''.join(lines)
b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()
file = base64.b64decode(b64)

with open("decoded_file", mode='wb') as end:
    end.write(file)

file_type = magic.from_file("decoded_file")
print(file_type)
