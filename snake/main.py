import subprocess
import sys

from snake import pygamescreen



if __name__ == '__main__':
    pygamescreen.pygamescreen()

    sys.exit(subprocess.call([sys.executable, __file__]))
