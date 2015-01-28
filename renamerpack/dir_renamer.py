#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# PROGRAM-NAME: pyrename
# VERSION: v0.9
# DESCRIPTION: module batch renaming for folder
# AUTHOR: Gianluca jeanslack Pernigotto <jeanlucperni@gmail.com>
# LICENSE: Copyright (c) Gianluca jeanslack Pernigotto GPL 3 
# FIRST RELEASE: v0.8 (date 30/08/2012)
# LAST REVISION:  date 28/01/215

import os
import sys
import string
###################### (rinomina e numera tutte le cartelle trovate)
def d_namereplace():
	filelist = []
	dirname = os.getcwd()  
	for name in os.listdir(dirname):
		if os.path.isdir(os.path.join(dirname, name)): # filtra il contenuto
			filelist.append(name)
	filelist.sort()
	dest = raw_input("\033[1mRename all folders as: >\033[0m ")
	disp = raw_input("\033[0;1mChoose where to place the numbering > [head/tail] \033[0m ")
	if disp == 'head' or disp == 'HEAD':
		for i, filename in enumerate(filelist):
			name, ext = os.path.splitext(filename)
			try:
				os.rename(filename, str(i+1)+'_'+dest+ext)
			except OSError: #'[Errno 21] Is a directory'
				sys.exit("\033[31;1m[ERROR]: One or more files have the same name\033[0m")
		sys.exit() 
	elif disp == 'tail' or disp == 'TAIL':
		for i, filename in enumerate(filelist):
			name, ext = os.path.splitext(filename)
			try:
				os.rename(filename, dest+'_'+str(i+1)+ext) 
			except OSError: #'[Errno 21] Is a directory'
				sys.exit("\033[31;1m[ERROR]: One or more files have the same name\033[0m")
		sys.exit()
	else:
		sys.exit('\033[31;1m[ERROR]: bad input\033[0m')
		
	sys.exit()

###################### (rinomina qualsiasi stringa di un file in un match)
def d_rename():      
	src = raw_input("\033[1m Enter the string to be replaced >\033[0m ")
	dest = raw_input("\033[1m Insert the replacement string >\033[0m ")
	li = os.listdir(os.getcwd())
	FileList = []
	
	for name in li:		
		if os.path.isdir(os.path.join(name)): # filtra il contenuto
			nuovoNome = name.replace("%s"%(src),"%s"%(dest))
			FileList.append(nuovoNome)
	
	for i in FileList: # itero sull'esistenza dei file
		if FileList.count(i) > 1:
			sys.exit("\033[31;1m[ERROR]: There is a directory with the same name\033[0m")
		
	if src in li and os.path.isfile(src):
		print "\033[31;1m[WARNING]: I can not rename the files, use the -f prefix\033[0m"
		sys.exit()
	else:
		for filename in li:
			if os.path.isdir(filename):
				nuovoNome = filename.replace("%s"%(src),"%s"%(dest))
				try:
					os.rename(filename, nuovoNome)
				except OSError: #'[Errno 21] Is a directory'
					sys.exit("\033[31;1m[ERROR]:  There is a file with the same name\033[0m")
	sys.exit()

###################### (numera le cartelle e conserva il nome ed estensione)
def d_enumerate():
	filelist = []
	dirname = os.getcwd()
	for name in os.listdir(dirname):
		if os.path.isdir(os.path.join(dirname, name)): # filtra il contenuto
			filelist.append(name)	
	filelist.sort()
	disp = raw_input("\033[0;1mChoose where to place the numbering > [head/tail] \033[0m ")
	if disp == 'head' or disp == 'HEAD':
		for i, filename in enumerate(filelist):
			name, ext = os.path.splitext(filename)
			try:
				os.rename(filename, str(i+1)+'_'+name+ext) 
			except OSError: #'[Errno 21] Is a directory'
				sys.exit("\033[31;1m[ERROR]: One or more files have the same name\033[0m")
		sys.exit() 
	elif disp == 'tail' or disp == 'TAIL':
		for i, filename in enumerate(filelist):
			name, ext = os.path.splitext(filename)
			try:
				os.rename(filename, name+'_'+str(i+1)+ext)
			except OSError: #'[Errno 21] Is a directory'
				sys.exit("\033[31;1m[ERROR]: One or more files have the same name\033[0m")
		sys.exit()
	else:
		sys.exit('\033[31;1m[ERROR]: bad input\033[0m')
		
##################### (toglie la numerazione progressiva)		
def d_delnumerate():  
	li = os.listdir(os.getcwd())
	FileList = []
	
	for name in li:
		if os.path.isdir(os.path.join(name)): # filtra il contenuto
			FileList.append(name)
	FileList.sort()
	
	tmp = []			
	for i, name in enumerate(FileList):
		nuovoNome = name.replace(str(i+1),"")
		tmp.append(nuovoNome)

	for i in tmp: # itero sull'esistenza dei file
		if tmp.count(i) > 1:
			sys.exit("\033[31;1m[ERROR]: One or more folders have the same name\033[0m")
	
	for i, filename in enumerate(FileList):
		#if os.path.isdir(os.path.join(filename)):
		nuovoNome = filename.replace(str(i+1),"")
		try:
			os.rename(filename, nuovoNome)
		except OSError: #'[Errno 21] Is a directory'
			sys.exit("\033[31;1m[ERROR]: One or more files have the same name\033[0m")
	sys.exit()


