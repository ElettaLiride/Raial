#!/apps/bin/perl

# Making the rich trees for a list of runs


# list of files
$list = $ARGV[0];

$LayerID = 0;


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


	$cmd = "./filterHipo -R" . $RunNumber ." -L" . $LayerID . " " . $fileIn;
	system($cmd);

    }
    else {
	printf("ERROR - missing file: %s\n", $fileIn); 
    }
}
close INFILE;
    
