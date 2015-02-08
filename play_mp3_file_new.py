"""PyAudio Example: Play a mp3 file."""

import sys
import mp3play
import time
import os.path


def main():
    pass
if len(sys.argv) < 2:
    	sys.exit('Plays a mp3 file \nUsage: %s ' % sys.argv[0])



filename_ext = str(sys.argv[1])
filename = r"E:\Internet Downloads" + '\\' + filename_ext
print (filename)

if os.path.exists(filename):
	clip = mp3play.load(filename)
	
	clip.play()

	print (" The duration of songs is " + str(clip.seconds()))

	time.sleep(min(300, clip.seconds()))
	clip.stop()
else :
	print "No such file exists - " + filename




if __name__ == '__main__':
    main()

