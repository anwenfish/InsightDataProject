import sys, os

def process(line, wordsCount):
    words = line.split()
    for word in words:
        if word not in wordsCount:
            wordsCount[word] = 1
        else:
            wordsCount[word] += 1

if __name__ == "__main__":

    dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    if len(sys.argv) > 1:
        ifilename = os.path.abspath(sys.argv[1])
        tmp = os.path.basename(ifilename).split('.')
	# when run run.sh at cygwin, ifilename has weird non-ascii character at the end
        if (tmp[1] is not 'txt'):
            ifilename = os.path.join(os.path.dirname(ifilename), tmp[0]+'.txt')
    else:
        ifilename = os.path.join(dir, '../tweet_input/tweets.txt')    
    
    if len(sys.argv) > 2:
        ofilename = os.path.abspath(sys.argv[2])
	# when run run.sh at cygwin, ifilename has weird non-ascii character at the end
        tmp = os.path.basename(ofilename).split('.')
        if (tmp[1] is not 'txt'):
            ofilename = os.path.join(os.path.dirname(ofilename), tmp[0]+'.txt')
    else:
        ofilename = os.path.join(dir, '../tweet_output/ft1.txt')

    # read input
    wordsCount = {}
    ifile = open(ifilename, 'r')
    for line in ifile:
        process(line, wordsCount)
    ifile.close()

    # write output
    length = max(len(word) for word in wordsCount)
    ofile = open(ofilename, 'w')
    for word in sorted(wordsCount):
        # I need to use '\r\n' when running the script at cygwin
        ofile.write("{:{}}      {}".format(word, length, wordsCount[word])+'\n')
    ofile.close()
    
