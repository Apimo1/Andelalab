def find_missing(list1, list2):
  if len(list1)== len(list2):
    return int(0)

  elif list != list2:
    x= set(list1)
    y=set(list2)
    z=x^y
    return list(z)[0]