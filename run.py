import os, platform
bit = platform.architecture()[0]
if bit == '64bit':
    import urlb
else:
    import urlb32
