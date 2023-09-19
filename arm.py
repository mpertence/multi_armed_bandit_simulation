import random
import numpy as np
    

class Arm:
  def __init__(self, name, click_prob, purchase_prob, click_reward=1, purchase_reward=3):
    self.name = name
    self.click_prob = click_prob
    self.purchase_prob = purchase_prob
    self.click_reward = click_reward
    self.purchase_reward = purchase_reward
    self.count_views = 0
    self.count_clicks = 0
    self.count_purchases = 0
    self.cum_reward = 0

  def __str__(self):
    return f"{self.name}"

  def __gt__(self, other):
    return self.cum_reward > other.cum_reward


  def run(self):

    ramdom_num = np.random.rand()
    view = 1 
    click = 1 if ramdom_num <= self.click_prob else 0
    purchase = 1 if (ramdom_num <= self.purchase_prob) & (click == 1) else 0
    
    self.count_views += 1
    self.count_clicks += click
    self.count_purchases += purchase
    self.cum_reward += (click * self.click_reward) + (purchase * self.purchase_reward)
    

    



