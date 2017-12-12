
Pyrename
====
Command line Batch renamer for Unix and Unix like OS


## Description

**Pyrename** is a command line renamer with sequential numbering. 
Each renaming process is applied separately for files and directories.

## License and Copyright

Copyright © 2010 - 2017 Gianluca Pernigotto   
Author and Developer: Gianluca Pernigotto   
Mail: <jeanlucperni@gmail.com>   
License: GPL3 (see LICENSE file in the docs folder)

## Requirements

python >=2.6


## Features

**Types of renaming consecutively numbered ordered:**

- Rename with a name and automatically assigns the numerical order.

- It adds a numerical ordered to the origin names, maintaining the 
alphanumeric order. The source names and extensions are not changed.

- Removes the progressive numbering previously applied with the above methods

**Rename with changes in strings methods:**

- Change or add certain strings to the names with the same match.
With this option you can also change the file extension, although 
it is encouraged to use the appropriate method (or addext extreplace), 
and you can delete them. 

- Adds strings to the names without any type of match (source names can 
be different for each file or folder), allowing us to determine the 
new string position, that is the beginning or end of the original 
name (but not of 'extension which remains the same).

**Extensions renaming methods:**

- Replaces the extensions encountered in a match: the renaming of
extensions is done by entering the extension you want to change in 
a group of files/folders.

- Adds extensions to files/folders who have none. Specifying
the prefix '-f' or 'd' if it determines the outcome for files or folders.


## Use

`pyrename |-f.|-d.| OPTION [DIRECTORY]`

**Prefix:**

-f.=FILES (process for renaming files only)   
-d.=FOLDERS (process of renaming only for folders)   

**Examples**

files rename: `pyrename -f.rename '/home/user/myphoto_album'`   
folders rename: `pyrename -d.rename '/home/user/myFolders'`   

**All options:**

*Rename with changes in strings methods:*

- rename
This method is a "do-everything", modify, add and replace certain strings to the names with the same match, but with the power to operate both on the names that the extensions. The method performs a consistency check, so if a match is not met warns: for example, when an object already exists with the same name of the objects that would be renamed (this is a security that will not overwrite files or folders). To rename the extensions, you should rely on the dedicated methods 'extreplace' or 'addext', unless you know what to do.

- addname
Adds strings to the names without any type of match (source names can be different for each object), allowing us to determine the position of the new string, in the head (head) or tail (tail) of the original name. If a match is not met warns: for example, when an object already exists with the same name (this is a security that will not overwrite any files).
This method does not take HAVE REGARD extension instead is kept unchanged.   

*Types of renaming consecutively numbered ordered:*

- namereplace
Completely replaces the names with a new unique name and automatically assigns the numerical order. The additional number is placed optionally in the head (head) or tail (tail) to the name of the objects. To add only and only the numbering is enough to leave the field empty renaming. Together with the numbering is place the character "underscore" for reasons of separation; if you want to change it or delete it use the method 'rename'.

- enumerate 
It adds to the names of origin numbered consecutively maintaining the alphanumeric order. The source names are not changed. The additional number is placed optionally in the head (head) or tail (tail) to the name of the objects.
Together with the numbering is place the character "underscore" for reasons of separation; if you want to change it or delete it use the method 'rename'.

- delnumerate
This method removes the numbering to objects that have previously been numbered with the method 'listed', but there are limitations: the objects must be numbered consecutively ordered starting at '1' and still ascending, otherwise the process will be partial and disorderly, or at best nothing will happen. If a match is not met warns: for example, when an object already exists with the same name of the objects that would be renamed (this is a security that will not overwrite files or folders).

*Extensions renaming methods:*

- extreplace
The method 'extreplace' is exclusive to the renaming of the sun extensions. It 'a safe method regarding the control of the names of existing objects. Replace extensions encountered in a match: renaming extensions done by entering the extension you want to change in a group of objects and the extension replacement, preserving all other files with a different extension or no extension. Specifying the prefix ('-f' or '-d') if it determines the outcome for files or folders. The inputs (input fields) can not be empty to avoid renaming incongruent. If implies the need to remove the extensions in a match, use the method 'rename'.

- addext
'addext', unlike 'extreplace', adds the desired extension only to objects that have no extension. The addition of the extension is done by entering the input with the chosen extension. Although this method is relatively safe as regards the control of the names of existing objects. The input (input field) can not be empty to avoid renaming incongruent. If implies the need to remove the extensions in a match, use the method 'rename'.

## Installation

pyrename not require installation, but if you are interested build an 
installable package, see below:

**Debian:**

Extra dependencies for build package with distutils:
`~# apt-get install python-all python-stdeb fakeroot`

Enter in unzipped sources folder and type (with not root):
`~$ python setup.py --command-packages=stdeb.command bdist_deb`

This should create a python-pyrename_version_all.deb in the new deb_dist directory.

see the setup.py script-file for more info on how-to build .deb package

**Slackware**

Is available a SlackBuild script to build a package *.tgz* for Slackware and Slackware based 
distributions. See here [pysplitcue.SlackBuild](https://github.com/jeanslack/slackbuilds/tree/master/pyrename)

Remember: install **pysetuptools** if not present first.
You can search on this site: [SlackBuild.org](http://slackbuilds.org/repository/14.1/python/pysetuptools/)

