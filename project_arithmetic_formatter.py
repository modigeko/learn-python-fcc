def arithmetic_arranger(problems, show_answers=False):
  # vars to build output
  first_line = ""
  second_line =""
  dashes = ""
  answers_line = ""
  first_problem = True
  # max problems is 5
  if len(problems) > 5:
    return 'Error: Too many problems.'
  problems_clean = []
  # sanity checks
  for problem in problems:
    # vars to build output
    operator = ""
    operand_left = ""
    operand_right = ""
    output = []
    # remove all spaces
    problem_temp = problem.replace(" ", "")
    # check if it consists only one operator (+ or -)
    plus_count = problem_temp.count('+')
    min_count = problem_temp.count('-')
    if plus_count + min_count < 1 or plus_count + min_count > 1:
      return "Error: Operator must be '+' or '-'."
    # check if operands only contain digits
    if plus_count == 1:
      operands = problem_temp.split('+')
      operator = "+"
    else:
      operands = problem_temp.split('-')
      operator = "-"
    width = 0
    for index, operand in enumerate(operands):
      if operand.isdigit() is False:
        return 'Error: Numbers must only contain digits.'
      # check if operands only have four or less digits
      if len(operand) < 1 or len(operand) > 4:
        return 'Error: Numbers cannot be more than four digits.'
      if len(operand) > width:
        width = len(operand)
      if index == 0:
        operand_left = operand
      else:
        operand_right = operand
    # get answer line
    if plus_count == 1:
      answer = int(operand_left) + int(operand_right)
    else:
      answer = int(operand_left) - int(operand_right)
    width += 2
    answer_len = len(str(answer))
    if answer_len > width and show_answers:
      width = answer_len + 1
    # format the output
    if first_problem:
      first_line = operand_left.rjust(width)
      second_line = operator + operand_right.rjust(width - 1)
      dashes = ''.rjust(width, '-')
      answers_line = str(answer).rjust(width)
      first_problem = False
    else:
      first_line += '    ' + operand_left.rjust(width)
      second_line += '    ' + operator + operand_right.rjust(width - 1)
      dashes += '    ' + ''.rjust(width, '-')
      answers_line += '    ' + str(answer).rjust(width)

  output = first_line + "\n" + second_line + "\n" + dashes
  # append answers if enabled
  if show_answers:
    output += "\n" + answers_line

  return output

print(f'{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

print(f'{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
print(f'{arithmetic_arranger(["1 + 2", "1 - 9380"])}')
print(f'{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
print(f'{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')
print(f'{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
print(f'{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')





"""

Arithmetic Formatter
Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

  235
+  52
-----
Finish the arithmetic_arranger function that receives a list of strings which are arithmetic problems, and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

Example
Function Call:

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
Output:

   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
Function Call:

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
Output:

  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
If there are too many problems supplied to the function. The limit is five, anything more will return: 'Error: Too many problems.'
The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."
Each number (operand) should only contain digits. Otherwise, the function will return: 'Error: Numbers must only contain digits.'
Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'


If the user supplied the correct format of problems, the conversion you return will follow these rules:
There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
Numbers should be right-aligned.
There should be four spaces between each problem.
There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)


arithmetic_arranger(["3801 - 2", "123 + 49"]) should return   3801      123\n-    2    +  49\n------    -----.
arithmetic_arranger(["1 + 2", "1 - 9380"]) should return   1         1\n+ 2    - 9380\n---    ------.
arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]) should return     3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----.
arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]) should return   11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------.
arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]) should return 'Error: Too many problems.'.
arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]) should return "Error: Operator must be '+' or '-'.".
arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]) should return 'Error: Numbers cannot be more than four digits.'.
arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]) should return 'Error: Numbers must only contain digits.'.
arithmetic_arranger(["3 + 855", "988 + 40"], True) should return     3      988\n+ 855    +  40\n-----    -----\n  858     1028.
arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True) should return    32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028.

"""
