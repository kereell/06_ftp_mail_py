#!/usr/bin/env python3
from ftplib import FTP

host = 'files.000webhost.com'
user = 'olorius'
password = 'aU&PeToVQRzMZZAgM%jF'

# host = 'kereell.bplaced.net'
# user = 'kereell'
# password = 'MnHQe6Ul7WssWq4V'


with FTP(host) as ftp:
    ftp.login(user=user, passwd=password)
    print(ftp.getwelcome())
    print("PWD:", ftp.pwd())
    ftp.dir()
    ftp.cwd(input("What dir I should go? "))
    ftp.dir()
    downfile = input("What file should I download? ")
    ftp.retrbinary("RETR" + downfile, open(downfile, "wb").write)
    ftp.debug()
