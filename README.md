================================================================================ 
Command line Batch renamer for Unix and Unix like OS
================================================================================ 


--------------------------------------------------------------------------------

Copyright © 2010 - 2015 jeanslack 
 
  Author and Developer: jeanslack 
  Mail: <jeanlucperni@gmail.com>
  License: GPL3 (see LICENSE file in the docs folder)

--------------------------------------------------------------------------------

Description:
------- 

Pyrename is written entirely in python, It uses the command line (cli)
and from the options is also available with sequential numbering. Each 
process is applied separately or renaming the files or folders.


Dependencies:
-------

python >=2.6


Features:
-------
 
Types of renaming consecutively numbered ordered :

* Rename with a name and automatically assigns the numerical order.

* It adds a numerical ordered to the origin names, maintaining the 
alphanumeric order. The source names and extensions are not changed.

* Removes the progressive numbering previously applied with the above methods

Rename with changes in strings methods :

* Change or add certain strings to the names with the same match.
With this option you can also change the file extension, although 
it is encouraged to use the appropriate method (or addext extreplace), 
and you can delete them. 

* Adds strings to the names without any type of match (source names can 
be different for each file or folder), allowing us to determine the 
new string position, that is the beginning or end of the original 
name (but not of 'extension which remains the same).

Extensions renaming methods : 

* Replaces the extensions encountered in a match: the renaming of
extensions is done by entering the extension you want to change in 
a group of files/folders.

* Adds extensions to files/folders who have none. Specifying
the prefix '-f' or 'd' if it determines the outcome for files or folders.


Use
-------

Open a terminal window and type:

		pyrename -h


Installation
-------

--------------------------------------------------------------------------------

DEBIAN:

--------------------------------------------------------------------------------

Extra dependencies for build package with distutils:

		# apt-get install python-all python-stdeb fakeroot

Enter in unzipped sources folder and type (with not root):

		python setup.py --command-packages=stdeb.command bdist_deb

This should create a python-pyrename_version_all.deb in the new deb_dist directory.

see the setup.py script-file for more info on how-to build .deb package

--------------------------------------------------------------------------------

SLACKWARE:

--------------------------------------------------------------------------------

First require pysetuptools at: [slackbuild.org](http://slackbuilds.org/repository/14.1/python/pysetuptools/)

Is available a SlackBuild script to build package .tgz for Slackware distribution that you can see 
here: [My-Repo-Slackware](https://github.com/jeanslack/My-Repo-Slackware/tree/master/slackware/utilities/pyrename)

If you want download entire content directory quickly, open a terminal window and type:

		svn checkout https://github.com/jeanslack/My-Repo-Slackware/trunk/slackware/utilities/pyrename

Then download the pyrename tarball source code: [pyrename-0.9.tar.gz/releases](https://github.com/jeanslack/pyrename/releases)

..and place it into the unzipped slackbuild folder .

For instructions on how to use the SlackBuilds, see:

[http://slackbuilds.org/howto/](http://slackbuilds.org/howto/)

[http://www.slackwiki.com/SlackBuild_Scripts](http://www.slackwiki.com/SlackBuild_Scripts)

[http://www.slacky.eu/slacky/Slackware_%26_SlackBuild](http://www.slacky.eu/slacky/Slackware_%26_SlackBuild)

Remember: first install pysetuptools

--------------------------------------------------------------------------------

