#!/usr/bin/python
import subprocess
import click
@click.command()
@click.option('-o','--osufilesdir', default='./', help='Put the directory which contains your osu files')
@click.option('-b','--beatmapsdir', default='~/.PlayOnLinux/wineprefix/osu_on_linux/drive_c/Program Files/osu!/Songs/', help='Extraction directory for beatmaps')
@click.option('-k','--skinsdir', default='~/.PlayOnLinux/wineprefix/osu_on_linux/drive_c/Program Files/osu!/Skins/', help='Extraction directory for skins')
def do(osufilesdir,beatmapsdir,skinsdir):
	"""Tool to extract and place osu files in their correct directory on linux"""
	osufilesdir = osufilesdir+("" if osufilesdir[len(osufilesdir)-1]=="/" else "/")
	out,err = subprocess.Popen("rename \"s/ /_/g\" "+osufilesdir+"*",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	print out,err
	out,err = subprocess.Popen("rename \"s/'//g\" "+osufilesdir+"*",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	print out,err
	out,err = subprocess.Popen("mkdir beatmaps",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	print out,err
	out,err = subprocess.Popen("mkdir skins",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	print out,err
	files,err = subprocess.Popen("ls "+osufilesdir+"*.osz",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	files = files.split("\n")
	files = files[:len(files)-1]
	files = [f.replace("\'","\\\'") for f in files]
	print files
	for f in files:
		out,err = subprocess.Popen("unzip \'"+osufilesdir+f+"\' -d "+"\'beatmaps/"+f[:len(f)-4]+"\'",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
		print out,err
		out,err = subprocess.Popen("rm \'"+osufilesdir+f+"\'",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
		print out,err
	out,err = subprocess.Popen("mv beatmaps/* \'"+beatmapsdir+"\'",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	print out,err
	files,err = subprocess.Popen("ls "+osufilesdir+"*.osk",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	files = files.split("\n")
	files = files[:len(files)-1]
	files = [f.replace("\'","\\\'") for f in files]
	print files
	for f in files:
		out,err = subprocess.Popen("unzip \'"+osufilesdir+f+"\' -d "+"\'skins/"+f[:len(f)-4]+"\'",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
		print out,err
		out,err = subprocess.Popen("rm \'"+osufilesdir+f+"\'",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
		print out,err
	out,err = subprocess.Popen("mv skins/* \'"+skinsdir+"\'",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	print out,err
if __name__ == '__main__':
	do()