# pc@DESKTOP-3QUJ44S MINGW64 ~
# $ pwd
# /c/Users/pc

# pc@DESKTOP-3QUJ44S MINGW64 ~
# $ ls
#  AppData/             Downloads/              'My Documents'@                                                                                 OneDrive/       SendTo@           ntuser.ini
# 'Application Data'@   Favorites/               NTUSER.DAT                                                                                     Pictures/      'Start Menu'@
#  Contacts/            IntelGraphicsProfiles/   NTUSER.DAT{ec4691a0-a057-11ed-939a-a4fc7720782c}.TM.blf                                        PrintHood@      Templates@
#  Cookies@             Links/                   NTUSER.DAT{ec4691a0-a057-11ed-939a-a4fc7720782c}.TMContainer00000000000000000001.regtrans-ms   Recent@         Videos/
#  Desktop/            'Local Settings'@         NTUSER.DAT{ec4691a0-a057-11ed-939a-a4fc7720782c}.TMContainer00000000000000000002.regtrans-ms  'Saved Games'/   ntuser.dat.LOG1
#  Documents/           Music/                   NetHood@                                                                                       Searches/       ntuser.dat.LOG2

# pc@DESKTOP-3QUJ44S MINGW64 ~
# $ cd desktop

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop
# $ cd dev

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev
# $ cd git

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git
# $ cd class1
# bash: cd: class1: No such file or directory

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git
# $ ls
# 'class 1'/

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git
# $ cd class 1
# bash: cd: too many arguments

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git
# $ cd 'class 1'

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git/class 1
# $ git int
# git: 'int' is not a git command. See 'git --help'.

# The most similar command is
#         init

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git/class 1
# $ git init
# Initialized empty Git repository in C:/Users/pc/Desktop/dev/git/class 1/.git/

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git/class 1 (master)
# $ touch love

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git/class 1 (master)
# $ ls
# love

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git/class 1 (master)
# $ rm -f love

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git/class 1 (master)
# $ ls

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git/class 1 (master)
# $ touch love.py

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git/class 1 (master)
# $ ls
# love.py

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git/class 1 (master)
# $ code .

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git/class 1 (master)
# $ git status
# On branch master

# No commits yet

# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         love.py

# nothing added to commit but untracked files present (use "git add" to track)

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git/class 1 (master)
# $

# git status check the status of your project

# git add . is used to add multiple files
# Omit --global to set the identity only in this repository.

# fatal: unable to auto-detect email address (got 'pc@DESKTOP-3QUJ44S.(none)')

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git/class 1 (master)
# $ git commit -m'my first commit'
# Author identity unknown

# *** Please tell me who you are.

# Run

#   git config --global user.email "you@example.com"
#   git config --global user.name "Your Name"

# to set your account's default identity.
# Omit --global to set the identity only in this repository.

# fatal: unable to auto-detect email address (got 'pc@DESKTOP-3QUJ44S.(none)')

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git/class 1 (master)
# $ ^C

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git/class 1 (master)
# $ git config --global user.email "onyedikachukwu.okere@gmail.com"

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git/class 1 (master)
# $ git config --global user.name "love"

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git/class 1 (master)
# $ git commit -m'my first commit'
# [master (root-commit) 07f046a] my first commit
#  1 file changed, 89 insertions(+)
#  create mode 100644 love.py

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git/class 1 (master)
# $ git status
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git restore <file>..." to discard changes in working directory)
#         modified:   love.py

# no changes added to commit (use "git add" and/or "git commit -a")

# pc@DESKTOP-3QUJ44S MINGW64 ~/desktop/dev/git/class 1 (master)
# $

print('hello am learning git')
