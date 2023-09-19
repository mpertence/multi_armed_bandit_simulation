import numpy as np
from arm import Arm
from bandit import Bandit
from strategy import EpsilonGreedyStrategy, GreedyStrategy, RandomStrategy


tela_1 = Arm(name="tela_1", click_prob=0.1, purchase_prob=0.05)
tela_2 = Arm(name="tela_2", click_prob=0.35, purchase_prob=0.08)
tela_3 = Arm(name="tela_3", click_prob=0.35, purchase_prob=0.02)

arms = [tela_1,tela_2,tela_3]
strategy = EpsilonGreedyStrategy(epsilon=0.1)
strategy_2 = GreedyStrategy()
strategy_3 = RandomStrategy()

bandit = Bandit(arms=arms, strategy=strategy, steps=1000000)

bandit.play()

for arm in bandit.arms:
    print(arm, arm.cum_reward, arm.count_purchases)