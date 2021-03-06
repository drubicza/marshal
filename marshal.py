#!/usr/bin/env python
import marshal, sys, os, platform
from time import sleep
B = '\x1b[34m'
R = '\x1b[31m'
G = '\x1b[32m'
W = '\x1b[0m'
Y = '\x1b[33;5m'
input = '%s[%s+%s] %sFile Name%s: %s' % (R, Y, R, W, B, W)

def clear():
    if 'linux2' or 'linux' or 'unix' in sys.platform:
        os.system('clear')
    else:
        if 'win' in sys.platform:
            os.system('cls')
        else:
            os.system('clear')


def banner():
    print '%s\n +%s===============================%s+%s\n| %sCoded By %s: %sGunadiCBR            %s|\n| %sGitHub   %s: %sgithub.com/afelfgie  %s|\n%s +%s===============================%s+\n' % (R, B, R, R, Y, R, W, R, Y, R, W, R, R, B, R)


def repro():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    curdir = os.getcwd()


try:
    clear()
    banner()
    file = raw_input(input)
    o = file.replace('.py', '')
except IndexError:
    print ''
    print ('Are you using python version {}').format(sys.argv[0])
    print 'Please, use version 2.X of python'
    sys.exit()
else:
    try:
        strng = open(file, 'r').read()
    except IOError as e:
        print ''
        print '%s[%s-%s] %sERROR: %s%s' % (R, B, R, R, W, e)
        print ''
        sleep(2)
        repro()

    try:
        code = compile(strng, '<GunadiCBR>', 'exec')
        data = marshal.dumps(code)
    except TypeError:
        banner()
        print '%s[%s!%s] %sfile already compiled' % (R, B, R, W)
        print ''
        sys.exit()

fileout = open(o + 'M.py', 'wb')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads(' + repr(data) + '))')
fileout.close()
clear()
banner()
print '%s[%s+%s] %sFile Saved%s: %s%sM.py' % (R, B, R, Y, R, W, o)
print ''
sys.exit()
