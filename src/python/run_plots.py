import sys
import os

from src.python import globalpath
from src.python import tools as t


@t.timer
def prova():
    print(globalpath.PLOTDIR)

def run_plot(input):
    """

    execute Mirazita code for build histogram and computing differences from expected and
    computed Cherenkov angles for single tile of the Aerogel panel

    :param filetoread:  file to read for the analysis
    :return: None

    """
    files = ""

    if os.path.isdir(input):
        for file in os.listdir(input):
            if os.path.isfile(f'{input}/{file}'):
                if int(file.split(sep='_')[4].split(sep='.')[0]) == globalpath.ITER:
                    files += " "
                    files += f'{input}/{file}'
    else:
       files = " " + input
    #print(files)
    _ = t.runcommand(f"{globalpath.BINDIR}/richPlots -R{globalpath.RN} {files}", output=globalpath.PRINTplot)
    _ = t.runcommand(f"mv RichPlots_{globalpath.RN}.out {globalpath.PLOTDIR}/result_{globalpath.RN}_{globalpath.ITER}.out")
    _ = t.runcommand(f"mv RichPlots_{globalpath.RN}.root {globalpath.PLOTDIR}/result_{globalpath.RN}_{globalpath.ITER}.root")



if __name__ == "__main__":
    _ = run_plot(sys.argv[1])
