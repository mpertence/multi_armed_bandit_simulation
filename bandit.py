import numpy as np

class Bandit:
  def __init__(self, arms, strategy, steps):
    self.arms = arms
    self.strategy = strategy
    self.steps = steps
    self.explorations = []

  def play(self):
    print(f"Playing {self.steps} times using {self.strategy} Strategy")    
    for step in range(self.steps):
        arm, is_exploration = self.strategy.choose(self.arms)
        self.explorations.append(is_exploration)
        arm.run()

