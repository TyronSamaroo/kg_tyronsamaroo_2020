import sys


def one_to_one_char_map(s1,s2):
    """This function determine whether a one-to-one character mapping exist from one string, s1, to another s2. 
    
    Arguments:
        s1 {String} -- string of english alphabet letters first command line argument 
        s2 {String} -- string of english alphabet letters second command line argument
    
    Returns:
        Boolean -- True if mapping exist otherwise False 
    """
    if not (s1.isalpha() and s2.isalpha()):
        raise TypeError("Inputs are not from english alphabet")   
    
    #First s1 and s1 has to be same length 
    if len(s1) != len(s2):
        return False

    #This step the len should be the same so now
    #Second string s1 cannot has duplicate characters
    if len(s1) != len(set(s1)):
        return False
    
    #At this point s1 and s1 should be from english alphabet, same length and s1 is unique so it can map to s2 which has enough letters to map each. 
    return True
    
    
if __name__ == "__main__":
    if sys.argv[1] == '-h':
        print(help(one_to_one_char_map))
    try:
        print(one_to_one_char_map(sys.argv[1],sys.argv[2]))
    except IndexError:
        print("You did not list two valid inputs")
        
   