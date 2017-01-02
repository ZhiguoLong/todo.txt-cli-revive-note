import sys
def main(argv):
    # the first argument is the input file
    # the second argument is the string (title) to match
    # the third argument is the output file of the matched note
    inputs = argv[0];
    strtomatch = argv[1];
    outputs = argv[2];
    outputf = open(outputs,"w");
    oinputs = argv[3];
    oinputf = open(oinputs,"w");
    with open(inputs,"r") as inputf:
        line = inputf.readline();
        nextline = inputf.readline();
        while line != "":
            if line.startswith(strtomatch):
                outputf.write(line);
                line = nextline
                nextline = inputf.readline();
                while line != "" and not(line.startswith("# ")):
                    # remove the last blank line in note
                    if nextline != "" and not(nextline.startswith("# ")):
                        outputf.write(line);
                    line = nextline
                    nextline = inputf.readline();
                if line != "":
                    oinputf.write(line);
            else:
                oinputf.write(line);
            line = nextline;
            nextline = inputf.readline();
    outputf.close();
    oinputf.close();

if __name__ == "__main__":
    main(sys.argv[1:])
