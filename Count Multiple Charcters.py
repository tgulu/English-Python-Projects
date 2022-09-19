# Write a function named count_multi_char_x 
# That takes a string named word and a string named x. 
# This function should do the same thing as the count_char_x 
# Function you just wrote - it should return the number of 
# Times x appears in word. However, this time, make sure 
# Your function works when x is multiple characters long.


def count_multi_char_x(word, x):
  splits = word.split(x)
  print(splits)
  return(len(splits)-1)


print(count_multi_char_x("mississippi", "iss"))
