from omniisaacgymenvs.tasks.base.rl_task import RLTask
from omniisaacgymenvs.robots.articulations.anymal import Anymal                     #Change later to CitoLibra
from omniisaacgymenvs.robots.articulations.views.anymal_view import AnymalView      #Change later to citolibra_view
from omniisaacgymenvs.tasks.utils.usd_utils import set_drive

from omni.isaac.core.utils.prims import get_prim_at_path

from omni.isaac.core.utils.torch.rotations import *

import numpy as np
import torch
import math

class CitolibraInvPendelTask(RLTask):
    def __init__(self, name, env, offset=None) -> None:
        super().__init__(name, env, offset)



    def set_up_scene(self, scene, replicate_physics=True) -> None:
        # To do
        return super().set_up_scene(scene, replicate_physics)
    

    def get_citolibra(self):
        # To do
        return 
    
    def get_target(self):
        # Maybe use the same idea as the quadcopter 
        # To do
        return
    
    def get_observations(self) -> dict: 
        # To do
        return 
    
    def pre_physics_step(self, actions):
        # To do
        return super().pre_physics_step(actions)
    
    def reset_idx(self, env_ids):
        # To do
        return 
    
    def post_reset(self):
        # To do
        return 
    
    def calculate_metrics(self) -> None:
        # To do
        return 
    
    def is_done(self) -> None: 
        # To do 
        return 