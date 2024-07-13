import copy
import random

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    self.num_colors = 0
    self.num_balls = 0
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)
      self.num_colors += 1
      self.num_balls += value

  def __repr__(self):
    return f"{self.__class__.__name__}()"

  def draw(self, num_balls_drawn):
    drawn_balls = []
    if num_balls_drawn > self.num_balls:
      self.num_balls = 0
      drawn_balls = self.contents.copy()
      self.contents.clear()
      return drawn_balls
    for i in range(num_balls_drawn):
      ball = random.choice(self.contents)
      drawn_balls.append(ball)
      self.contents.remove(ball)
      self.num_balls -= 1
    return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  # sanity check
  if num_experiments < 1:
    return 0

  # print(hat.contents, hat.num_colors, hat.num_balls)
  # print("expected_balls = ", expected_balls)
  num_success = 0
  for _ in range(num_experiments):
    # backup hat instance
    hat_copy = copy.deepcopy(hat)
    # draw balls and save to a string list
    drawn_balls = hat_copy.draw(num_balls_drawn)
    # print("drawn_balls = ", drawn_balls)
    # convert list to dictionary
    drawn_balls_dict = {}
    for ball in drawn_balls:
      if ball in drawn_balls_dict:
        drawn_balls_dict[ball] += 1
      else:
        drawn_balls_dict[ball] = 1
    # print("drawn_balls_dict = ", drawn_balls_dict)
    # check if all expected balls exist in drawn balls
    all_balls_found = True
    for ball, count in expected_balls.items():
      if drawn_balls_dict.get(ball, 0) < count:
        all_balls_found = False
        break
    if all_balls_found:
      num_success += 1

  return num_success / num_experiments

def main():
  hat = Hat(black=6, red=4, green=3)
  # print(hat.draw(14))
  # print(hat.contents, hat.num_colors, hat.num_balls)
  probability = experiment(hat=hat,
                    expected_balls={'red':2,'green':1},
                    num_balls_drawn=5,
                    num_experiments=20)
  print (probability)

if __name__ == '__main__':
  main()

"""
Build a Probability Calculator Project
Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.

For this project, you will write a program to determine the approximate probability of drawing certain balls randomly from a hat.

First, create a Hat class in main.py. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. For example, a class object could be created in any of these ways:

hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
A hat will always be created with at least one ball. The arguments passed into the hat object upon creation should be converted to a contents instance variable. contents should be a list of strings containing one item for each ball in the hat. Each item in the list should be a color name representing a single ball of that color. For example, if your hat is {'red': 2, 'blue': 1}, contents should be ['red', 'red', 'blue'].

The Hat class should have a draw method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from contents and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.

Next, create an experiment function in main.py (not inside the Hat class). This function should accept the following arguments:

hat: A hat object containing balls that should be copied inside the function.
expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {'blue':2, 'red':1}.
num_balls_drawn: The number of balls to draw out of the hat in each experiment.
num_experiments: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)
The experiment function should return a probability.

For example, if you want to determine the probability of getting at least two red balls and one green ball when you draw five balls from a hat containing six black, four red, and three green. To do this, you will perform N experiments, count how many times M you get at least two red balls and one green ball, and estimate the probability as M/N. Each experiment consists of starting with a hat containing the specified balls, drawing several balls, and checking if you got the balls you were attempting to draw.

Here is how you would call the experiment function based on the example above with 2000 experiments:

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
The output would be something like this:

0.356
Since this is based on random draws, the probability will be slightly different each time the code is run.

Hint: Consider using the modules that are already imported at the top. Do not initialize random seed within the file.

Note: open the browser console with F12 to see a more verbose output of the tests.

Run the Tests (Ctrl + Enter)
Save your Code
Reset this lesson
Get Help
Tests
Waiting:Creation of hat object should add correct contents.
Waiting:The draw method in hat class should reduce number of items in contents.
Waiting:The draw method should behave correctly when the number of balls to extract is bigger than the number of balls in the hat.
Waiting:The experiment method should return a different probability.
"""