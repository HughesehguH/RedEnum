from optparse import OptionParser


def main():
  options = handleCommandArgs()


############################
#
# This function is responsible for handling the command line options of the program
# Returns a list of the options passed by the user
#
############################
def handleCommandArgs():
    parser = OptionParser()
    parser.add_option("-u", "--user", dest="user", help="The reddit account name to be enumerated")
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False, help="Turn on verbose mode to give more output")
    (options, args) = parser.parse_args()
    return options


if __name__ == '__main__':
    main()