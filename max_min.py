def find_max_min(value):
  
  max_num = max(value)
  min_num = min(value)
  array = []
  
  if min_num == max_num:
    num_of_elements = len(value)
    array.append(num_of_elements)
    return array
    
  else:
    array.append(min_num)
    array.append(max_num)
    return array
      
    