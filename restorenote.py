import sys
def main(argv):
    # the first argument is the input file (note archive)
    # the second argument is the string (old title) to match
    # the third argument is the new title to write
    # the fourth argument is the output file of the matched note
    # the fifth argument is the output file of the revised archive
    inputs = argv[0];
    strtomatch = argv[1];
    #print strtomatch
    strtowrite = argv[2];
    #print strtowrite
    outputs = argv[3];
    outputf = open(outputs,"w");
    oinputs = argv[4];
    oinputf = open(oinputs,"w");
    with open(inputs,"r") as inputf:
        line = inputf.readline();
        while line != "":
            if line.startswith(strtomatch):
                # write the new title in the restored note
                outputf.write(strtowrite+"\n");
                #print nextline
                line = inputf.readline();
                nextline = inputf.readline();
                while not(nextline == "") and not(nextline.startswith("# ")):
                    outputf.write(line)
                    line = nextline
                    nextline = inputf.readline();
                #if nextline == "":
                #    outputf.write(line);
                #else:
                outputf.write(line.rstrip('\n'));
                oinputf.write(nextline);
            else:
                # remove the extra blank line in archive
                oinputf.write(line);
            line = inputf.readline();
    outputf.close();
    oinputf.close();

if __name__ == "__main__":
    main(sys.argv[1:])
