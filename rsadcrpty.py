from math import gcd

# Finding modular inverse: https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

e = 65537
c = 1415060907955076984980255543080831671725408472748
p = 255097177
q = 22034393943473183756163118460342519430053
n = p*q
phi = (p-1)*(q-1)

d = modinv(e,phi)

try:
    # Get plaintext in integer format
    plaintext = pow(c,d,n)
    # Convert the integer to bytes, then to a string
    flag = plaintext.to_bytes((plaintext.bit_length() + 7) // 8,byteorder='big').decode('ascii')
    print(flag)
except Exception:
    print("Decryption failed")
