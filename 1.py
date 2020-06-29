import sys

sys.setrecursionlimit(1500)


def encrypt(encrypted_text, n):
    if n >= 1:

        n -= 1
        encrypted_text1 = encrypted_text[::2]
        encrypted_text2 = encrypted_text[1::2]
        encrypted_text = encrypted_text2 + encrypted_text1
        return encrypt(encrypted_text, n)
    else:
        return encrypted_text


def decrypt(text, n):
    if n >= 1:
        n -= 1
        if len(text) % 2 == 0:
            d = ''
            a = text[:len(text) // 2]
            b = text[len(text) // 2:]
            for i in range(len(a)):
                d = d + b[i] + a[i]
            return decrypt(d, n)
        else:
            d = ''
            a = text[:len(text) // 2]
            b = text[len(text) // 2:]

            for i in range(0, len(b)):
                if len(a) - 1 >= i:
                    d = d + b[i] + a[i]
                else:
                    d = d + b[i]
            return decrypt(d, n)
    else:
        return text

print(encrypt('Юрка молодец!12313',1))
print(decrypt('рамлдц133Юк оое!21',1))
