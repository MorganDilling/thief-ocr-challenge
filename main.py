def validate(code:str, n: int) -> bool:
  if len(code) != n:
    return False
  if not code.isnumeric():
    return False

  return True

def splitCode(code:str) -> list[int]:
  return [int(i) for i in code]

def joinCodes(codes:list[int]) -> str:
  return "".join([str(i) for i in codes])

def findLowest(code:str) -> int:
  codes = splitCode(code)
  codes.sort()
  return int(joinCodes(codes))

def findHighest(code:str) -> int:
  codes = splitCode(code)
  codes.sort(reverse=True)
  return int(joinCodes(codes))

def containsCode(code:list[int], digits:list[int]) -> bool:
  truthy = 0
  for digit in digits:
    if digit in code:
      truthy += 1
  return truthy == len(digits)

def findPossibilities(code:str) -> list[str]:
  possibilities = []

  codes = splitCode(code)

  lowest = findLowest(code)
  highest = findHighest(code)

  for i in range(lowest, highest + 1):
    if containsCode(codes, splitCode(str(i))) and not str(i) in possibilities:
      possibilities.append(formatNumberWithZeros(i, 4))

  return possibilities

def formatNumberWithZeros(number:int, n:int) -> str:
  return f"{number:0{n}d}"

if __name__ == "__main__":
  code = ""

  while not validate(code, 4):
    code = input("Enter a 4-digit code: ")

  print(f"Your code is {code}")

  possibilities = findPossibilities(code)

  print(f"There are {len(possibilities)} possibilities")
  
  for possibility in possibilities:
    print(possibility)