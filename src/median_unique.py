import os, sys
from heapq import heappush as push, heappop as pop

# a class can insert numbers one by one, and get corresponding median
class RunningMedians:
    def __init__(self):
        self.left, self.right = [], []
        
    def insert(self, num):
        if len(self.right) == len(self.left):
            push(self.left, -num)
            push(self.right, -pop(self.left))
        else:
            push(self.right, num)
            push(self.left, -pop(self.right))

    def getMed(self):
        if len(self.right) == 0:
            return 0

        if len(self.right) == len(self.left):
            return (self.right[0] - self.left[0])/2.0
        else:
            return self.right[0]

# a list of numbers as input argument; it is a redundant function. I do not used in __main__
def medians(numbers):
    numbers = iter(numbers)
    left, right = [], []
    while True:
        #odd items
        push(left, -next(numbers))
        push(right, -pop(left))
        yield right[0]

        #even items
        push(right, next(numbers))
        push(left, -pop(right))
        yield (right[0] - left[0])/2.0

if __name__ == '__main__':
    
    dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    if len(sys.argv) > 1:
        ifilename = os.path.abspath(sys.argv[1])
	# when run run.sh at cygwin, ifilename has weird non-ascii character at the end
	tmp = os.path.basename(ifilename).split('.')
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
        ofilename = os.path.join(dir, '../tweet_output/ft2.txt')

    #read input
    meds = []
    medians = RunningMedians()
    ifile = open(ifilename, 'r')
    for line in ifile:
        num = len(set(line.split()))
        medians.insert(num)
        meds.append(medians.getMed())
    ifile.close()
            

    #write output
    ofile = open(ofilename, 'w')
    for med in meds:
        # I need to change '\n' to '\r\n' when running the script at cygwin
        ofile.write(str(med)+'\n')
    ofile.close()
