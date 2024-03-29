import numpy as np

class Arm:
  def __init__(self, name, click_prob, purchase_prob, click_reward=1, purchase_reward=3):
    self.name = name
    self.click_prob = click_prob
    self.purchase_prob = purchase_prob
    self.click_reward = click_reward
    self.purchase_reward = purchase_reward

    self.views = []
    self.clicks = []
    self.purchases = []
    self.rewards = []

    self.total_reward = 0
    self.avg_reward = 0
    self.total_views = 0
    self.total_purchases = 0

  def __str__(self):
    return f"{self.name}"

  def __gt__(self, other):
    return self.avg_reward > other.avg_reward
  
  def summary(self):
    return f"{self.name} - total rewards: {self.total_reward} - Mean Rewards: {self.avg_reward}"

  def reset(self):
    self.views = []
    self.clicks = []
    self.purchases = []
    self.rewards = []

    self.total_reward = 0
    self.avg_reward = 0
    self.total_views = 0
    self.total_purchases = 0

  def run(self):

    ramdom_num = np.random.rand()
    view = 1 
    click = 1 if ramdom_num <= self.click_prob else 0
    purchase = 0
    if click == 1:
        ramdom_num = np.random.rand()
        purchase = 1 if (ramdom_num <= self.purchase_prob) else 0
    reward = (click * self.click_reward) + (purchase * self.purchase_reward)
    
    self.views.append(view)
    self.clicks.append(click)
    self.purchases.append(purchase)
    self.rewards.append(reward)

    self.total_reward += reward
    self.total_views += view
    self.total_purchases += purchase

    self.avg_reward = self.total_reward/self.total_views


    



