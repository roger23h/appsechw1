import struct
import sys

# We build the content of the file in a byte string first
# This lets us calculate the length for the header at the end
data = b''
data += b"A"*32 # Merchant ID
data += b"B"*32 # Customer ID
data += struct.pack("<I", 1) # One record
# Record of type animation
data += struct.pack("<I", 8 + 32 + 256) # Record size (4 bytes)
data += struct.pack("<I", 3)            # Record type (4 bytes)
data += b"A"*31 + b'\x00'               # Note: 32 byte message
#data+= b'\x00'*252
data+=b'\x04'
data+=b'\x16\x16'
#data+=struct.pack("<I",16)
#data += b'\x08' + b'\x0022\x0122\x0222\x0322\x0422\x0522\x0622\x0722\x0822\x0922\x1022'.ljust(256, b' ')# * 256                   # Program made entirely of "end program" (256 bytes)

f = open(sys.argv[1], 'wb')
datalen = len(data) + 4 # Plus 4 bytes for the length itself
f.write(struct.pack("<I", datalen))
f.write(data)
f.close()
