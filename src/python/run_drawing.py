import sys

from src.python import tools as t


# executing Mirazita code for drawing
def runcommand(file):
    command = f"root -l -p -q src/cpp/DrawRichPlots.C(\"{file}\")"
    stdout = t.runcommand(command)
    print(stdout[0])


if __name__ == "__main__":
    runcommand(sys.argv[1])
