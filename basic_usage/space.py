import gym
import numpy as np
from gym.spaces import Box, Discrete, Dict, Tuple, MultiBinary, MultiDiscrete

observation_space = Box(low=-1.0, high=2.0, shape=(3,), dtype=np.float32)
print(observation_space.sample())
#[ 1.6952509 -0.4399011 -0.7981693]

observation_space = Discrete(4)
print(observation_space.sample())
#1

observation_space = Discrete(5, start=-2)
print(observation_space.sample())
#-2

observation_space = Dict({"position": Discrete(2), "velocity": Discrete(3)})
print(observation_space.sample())
#OrderedDict([('position', 0), ('velocity', 1)])

observation_space = Tuple((Discrete(2), Discrete(3)))
print(observation_space.sample())
#(1, 2)

observation_space = MultiBinary(5)
print(observation_space.sample())
#[1 1 1 0 1]

observation_space = MultiDiscrete([ 5, 2, 2 ])
print(observation_space.sample())
#[3 0 0]