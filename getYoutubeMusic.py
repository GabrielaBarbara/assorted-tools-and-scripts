#!/usr/bin/python

import errno
import os.path
import string
import subprocess
import sys
from subprocess import call

def main():

    try:
        output = subprocess.check_output(["which", "youtube-dl"])
    except subprocess.CalledProcessError as e:
        print "youtube-dl was not found, please install it."
        sys.exit()

    try:
        f = open("linksToGet.txt","r")
    except IOError as e:
        print "=-"*30+"=\n"
        print "The file linksToGet.txt does not exist.\n\n"\
            "Please create it and populate it like so:\n\n"\
            "#nameOfArtistOrDirectory\n"\
            "https://youtu.be/7RujKG9hmCY\n\n"\
            "Where the link is obtained from the youtube 'share' button.\n"\
            "You can have as multiple artists/directories and links.\n"\
            "If a directory does not exist it will be created.\n"\
            "This program writes to the Music directory in your home.\n"
        print "=-"*30+"=\n"
        sys.exit()

    want_link = {}
    cur_artist = ""
    for line in f.readlines():
        line = string.replace(line,"\n","")
        if line == '':
            continue
        if line.startswith("#"):
            cur_artist = line.replace("#","")
        else:
            want_link[string.replace(line,"https://youtu.be/","")] = cur_artist
    f.close()

    if len(want_link) == 0:
        print "=-"*30+"=\n"
        print "The file linksToGet.txt is empty.\n\n"\
            "Please populate it like so:\n\n"\
            "#nameOfArtistOrDirectory\n"\
            "https://youtu.be/7RujKG9hmCY\n\n"\
            "Where the link is obtained from the youtube 'share' button.\n"\
            "You can have as multiple artists/directories and links.\n"\
            "If a directory does not exist it will be created.\n"\
            "This program writes to the Music directory in your home.\n"
        print "Or, see exampleLinks.txt for my hacking music collection!\n"
        print "=-"*30+"=\n"
        sys.exit()

    musicpath = os.path.expanduser('~')+"/Music"

    try:
        os.stat(musicpath)
    except OSError:
        os.mkdir(musicpath)
    os.chdir(musicpath)
    for k,v in want_link.iteritems():
        songpath = musicpath+"/"+v.strip()
        downloaditem = "http://youtu.be/"+k
        libarypath = "/var/music/"
        existing_music = []

        for f in os.walk(libarypath):
            for s in f[2]:
                existing_music.append(s[-15:])

        try:
            os.stat(songpath)
        except OSError:
            os.mkdir(songpath)

        os.chdir(songpath)

        # youtube-dl --extract-audio --audio-format mp3 <url>
        if not k in existing_music and not os.path.exists(downloaditem):
            call(["youtube-dl", "--extract-audio",
                  "--audio-format", "mp3", downloaditem])

    print "Download complete.\n"\
          "Please copy the contents of ~/Music to "\
          "/var/music and empty the linksToGet.txt file."

if __name__ == '__main__':
    main()
