import os, platform
bit = platform.architecture()[0]
if bit == '64bit':
    import urlb
elif bit == '32bit':
    import urlb32
else:
    print('noe')
    exit()
