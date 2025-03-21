from invertsy.env.world import Seville2009
from invertsy.agent import PathIntegrationAgent
from invertsy.sim.simulation import PathIntegrationSimulation
from invertsy.sim.animation import PathIntegrationAnimation
import json, os
import numpy as np
import random
random.seed(0)

def main(N,J_E,J_I,weight_norm,state_norm,*args):
    routes = Seville2009.load_routes(args[0], degrees=True)
    ant_no, rt_no, rt = routes['ant_no'][0], routes['route_no'][0], routes['path'][0]
    print("Ant#: %d, Route#: %d, steps#: %d" % (ant_no, rt_no, rt.shape[0]))

    rt = rt[::-1]
    rt[:, 3] = (rt[:, 3] - 0) % 360 - 180
    # rt[:, 3] = (rt[:, 3] - 5) % 360 - 180
    agent = PathIntegrationAgent(N,J_E,J_I,weight_norm,state_norm)
    agent.step_size = .01
    sim = PathIntegrationSimulation(N,J_E,J_I,weight_norm,state_norm, rt, agent=agent, noise=0., name="pi-ant%d-route%d" % (ant_no, rt_no))
    ani = PathIntegrationAnimation(N,J_E,J_I,weight_norm,state_norm, sim, show_history=True)
    ani(save=False, show=True, save_type="mp4", save_stats=False)


if __name__ == '__main__':
    import warnings
    import argparse

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        parser = argparse.ArgumentParser(
            description="Run a path integration test."
        )

        parser.add_argument("-i", dest='input', type=str, required=False, default=Seville2009.ROUTES_FILENAME,
                            help="File with the recorded routes.")

        p_args = parser.parse_args()

        valid_JE_JI = [(10, -6), (10, -7), (10, -8), (10, -9), (10, -10), (10, -11), (10, -12), (10, -13), (10, -14),
                       (9, -5), (9, -6), (9, -7), (9, -8), (9, -9), (9, -10), (9, -11), (9, -12), (9, -13), (9, -14),
                       (8, -5), (8, -6), (8, -7), (8, -8), (8, -9), (8, -10), (8, -11), (8, -12), (8, -13), (8, -14),
                       (7, -4), (7, -5), (7, -6), (7, -7), (7, -8), (7, -9), (7, -10), (7, -11), (7, -12), (7, -13),
                       (7, -14),
                       (6, -3), (6, -4), (6, -5), (6, -6), (6, -7), (6, -8), (6, -9), (6, -10), (6, -11), (6, -12),
                       (6, -13),
                       (6, -14),
                       (5, -2), (5, -3), (5, -4), (5, -5), (5, -6), (5, -7), (5, -8), (5, -9), (5, -10), (5, -11),
                       (5, -12),
                       (5, -13), (5, -14),
                       (4, -1), (4, -2), (4, -3), (4, -4), (4, -5), (4, -6), (4, -7), (4, -8), (4, -9), (4, -10),
                       (4, -11),
                       (4, -12), (4, -13), (4, -14),
                       (3, -1), (3, -2), (3, -3), (3, -4), (3, -5), (3, -6), (3, -7), (3, -8), (3, -9), (3, -10),
                       (3, -11),
                       (3, -12), (3, -13), (3, -14),
                       ]
        short_valid_JE_JI = [(10, -9),
                             (9, -8),
                             (8, -7),
                             (7, -6),
                             (6, -5),
                             (5, -4),
                             (4, -3),
                             (3, -2)
                       ]
        N_range = np.arange(6, 40, 2)

        short_weight_norms = [0,0.05,0.1,0.15,0.2]
        short_state_norms = [0,0.05,0.1,0.15,0.2]
        short_JEs = 4 + np.array([-0.2,-0.15,-0.1,-0.05,0,0.05,0.1,0.15,0.2])
        J_I = -2.4

        for N in N_range:
            for J_E in short_JEs:
                for weight_norm in short_weight_norms:
                    for state_norm in short_state_norms:
                        values = [N,J_E,J_I,weight_norm,state_norm]
                        print('Values',values)
                        np.random.seed(0)
                        main(N,J_E,J_I,weight_norm,state_norm,p_args.input)
