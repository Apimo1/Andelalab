def data_type(z):
    """ a function called data_type that takes one argument and returns result based on the argument """
    if type(z) == None :
        return'no value'
        
    elif type(z)==list:
        i=2
        while i> len(z):
            i=i+1
            return andela[i]
            
        else:
            return 'none'
            
    elif type(z)== bool:
        return 'andela'
    elif type(z)== int:
        if type(z)<100:
            return 'less than 100'
            
        elif type(z)==100:
            return'equal to 100'
            
        elif type(z)>100:
            return 'more than 100'
      
    elif type(z)== str:
        return len(z)