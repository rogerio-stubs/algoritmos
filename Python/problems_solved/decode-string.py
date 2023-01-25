"""
Dada uma string codificada, retorne a string decodificada.

A regra de codificação é: k[string_codificada], onde a string_codificada dentro dos 
colchetes serão repetidas o número de k vezes. O valor de k será sempre um número 
positivo.

Você deve assumir que as strings de entrada são sempre válidas, 
sem espaço e os colchetes estão bem formatados.

s = "2[a]3[bc]", retornará "aabcbcbc".
s = "3[a2[c]]", retornará "accaccacc".
s = "2[abc]3[cd]ef", retornará "abcabccdcdcdef".
"""

def decode_string(str_to_decode):
  stack = []

  mapping = {
    ')': '(',
    ']': '[',
    '}': '{'
  }

  # O(n)
  for input in str_to_decode:
    if input in mapping:
        if len(stack) and mapping[input] == stack.pop():
          continue
    stack.append(input)

  return len(stack) == 0 

if __name__ == '__main__':
  decode_string("2[a]3[cd]")  
  decode_string("3[a2[c]]")
  decode_string("2[abc]3[cd]ef")