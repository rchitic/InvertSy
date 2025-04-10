import numpy as np
import matplotlib.pyplot as plt
from invertpy.brain.centralcomplex.attractor_static_params import *

short_valid_JE_JI = [(10, -9),
                     (9, -8),
                     (8, -7),
                     (7, -6),
                     (6, -5),
                     (5, -4),
                     (4, -3),
                     (3, -2)
                     ]
N_range = np.arange(6, 12, 2)
weight_norms = [0.01, 0.1, 0.5, 1, 3, 5, 10]
state_norms = [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Reduce number of parameter combinations
short_weight_norms = [0.01, 1, 5, 10, 50]
short_state_norms = [1, 5, 10, 50, 100]

# angles, home_vectors, agent_locations = [], [], []
# for N in N_range:
#     for idx in range(len(short_valid_JE_JI)):
#         J_E, J_I = short_valid_JE_JI[idx]
#         for weight_norm in short_weight_norms:
#             for state_norm in short_state_norms:
#                 values = [N, J_E, J_I, weight_norm, state_norm]
#                 angle = np.load("/home/p318679/Documents/InvertSy/data/attractor/attractor_angles/N{}_JE{}_JI{}_WN{}_SN{}.npy".format(N,J_E,J_I,weight_norm,state_norm))
#                 angles.append(angle)
#                 home_vector = np.load("/home/p318679/Documents/InvertSy/data/attractor/home_vectors/N{}_JE{}_JI{}_WN{}_SN{}.npy".format(N,J_E,J_I,weight_norm,state_norm))
#                 home_vectors.append(home_vector)
#                 trip_end_location = np.load("/home/p318679/Documents/InvertSy/data/attractor/agent_locations/N{}_JE{}_JI{}_WN{}_SN{}.npy".format(N,J_E,J_I,weight_norm,state_norm))
#                 agent_locations.append(trip_end_location)
#
# home_vectors = np.array(home_vectors).reshape(3,len(short_valid_JE_JI),len(short_weight_norms),len(short_state_norms),len(home_vector))
# angles = np.array(angles).reshape(3,len(short_valid_JE_JI),len(short_weight_norms),len(short_state_norms),len(angle))
# agent_locations = np.array(agent_locations).reshape(3,len(short_valid_JE_JI),len(short_weight_norms),len(short_state_norms),len(trip_end_location))
# print(angles.shape, home_vectors.shape, agent_locations.shape)

N,J_E,J_I,WN,SN = 6,4.1,-2.5,1,0

agent_locations=np.load("{}\\InvertSy\\data\\attractor\\agent_locations\\N{}_JE{}_JI{}_WN{}_SN{}.npy".format(home_loc,N,J_E,J_I,WN,SN))
agent_locations = agent_locations[:len(agent_locations)//3*3].reshape(len(agent_locations)//3,3)
print(agent_locations.shape)
plt.scatter(agent_locations[:,1],agent_locations[:,0])
plt.show()

#---------------------------------------------------------------------------------------------------------------------------------
# ATTRACTOR ACTIVITY

t=190
att_activity=np.load("{}\\InvertSy\\data\\attractor\\attractor6_activity_with_drift\\N{}_JE{}_JI{}_WN{}_SN{}.npy".format(home_loc,N,J_E,J_I,WN,SN))
non_att_activity=np.load("{}\\InvertSy\\data\\attractor\\attractor6_activity_without_drift\\N{}_JE{}_JI{}_WN{}_SN{}.npy".format(home_loc,N,J_E,J_I,WN,SN))
att_activity = att_activity[:len(att_activity)//N*N].reshape(len(att_activity)//N,N)
non_att_activity = non_att_activity[:len(non_att_activity)//N*N].reshape(len(non_att_activity)//N,N)
plt.plot(non_att_activity[t])
plt.plot(att_activity[t])
plt.title(f'Attractor 6 activity at timestep {t}')
plt.show()

att_activity=np.load("{}\\InvertSy\\data\\attractor\\attractor3_activity_with_drift\\N{}_JE{}_JI{}_WN{}_SN{}.npy".format(home_loc,N,J_E,J_I,WN,SN))
non_att_activity=np.load("{}\\InvertSy\\data\\attractor\\attractor3_activity_without_drift\\N{}_JE{}_JI{}_WN{}_SN{}.npy".format(home_loc,N,J_E,J_I,WN,SN))
att_activity = att_activity[:len(att_activity)//N*N].reshape(len(att_activity)//N,N)
non_att_activity = non_att_activity[:len(non_att_activity)//N*N].reshape(len(non_att_activity)//N,N)
plt.plot(non_att_activity[t])
plt.plot(att_activity[t])
plt.title(f'Attractor 3 activity at timestep {t}')
plt.show()

att_activity=np.load("{}\\InvertSy\\data\\attractor\\attractor1_activity_with_drift\\N{}_JE{}_JI{}_WN{}_SN{}.npy".format(home_loc,N,J_E,J_I,WN,SN))
non_att_activity=np.load("{}\\InvertSy\\data\\attractor\\attractor1_activity_without_drift\\N{}_JE{}_JI{}_WN{}_SN{}.npy".format(home_loc,N,J_E,J_I,WN,SN))
att_activity = att_activity[:len(att_activity)//N*N].reshape(len(att_activity)//N,N)
non_att_activity = non_att_activity[:len(non_att_activity)//N*N].reshape(len(non_att_activity)//N,N)
plt.plot(non_att_activity[t])
plt.plot(att_activity[t])
plt.title(f'Attractor 1 activity at timestep {t}')
plt.show()

att_mem=np.load("{}\\InvertSy\\data\\attractor\\__mem\\N{}_JE{}_JI{}_WN{}_SN{}.npy".format(home_loc,N,J_E,J_I,WN,SN))
non_att_mem=np.load("{}\\InvertSy\\data\\attractor\\__mem_without_drift\\N{}_JE{}_JI{}_WN{}_SN{}.npy".format(home_loc,N,J_E,J_I,WN,SN))
baseline=np.load("{}\\InvertSy\\data\\non_attractor\\__mem\\N{}_JE{}_JI{}_WN{}_SN{}.npy".format(home_loc,6,4,-2.4,0,0))
att_mem = att_mem[:len(att_mem) // 16 * 16].reshape(len(att_mem) // 16, 16)
non_att_mem = non_att_mem[:len(non_att_mem) // 16 * 16].reshape(len(non_att_mem) // 16, 16)
baseline = baseline[:len(baseline) // 16 * 16].reshape(len(baseline) // 16, 16)

for t in [10,20,30,40,50]:
    plt.plot(baseline[t])
    plt.plot(non_att_mem[t])
plt.show()

t=100
plt.plot(baseline[t])
plt.plot(att_mem[t])

t=200
plt.plot(baseline[t])
plt.plot(att_mem[t])
#
t=299
plt.plot(baseline[t])
plt.plot(att_mem[t])

plt.title(f'CPU4 mem at timestep {t}')
plt.show()

att_angles=np.load("{}\\InvertSy\\data\\attractor\\attractor_angles\\N{}_JE{}_JI{}_WN{}_SN{}.npy".format(home_loc,N,J_E,J_I,WN,SN))
non_att_angles=np.load("{}\\InvertSy\\data\\attractor\\attractor_angles_without_drift\\N{}_JE{}_JI{}_WN{}_SN{}.npy".format(home_loc,N,J_E,J_I,WN,SN))
att_angles = att_angles[:len(att_angles) // 16 * 16].reshape(len(att_angles) // 16, 16)
non_att_angles = non_att_angles[:len(non_att_angles) // 16 * 16].reshape(len(non_att_angles) // 16, 16)

# t=100
# plt.plot(non_att_angles[t])
# plt.plot(att_angles[t])
#
t=100
plt.plot(non_att_angles[t])
plt.plot(att_angles[t])

t=200
plt.plot(non_att_angles[t])
plt.plot(att_angles[t])

t=299
plt.plot(non_att_angles[t])
plt.plot(att_angles[t])

plt.title('Attractor angles at food')
plt.show()

att_angles=np.load("{}\\InvertSy\\data\\attractor\\steering_vectors\\N{}_JE{}_JI{}_WN{}_SN{}.npy".format(home_loc,N,J_E,J_I,WN,SN))
non_att_angles=np.load("{}\\InvertSy\\data\\non_attractor\\steering_vectors\\N{}_JE{}_JI{}_WN{}_SN{}.npy".format(home_loc,6,4,-2.4,0,0))
#non_att_angles=np.load("{}\\InvertSy\\data\\attractor\\attractor_angles_without_drift\\N{}_JE{}_JI{}_WN{}_SN{}.npy".format(home_loc,N,J_E,J_I,WN,SN))
plt.plot(non_att_angles)
plt.plot(att_angles)
plt.title('Steering vector')
plt.show()