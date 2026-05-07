
d=input("Data: "); v=input("Div: ")
n=len(v); t=d+'0'*(n-1)

for i in range(len(d)):
    if t[i]=='1':
        t=t[:i]+''.join('0' if t[i+j]==v[j] else '1' for j in range(n))+t[i+n:]

c=t[-(n-1):]; code=d+c
print("CRC:",c,"\nCodeword:",code)

r=input("Received: "); t=r
for i in range(len(r)-n+1):
    if t[i]=='1':
        t=t[:i]+''.join('0' if t[i+j]==v[j] else '1' for j in range(n))+t[i+n:]

print("Error Detected!" if '1' in t[-(n-1):] else "No Error")




# CRC (Cyclic Redundancy Check)

# CRC is an error detection technique used in computer networks to detect errors during data transmission.

# Working:
# 1. Sender divides data using a generator key.
# 2. The remainder obtained is called CRC.
# 3. CRC is added to the data and transmitted.
# 4. Receiver performs the same division.
# 5. If remainder = 0 → No Error
#    If remainder ≠ 0 → Error Detected


# Example

# Data Bits : 11001
# Key       : 101

# Sender Side:

# Append 2 zeros to data:
# 11001 → 1100100


#         101
#       --------
# 101 ) 1100100
#       101
#       ---
#        110
#        101
#        ---
#         111
#         101
#         ---
#          10   ← CRC


# CRC = 10

# Codeword Sent:
# 11001 + 10 = 1100110


# Receiver Side:

#         101
#       --------
# 101 ) 1100110
#       101
#       ---
#        110
#        101
#        ---
#         111
#         101
#         ---
#          101
#          101
#          ---
#          000


# Remainder = 000

# All zeros → No Error
# Non-zero remainder → Error Detected