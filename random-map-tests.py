import pysc2
from pysc2.agents import random_agent
from pysc2.env import sc2_env, run_loop

from absl import flags
import sys
FLAGS = flags.FLAGS
FLAGS(sys.argv)


step_mul = 1
steps = 10000
with sc2_env.SC2Env(map_name="DefeatZerglingsAndBanelings",
                    players= [sc2_env.Agent(sc2_env.Race.protoss)],
agent_interface_format = sc2_env.AgentInterfaceFormat(
                                                    feature_dimensions=sc2_env.Dimensions(
                                                    screen=84,
                                                    minimap=64),
                                                    use_feature_units=True),
step_mul=step_mul,
visualize=True,
game_steps_per_episode=steps * step_mul) as env:
    agent = random_agent.RandomAgent()
    run_loop.run_loop([agent], env, steps)