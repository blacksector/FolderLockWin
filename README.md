FolderLockWin
=============

This is a small Python 2.7 Program that allows you to lock a folder. This is just a demo, not designed to be used in production states.

Docs
=====

FolderLockWin was designed from scratch using Python 2.7 and a windows BATCH program. The program simply renames a folder but when renamed it is a hidden system in Windows that locks the folder, and even after the Hidden files are shown on windows, the folder CANNOT be accessed. As of Windows XP, Vista, 7. Windows 8 has NOT been tested yet.

INSTALL
=======
You can easily run the script from the Python Shell, or you can compile it, please use windows, as this is not supported for *nix operating systems.

For the compiling:
1. Install py2exe from here: http://sourceforge.net/projects/py2exe/
2. Open up CMD from windows. (Ctrl + R; then type "CMD")
3. Now, CD into the directory with this program. For example: "cd D:\Dev\Python\LockFolder\"
4. Now type this: "python setup.py py2exe"

Enjoy! And good luck, it should finish the build and the files need to be copied are in the DIST folder.
