import sys
import os

from src.python import globalpath
from src.python import tools as t


#@t.timer
def run_plot(input):
    """

    execute Mirazita code for build histogram and computing differences from expected and
    computed Cherenkov angles for single tile of the Aerogel panel

    :param filetoread:  file to read for the analysis
    :return: None

    """
    files = ""
    print(input)
    if os.path.isdir(input):
        for file in os.listdir(input):
            if os.path.isfile(f'{input}/{file}'):
                print(file)
                print(file.split(sep='_')[4])
                print(file.split(sep='_')[5].split('.')[0])
                print(globalpath.ITER)
                print(globalpath.RN)
                if int(file.split(sep='_')[4]) == globalpath.ITER and int(file.split(sep='_')[5].split('.')[0]) == globalpath.RN:
                    files += " "
                    files += f'{input}/{file}'
    else:
       files = " " + input
    #print(files)
    print(files)
    _ = t.runcommand(f"{globalpath.BINDIR}/{globalpath.RICHPLOTBIN} -R{globalpath.RN} {files}", output=globalpath.PRINTplot)
    _ = t.runcommand(f"mv RichPlots_{globalpath.RN}.out {globalpath.PLOTDIR}/result_{globalpath.RN}_{globalpath.ITER}.out")
    _ = t.runcommand(f"mv RichPlots_{globalpath.RN}.root {globalpath.PLOTDIR}/result_{globalpath.RN}_{globalpath.ITER}.root")



if __name__ == "__main__":
    _ = run_plot(sys.argv[1])
