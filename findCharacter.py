def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) != 0 and len(aStr) !=1:
        midPoint = int(len(aStr)/2)
        test = aStr[midPoint]
        if test == char:
            return True
        elif test > char:
            return isIn(char, aStr[:midPoint])
        elif test < char:
            return isIn(char, aStr[midPoint:])
    else:  
        return False
        

isIn('q', 'cpx')