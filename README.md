# assorted-tools-and-scripts
Some tools and scripts that may be useful

## CompileGolang.bash
Compile your golang programs in peace, and have the script comment out any unused variables instead of trying to use the _ = foo trick that ends up hard to clean up.

## powersOf2Drill
A simple trick to knowing what 2^n is approximately plus a little drill program to practice.  

## getYoutubeMusic.py
Little script to grab mp3 files from youtube.  You need youtube-dl and a file in the same directory as the program called 'linksToGet.txt' that looks like so:
```
#nameOfDirectoryThisFileGoesTo
https://youtu.be/7RujKG9hmCY

#OsamuKitajima
https://youtu.be/SuOBOGA_CTo
https://youtu.be/qQgHW4y8_Go

#theMoreTheMerrier
https://youtu.be/MoreLinksHere
```
Where the link is taken from the 'share' button on the youtube page.q

The program creates the directory if it does not already exist in your ~/Music directory, and it checks /var/music if the mp3 you want already exists.  So, if your set up is different, change that please.
