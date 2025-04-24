## 1. SQL Injection Challenge

Description: 

Create a web app with a login form vulnerable to SQL injection. The challenge is to extract a hidden flag from the database.

Implementation Steps:

1. Use Python with Flask to create a web application.
2. Add a login form that directly concatenates user inputs into an SQL query.
3. Store the flag in the database.


## 2. XSS Challenge

Description: 

Participants must execute a reflected XSS payload to reveal the flag.

Implementation Steps:

1. Create an HTML page with a vulnerable search form.
2. Display user input without sanitization.


## 3. Steganography Challenge

Description: 

Embed a flag into an image using steganography.

Implementation Steps:

1. Use the pillow Python library to encode hidden text into an image.
2. Save the image as the challenge file.


## 4. Weak Encryption Challenge

Description: 

Break a weak XOR cipher to reveal the flag.

Implementation Steps:

1. Create a Python script to encrypt the flag with XOR.
2. Provide the encrypted flag and key.


## 5. Buffer Overflow Challenge

Description: 

Exploit a buffer overflow in a C program to reveal the flag.

Implementation Steps:

1. Write a vulnerable C application.
2. Compile the program with debugging symbols.


## 6. Reverse Engineering Challenge

Description: 

Reverse engineer a binary to retrieve the flag.

Implementation Steps:

1. Write a C program that obfuscates the flag.
2. Compile and provide the binary.


## 7. Packet Analysis Challenge

Description: 

Analyze a PCAP file to retrieve the flag.

## Folder Structure

https://github.com/h3ll0clar1c3/CTF/blob/main/Folder%20Structure.png

Implementation Steps:

1. Use scapy to generate a PCAP file with HTTP data.
2. Embed the flag in the HTTP payload.
