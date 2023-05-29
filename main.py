from Crypto.Cipher import AES
import binascii

key = binascii.unhexlify('000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f')

cipher = AES.new(key, AES.MODE_ECB)
msg = cipher.encrypt(binascii.unhexlify('00112233445566778899aabbccddeeff'))

print(binascii.hexlify(msg))