######### (Aggiunge stringhe all'inizio o alla fine dei nomi preservando l'estensione)
	
def f_addname():           
	dest = raw_input("\033[0;1mEnter the string to be added to the file name >\033[0m ")
	FileList = []
	dirname = os.getcwd()  
	for name in os.listdir(dirname):
		if os.path.isdir(os.path.join(dirname, name)): 
			FileList.append(name)
	FileList.sort()

	disp = raw_input("\033[0;1mChoose where to place the new string > [head/tail] \033[0m ")
	if disp == 'head' or disp == 'HEAD':
		for a in FileList:
			if "%s%s" % (dest, a) in FileList:
				sys.exit("\033[31;1m[ERROR]: The object folder already exists with the same name \033[0m") 
		for i, filename in enumerate(FileList):
			try:
				os.rename(filename, dest+filename)
			except OSError: #'[Errno 21] Is a directory'
				sys.exit("\033[31;1m[ERROR]:  There is a file with the same name\033[0m")

	elif disp == 'tail' or disp == 'TAIL':
		for a in FileList:
			if "%s%s" % (a, dest) in FileList:
				sys.exit("\033[31;1m[ERROR]: The object folder already exists with the same name\033[0m")
		for i, filename in enumerate(FileList):
			name, ext = os.path.splitext(filename)			
			try:
				os.rename(filename, name+dest+ext)
			except OSError: #'[Errno 21] Is a directory'
				sys.exit("\033[31;1m[ERROR]:  There is a file with the same name\033[0m")
	else:
		sys.exit('\033[31;1m[ERROR]: bad input\033[0m')
	sys.exit()
		
		
###################### (rinomina l'estensione delle cartelle in un match)
	
def d_extreplace():
	oldext = raw_input("\033[1mEnter the extension to change>\033[0m .")
	newext = raw_input("\033[1mEnter the new extension>\033[0m .")
	FileExtension = []
	FileExist = []
	li = os.listdir(os.getcwd())
			
	if oldext in string.whitespace:
		sys.exit("\033[31;1m[ERROR]: Empty string (old ext) \033[0m")
	if newext in string.whitespace:
		sys.exit("\033[31;1m[ERROR]: Empty string (new ext) \033[0m")
				
	for filename in li: # appendo solo le ext. delle cartelle
		if os.path.isdir(os.path.join(filename)):
			name, ext = os.path.splitext(filename)
			FileExtension.append(ext)
	for filename in li: # appendo tutti i file/dir esistenti con la nuova ext. 
		os.path.join(filename)
		name, ext = os.path.splitext(filename)
		if ext.endswith(oldext):
			FileExist.append("%s.%s" %(name,newext))
			
	for filename in FileExist: # itero sull'esistenza di file con uguale nome.newext
		if os.path.exists(filename):
			print "\033[31;1m[ERROR]: The object already exists with the same name\033[0m"		
			if os.path.isfile(filename):
				sys.exit('        \033[31;1m  and is a file\033[0m')
			elif os.path.isdir(filename):
				sys.exit('        \033[31;1m  and is a directory\033[0m')
		
	if ".%s" % oldext not in FileExtension:
		sys.exit("\033[31;1m[ERROR]: There is no file with the extension '.%s' in the path\033[0m" % oldext)
		
	for filename in li:
		if os.path.isdir(os.path.join(filename)):
			name, ext = os.path.splitext(filename)
			if ext.endswith(oldext):			
				newname = filename.replace(oldext,newext)
				try:
					os.rename(filename, newname)
				except OSError: #'[Errno 21] Is a directory'
					sys.exit("\033[31;1m[ERROR]:  There is a file with the same name\033[0m")
				
	sys.exit()

##################### (aggiunge l'estensione alle cartelle che ne sono prive)
def d_addext():
	newext = raw_input("\033[1m Enter the extension to apply>\033[0m .")
	FileList = []
	FileExist = []
	li = os.listdir(os.getcwd())
	if newext in string.whitespace:
		sys.exit("\033[31;1m[ERROR]: Empty string (new ext) \033[0m")

	for filename in li:
		if os.path.isdir(os.path.join(filename)):
			name, ext = os.path.splitext(filename)
			if ext in string.whitespace:
				FileList.append(filename)	
	if FileList == []:
		sys.exit("\033[31;1m[ERROR]: There is no file with no extension in the path\033[0m")

	for filename in li:
		if os.path.join(filename):
			name, ext = os.path.splitext(filename)
			FileExist.append("%s.%s" %(name,newext))
	print FileExist
	for verify in FileExist:	
		if FileExist in li:
			print "\033[31;1m[ERROR]: The object already exists with the same name\033[0m"		
			if os.path.isfile(verify):
				sys.exit('        \033[31;1m  and is a file\033[0m')
			elif os.path.isdir(verify):
				sys.exit('        \033[31;1m  and is a directory\033[0m')
				
	for filename in FileList:
		try:
			os.rename(filename, "%s.%s" % (filename, newext))
		except OSError: #'[Errno 21] Is a directory'
				sys.exit("\033[31;1m[ERROR]:  There is a file with the same name\033[0m")
	sys.exit()
