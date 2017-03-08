def fizz_buzz(num):
  """ a function called fiizz_buzz that returns argument depending on the arguement it takes"""
  
  
  if num %3 == 0 and num % 5 ==0:
     return 'FizzBuzz'
  
  elif  num %3 ==0:
    return 'Fizz'

  elif num % 5 ==0:
    return 'Buzz'
        
  
  else:
    return num
    