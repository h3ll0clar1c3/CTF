# File: weak_encryption.py
def xor_encrypt_decrypt(data, key):
    return ''.join(chr(ord(c) ^ key) for c in data)

# Encrypt the flag
flag = "CTF{weak_encryption_flag}"
key = 42
encrypted_flag = xor_encrypt_decrypt(flag, key)
print("Encrypted flag:", encrypted_flag)