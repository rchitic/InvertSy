import numpy as np
import matplotlib.pyplot as plt

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

# angles, home_vectors, trip_end_locations = [], [], []
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
#                 trip_end_location = np.load("/home/p318679/Documents/InvertSy/data/attractor/trip_end_locations/N{}_JE{}_JI{}_WN{}_SN{}.npy".format(N,J_E,J_I,weight_norm,state_norm))
#                 trip_end_locations.append(trip_end_location)
#
# home_vectors = np.array(home_vectors).reshape(3,len(short_valid_JE_JI),len(short_weight_norms),len(short_state_norms),len(home_vector))
# angles = np.array(angles).reshape(3,len(short_valid_JE_JI),len(short_weight_norms),len(short_state_norms),len(angle))
# trip_end_locations = np.array(trip_end_locations).reshape(3,len(short_valid_JE_JI),len(short_weight_norms),len(short_state_norms),len(trip_end_location))
# print(angles.shape, home_vectors.shape, trip_end_locations.shape)
#
# means = np.mean(home_vectors,axis=(1,2,3))
# print(means.shape,means)
#
# print('h',np.sum(home_vectors[2,0,0,0][:8]),np.sum(home_vectors[2,0,0,0][8:]))
# print('h',np.sum(home_vectors[2,0,2,0][:8]),np.sum(home_vectors[2,0,2,0][8:]))
#
# plt.plot(home_vectors[2,0,0,0])
# plt.plot(home_vectors[2,0,2,0])
# #plt.plot(angles[0,0,2,0])
# plt.show()

# baseline=np.load("/home/p318679/Documents/InvertSy/data/non_attractor/steering_vectors/N20_JE4_JI-2_WN0_SN0.npy")
# #b=np.load("/home/p318679/Documents/InvertSy/data/attractor/steering_vectors/N6_JE10_JI-9_WN0.01_SN1.npy")
# #c=np.load("/home/p318679/Documents/InvertSy/data/attractor/steering_vectors/N6_JE10_JI-9_WN0.01_SN5.npy")
#
# b=np.load("/home/p318679/Documents/InvertSy/data/attractor/steering_vectors/N20_JE4_JI-2_WN0_SN0.npy")
#
# plt.plot(baseline)
# plt.plot(b,alpha=0.5)
# #plt.plot(b,alpha=0.5)
# #plt.plot(c,alpha=0.5)
# plt.show()



baseline=np.load("/home/p318679/Documents/InvertSy/data/attractor/home_vectors/N16_JE4_JI-2_WN0_SN0.npy")
#b=np.load("/home/p318679/Documents/InvertSy/data/attractor/steering_vectors/N6_JE10_JI-9_WN0.01_SN1.npy")
#c=np.load("/home/p318679/Documents/InvertSy/data/attractor/steering_vectors/N6_JE10_JI-9_WN0.01_SN5.npy")

b=np.load("/home/p318679/Documents/InvertSy/data/attractor/__mem/N16_JE4_JI-2_WN0_SN0.npy")
print(b.shape)
b=b.reshape(5684,16)
#plt.plot(baseline)
plt.plot(b[0],alpha=0.5)
plt.plot(b[10],alpha=0.5)
plt.plot(b[200],alpha=0.5)

#plt.plot(c,alpha=0.5)
#plt.show()

# b=np.load("/home/p318679/Documents/InvertSy/data/non_attractor/__mem/N16_JE4_JI-2_WN0_SN0.npy")
# print(b.shape)
# b=b.reshape(1805,16)
# #plt.plot(baseline)
# plt.plot(b[0],alpha=0.5)
# plt.plot(b[10],alpha=0.5)
# plt.plot(b[200],alpha=0.5)

#plt.plot(c,alpha=0.5)
plt.show()