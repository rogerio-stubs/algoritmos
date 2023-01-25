""" 
Dada uma string com apenas os seguintes caracteres '(', ')', '{', '}', '[', ']' 
determine se uma determinada string é válida.
"""
def valid_parentheses(str_to_validate):
  stack = []

  mapping = {
    ')': '(',
    ']': '[',
    '}': '{'
  }

  # O(n)
  for input in str_to_validate:
    if input in mapping:
        if len(stack) and mapping[input] == stack.pop():
          continue
    stack.append(input)

  return len(stack) == 0 



if __name__ == '__main__':
    result = valid_parentheses("(()")
    print(result)
