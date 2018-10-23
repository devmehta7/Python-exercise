str = '123a'
str1="123"
#str = '123'
def is_string(str):
    try:
     i = float(str)
    except (ValueError, TypeError):
      print('\nNot numeric')
