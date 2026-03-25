import numpy as np
import random

from utils.track_utils import compute_curvature, compute_slope
from agents.kart_agent import KartAgent

class Agent7(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.name = "ZHOU_YUNHAO" # replace with your chosen name

        self.cmp = 0 #compteur
    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []
        self.cmp = 0 #compteur
        

    def endOfTrack(self):
        return self.isEnd

    def choose_action(self, obs):
        print("race duration:", self.cmp) #afficher nb de pas
        
        if (self.cmp < 200): # sinb pas inferieur ou egale à 200 
            acceleration = 1 
            steering = 0
            self.cmp = self.cmp + 1 #compteur + 1
        else:                   #sinon
            acceleration = 0    
            steering = 0
        

        action = {
            "acceleration": acceleration,
            "steer": steering,
            "brake": False, # bool(random.getrandbits(1)),
            "drift": bool(random.getrandbits(1)),
            "nitro": bool(random.getrandbits(1)),
            "rescue":bool(random.getrandbits(1)),
            "fire": bool(random.getrandbits(1)),
        }
        return action
