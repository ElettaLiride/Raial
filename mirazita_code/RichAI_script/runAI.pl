#!/apps/bin/perl

# Run a chain of programs for AI alignment studies

$rootDir = "../";

#For the reconstruction of the rich
$dir_reco = $rootDir . "/RichAI_script";
$exe_reco = "/work/clas12/users/devita/clas12validation/clara-iss643-rich/plugins/clas12/bin/recon-util";
$yamlF = $dir_reco . "/rich.yaml";
$dirOUT_reco = $rootDir . "/out";
if (! -d dirOUT_reco) {
    $cmd = "mkdir " . $dirOUT_reco;
    system($cmd);
}


# For the plots 
$dir_plots = $rootDir . "/RichAI_Plots";
$exe_plots = $dir_plots . "/richPlots";
$ccdbAerogel = $dir_plots . "/Aerogel_ccdb.dat";
$root_plots = $dir_plots . "/DrawRichPlots.C";



# list of files
$list = $ARGV[0];



############################################
# Reprocessing the RICH


# CHECK THE VALUE OF $CCDB_CONNECTION
$cmd = "echo \$CCDB_CONNECTION";
system($cmd);


open (LISTFILE, "<$list");
while (<LISTFILE>) {
    chomp;

    printf("\n=====================================\n\n");
    
    $fileIn = $_;
    printf("file  %s\n", $fileIn);

    if (-e $fileIn) { 

	$nData1 = split /_/, $_;
	@str1 = split(/_/, $_);

#	printf("nData1=%d\n", $nData1);
#	for ($i=0; $i<$nData1; $i++) {
#	    printf("i=%d    data=%s\n", $i, $str1[$i]);
#	}
	
	$RunNumber = $str1[$nData1-2];
	printf("  RUN  %d  \n", $RunNumber);



	$nData = split /\//, $fileIn;
	@str = split /\//, $fileIn;
	$fileOut = $dirOUT_reco . "/" . $str[$nData-1];
	printf("reco file: %s\n", $fileOut);


	$cmd = $exe_reco . " -i " . $fileIn . " -o " . $fileOut . " -y " . $yamlF;
	printf("cmd:  %s\n", $cmd);
	system($cmd);

    }
    else {
	printf("ERROR - missing file: %s\n", $fileIn); 
    }
}
close INFILE;


############################################
# Making the plots 

$cmd = "cp -p " . $ccdbAerogel . " .";
printf("cmd:  %s\n", $cmd);
#system($cmd); 

$RunNumber = 10;

$cmd = $exe_plots . " -R" . $RunNumber . " " . $dirOUT_reco . "/*";
printf("cmd:  %s\n", $cmd);
system($cmd);

$fileRoot = "RichPlots_" . $RunNumber . ".root";
$cmd = "root -l -b -q '" . $root_plots . "(\"" . $fileRoot . "\")'";
printf("cmd:  %s\n", $cmd);
system($cmd);
 
$cmd = "mv RichPlots_* " . $dirOUT_reco;
printf("cmd:  %s\n", $cmd);
system($cmd);


    
