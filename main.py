import sys
import os
import subprocess

import ccdb_connection as cc
import parameters_setting as pm

def getrunnumber(file):
    return file.split("_")[2]


if __name__ == "__main__":
    exereco = "/work/clas12/users/devita/clas12validation/clara-iss643-rich/plugins/clas12/bin/recon-util"
    exeplot = "mirazita_code/RichAI_Plots/richPlots"
    fileIN = "../RICH_alignement/Mirazita_script/RichAI_FilterC/rec_clas_5208_AIskim1.hipo"
    fileOUT = "5208_AIskim1.hipo"
    runnumber = getrunnumber(fileIN)
    DrawingFile = "mirazita_code/RichAI_plots/DrawRichPlots.C"
    yalm = "mirazita_code/RichAI_script/rich.yaml"
    dirOUT = "out/"

    calibration_connection = "sqlite:////$PWD/ccdb_4.3.2.sqlite "
    calibration_table = '/calibration/rich/misalignments'
    variation = 'misalignements'
    user = "Costantini"

    module = [4, 201, 1]
    pars = [0, 0, 1, 1, 1, 0]

    RunNumber = "0"
    Layer = "-1"
    filetofilter = "file"

    # executing Mirazita code for filtering
    # if sys.argv[0] == '-f':
    #     subprocess.run(["./mirazita_code/RichAI_FilterC/filterHipo", "-R" + RunNumber, "-L" + Layer, filetofilter])

    # executing reconstruction
    # subprocess.run(["./", exereco, "-i", fileIN, "-o", fileOUT, "-y", yalm])
    bashCommand = "echo ==============INIZIO-LA-RECO============== "
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    bashCommand = "/work/clas12/users/devita/clas12validation/clara-iss643-rich/plugins/clas12/bin/recon-util -i " + fileIN + " -o " + fileOUT + " -y " + yalm
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    #execute evaluation

    bashCommand = "echo ==============INIZIO-I-PLOT============== "
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    # subprocess.run([exeplot, "-R"+runnumber, dirOUT + "/*"])
    bashCommand = "./"+exeplot+" -R"+runnumber+" "+dirOUT+"/*"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    #execute drawing

    # subprocess.run(["root", "-l", "-p", "-q", DrawingFile + "(\"RichPlots_" + runnumber + "\")"])
    # subprocess.run(["mv", "RichPlots_*", dirOUT])
    # # execute Costantini code for update ccdb

    # update ccdb
    #
    # provider = cc.connecting_ccdb(calibration_connection, variation)
    # old_pars_table = cc.reading_ccdb(provider, calibration_table, variation)
    # new_pars_table = pm.changing_parameters(pars, old_pars_table, module)
    #
    # toadd = new_pars_table.values.tolist()
    # cc.adding_to_ccdb(toadd, provider, calibration_table, variation)
