import numpy as np
import bezier_curves as b_c


previous_m_state_x, previous_m_state_y = 0,0
zoomFactor = 1.0
scalar_matrix = np.array([[zoomFactor, 0.0, 0.0, 0.0],[0.0, zoomFactor, 0.0, 0.0],[0.0, 0.0, zoomFactor, 0.0,],[0.0, 0.0, 0.0, 1.0]])

rotate_mtr_on_z = lambda alpha : np.array([[np.cos(alpha),0,np.sin(alpha)], [0,1,0],[-np.sin(alpha),0,np.cos(alpha)]])


def make_copy(points) :
    n = int(360/20)
    arr_points = np.empty((n,len(data),3))
    for i in range(0,n):
        alpha = (i+1)*(2*np.pi/n)
        tmp = points.dot(rotate_mtr_on_z(alpha))
        arr_points[i] = tmp
    return arr_points


def paralels(points) :
    return points.transpose((1,0,2))

data = b_c.get_data()
tmp = np.insert(data, 2, 0, axis=1)
max_y = max(tmp[:,1])
max_x = max(tmp[:,0])
for i in range(len(tmp)):
    tmp[i] = [(tmp[i][0] - max_x)/max_x, (tmp[i][1] - max_y/2)/max_y*1.7, 0]

meredians_arr = make_copy(tmp)

# arr = []
# for arr1 in meredians_arr:
#     for arr2 in arr1:
#         arr.append(arr2)

paralels_arr = paralels(meredians_arr)

# arrP = []
# for arr1 in paralels_arr:
#     for arr2 in arr1:
#         arrP.append(arr2)
