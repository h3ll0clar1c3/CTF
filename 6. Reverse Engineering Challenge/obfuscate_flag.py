flag = "CTF{reverse_flag}"
obfuscated_flag = [ord(c) + 3 for c in flag]  # Simple Caesar cipher
print("Obfuscated flag:", obfuscated_flag)