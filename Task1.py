def list_to_int(lst:List[int]):
  numStr = ""
  for num in lst:
    numStr += str(num)

  return int(numStr)
