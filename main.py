# Import the super-mario game
import gym_super_mario_bros
# Import the joypad
from nes_py.wrappers import JoypadSpace
# Import the MOVEMENT controller
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
# Import input processors
from gym.wrappers import FrameStack, GrayScaleObservation
from stable_baselines3.common.vec_env import VecFrameStack, DummyVecEnv

# Import matplotlib
from matplotlib import pyplot as plt

# Setup supermario game
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)

# Run game
done = True
for step in range(100000):
    if done:
        env.reset()
    state, reward, done, info = env.step(env.action_space.sample())
    print(reward)
    env.render()
env.close()

# Pre-process env
