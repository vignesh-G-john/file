import subprocess
import time
import os
import io
import sys
import itertools
def convertMergeImages():
    filename = 'file.jpg'
    IMG = ['corner.jpg','top.jpg','side.jpg','take.jpg']
    subprocess.call(["montage",
                     IMG[0],IMG[1],IMG[0],IMG[1],IMG[0],IMG[1],IMG[0],IMG[1],IMG[0],
                     IMG[2],IMG[3],IMG[2],IMG[3],IMG[2],IMG[3],IMG[2],IMG[3],IMG[2],
                     IMG[0],IMG[1],IMG[0],IMG[1],IMG[0],IMG[1],IMG[0],IMG[1],IMG[0],
                     IMG[2],IMG[3],IMG[2],IMG[3],IMG[2],IMG[3],IMG[2],IMG[3],IMG[2],
                     IMG[0],IMG[1],IMG[0],IMG[1],IMG[0],IMG[1],IMG[0],IMG[1],IMG[0],
                     "-geometry","+0+0",
                     "-tile","9x6",
                     filename,
                     ],shell=True)
convertMergeImages()

                    
