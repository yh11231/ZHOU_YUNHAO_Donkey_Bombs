import numpy as np
import random

from utils.track_utils import compute_curvature, compute_slope
from agents.kart_agent import KartAgent

#from .Mid import Mid 



class Agent6(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.name = "ZHOU_YUNHAO" # replace with your chosen name


        self.dernier_distance_centre = 0.0 #initialiser le dernier distance du centre a 0
    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []

    def endOfTrack(self):
        return self.isEnd

    def choose_action(self, obs):
        distance_centre = obs['center_path_distance'][0]  # distance au centre 

        # si la distance est plus loin du centre, on tourne plus fort, avec un valeur de controle pour tourner doux
        erreur = 0.35 * distance_centre
        # la différence avec la dernière distance centre pour éviter les virages brusques
        diff = 0.77 * (distance_centre - self.dernier_distance_centre)
        # angle de tournage, lopposé avec la distance au centre, si la distance est positive (droite), on tourne à gauche etc.
        steer = -(erreur + diff)
        # min et max pour limiter les tourne trop forts
        steer = max(-0.6, min(0.6, steer))
        
        # 3. mettre en jour le dernier distance centre pour le prochaine calcule
        self.dernier_distance_centre = distance_centre
        brake = 0.0
        action = {
            "acceleration": 1,
            "steer": steer,
            "brake": brake,
            "drift": False,  
            "nitro": False,
            "rescue": bool(random.getrandbits(1)),
            "fire": bool(random.getrandbits(1)),
        }
        return action