import numpy as np
from arm import Arm
from bandit import Bandit
from strategy import EpsilonGreedyStrategy, GreedyStrategy, RandomStrategy, UCB


tela_1 = Arm(name="tela_1", click_prob=0.1, purchase_prob=0.15)
tela_2 = Arm(name="tela_2", click_prob=0.35, purchase_prob=0.08)
tela_3 = Arm(name="tela_3", click_prob=0.35, purchase_prob=0.02)

arms = [tela_1,tela_2,tela_3]
egreedy = EpsilonGreedyStrategy(epsilon=0.1)
greedy = GreedyStrategy()
random = RandomStrategy()
upper_bound = UCB()

bandit = Bandit(arms=arms, strategy=upper_bound, steps=1000)

bandit.play()

for arm in bandit.arms:
    print(arm)
