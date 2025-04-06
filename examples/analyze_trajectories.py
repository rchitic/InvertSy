import numpy as np
import matplotlib.pyplot as plt
from invertpy.brain.centralcomplex.attractor_static_params import *
from invertsy.env.world import Seville2009
import warnings
import argparse

# Get route
with warnings.catch_warnings():
    warnings.simplefilter("ignore")

    parser = argparse.ArgumentParser(
        description="Run a path integration test."
    )

    parser.add_argument("-i", dest='input', type=str, required=False, default=Seville2009.ROUTES_FILENAME,
                        help="File with the recorded routes.")

    p_args = parser.parse_args()
routes = Seville2009.load_routes(p_args.input, degrees=True)
ant_no, rt_no, rt = routes['ant_no'][0], routes['route_no'][0], routes['path'][0]
rt = rt[::-1]
rt[:, 3] = (rt[:, 3] - 0) % 360 - 180
rt = rt[:,:2]
route_length = rt.shape[0]
route_distance = np.linalg.norm(rt[0]-rt[-1])

def get_min(value,min):
    if value < min:
        return value

short_weight_norms = [0, 1, 5, 10]
short_state_norms = [0, 1, 5, 10]
short_JEs = 4 + np.array([-10, -5, -1, 0, 1, 5, 10]) / 100 * 4
short_JIs = -2.4 + np.array([-10, -5, -1, 0, 1, 5, 10]) / 100 * 2.4

N=8
min_dists = []
mem_dists = []
correlations,correlations_normalized = [],[]
amp_diffs = []
for J_E in short_JEs:
    for J_I in short_JIs:
        for weight_norm in short_weight_norms:
            for state_norm in short_state_norms:
                # Closest trajectory point to nest
                agent_locations=np.load("{}\\InvertSy\\data\\attractor\\agent_locations\\N{}_JE{}_JI{}_WN{}_SN{}.npy".format(home_loc,N,round(J_E,2),round(J_I,2),round(weight_norm,2),round(state_norm,2)))
                agent_locations = agent_locations[:len(agent_locations)//3*3].reshape(len(agent_locations)//3,3)
                agent_locations = agent_locations[route_length:,:2]
                dists = np.linalg.norm(agent_locations-rt[0],axis=1)
                min_dist = np.min(dists)
                min_dists.append(min_dist)

                # Distance between real and attractor home vectors
                non_att_mem = np.load(
                    "{}\\InvertSy\\data\\non_attractor\\__mem\\N{}_JE{}_JI{}_WN{}_SN{}.npy"\
                        .format(home_loc,N,3.6,-2.64,1,5)
                )
                non_att_mem = non_att_mem[:len(non_att_mem) // 16 * 16].reshape(len(non_att_mem) // 16, 16)
                att_mem = np.load(
                    "{}\\InvertSy\\data\\attractor\\__mem\\N{}_JE{}_JI{}_WN{}_SN{}.npy"\
                        .format(home_loc, N, round(J_E,2), round(J_I,2), weight_norm, state_norm)
                )
                att_mem = att_mem[:len(att_mem) // 16 * 16].reshape(len(att_mem) // 16, 16)
                mem_dist = np.linalg.norm(att_mem[route_length]-non_att_mem[route_length])
                mem_dists.append(mem_dist)

                # Extract the memory when reaching food
                non_att_mem = non_att_mem[route_length]
                att_mem = att_mem[route_length]

                # Pearson correlation
                corr_normalized = np.corrcoef(non_att_mem,att_mem)[0,1]
                correlations_normalized.append(corr_normalized)

                # Amplitude
                amp_diff = np.abs(np.mean(att_mem / non_att_mem))
                amp_diffs.append(amp_diff)
# plt.plot(min_dists)
# plt.xlabel('Parameter combination id')
# plt.title('Euclidean distance between nest & closest trajectory point')
# plt.ylabel('Euclidean distance (m)')
# plt.savefig("{}\\InvertSy\\data\\attractor\\graphs\\trajectory_Euclidean_min_dist_N{}.png".format(home_loc,N))
# plt.show()

# plt.plot(mem_dists)
# plt.xlabel('Parameter combination id')
# plt.title('Euclidean distance between ground truth & attractor home vectors')
# plt.ylabel('Euclidean distance (m)')
# plt.savefig("{}\\InvertSy\\data\\attractor\\graphs\\home_vector_Euclidean_dist_N{}.png".format(home_loc,N))
# plt.show()

fig, axs = plt.subplots(2,1)  # Main axis
axs[0].plot(correlations_normalized,label='(gt,obs) mem correlation')
axs[0].plot(amp_diffs,label='mean abs obs/gt mem')
axs[1].plot(min_dists,label='closest dist to nest',color='g',alpha=0.5)
fig.suptitle('Relation between ground truth and attractor encoded memory')
plt.xlabel('Parameter combination id')
axs[0].legend()
axs[1].legend()
axs[1].set_ylabel('Distance (m)')
plt.savefig("{}\\InvertSy\\data\\attractor\\graphs\\correlation_N{}.png".format(home_loc,N))
plt.show()