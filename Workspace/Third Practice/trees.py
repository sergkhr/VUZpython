import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# settings
x_field_size = 100
y_field_size = 100
attraction_count = 100
attraction_radius = 50
attraction_death_radius = 2
growth_distance = 2

# (x, y), (dx, dy) - starting point and direction of growth
growth_starting_point = np.array([np.array([50, 5]), np.array([0, 0])])
# Create a random set of attractors
attractors = np.random.rand(attraction_count, 2) * [x_field_size, y_field_size]
#print(attractors)
# # draw the attractors as a scatter plot
#plt.scatter(attractors[:, 0], attractors[:, 1], s=1, c='k')
# plt.show()

tree = np.array([growth_starting_point])


def attract_closest(attractor_point, tree, attractors):
    # get the closest point on the tree to the attractor
    closest_point_index = 0
    for i in range(len(tree)):
        if np.linalg.norm(np.array(tree[i][0]) - np.array(attractor_point)) < \
                    np.linalg.norm(np.array(tree[closest_point_index][0]) - np.array(attractor_point)):
            closest_point_index = i
    closest_point = tree[closest_point_index]
    # get the distance between the attractor and the closest point
    distance = np.linalg.norm(np.array(closest_point[0]) - np.array(attractor_point))
    # print(attractor_point, closest_point[0], distance)
    
    if distance < attraction_death_radius:
        # find attractor_point index in attractors
        ind = np.where(attractors == attractor_point)[0][0]
        # remove the attractor from the list
        attractors = np.delete(attractors, ind, 0)

    #print(distance, attraction_radius)
    if distance < attraction_radius:
        #print('Attracting...')
        temp_dx = attractor_point[0] - closest_point[0][0]
        temp_dy = attractor_point[1] - closest_point[0][1]
        dx = temp_dx / distance
        dy = temp_dy / distance
        # set the direction of growth of the closest point to the direction of the attractor
        new_dx = closest_point[1][0] + dx
        new_dy = closest_point[1][1] + dy
        tmp_distance = np.linalg.norm(np.array([new_dx, new_dy]))
        tmp_cls_point = np.array([closest_point[0], np.array([new_dx / tmp_distance, new_dy / tmp_distance])])
        tree[closest_point_index] = tmp_cls_point.copy()
        print (tmp_cls_point)
        print(tree[closest_point_index])



def grow_tree(tree):
    for point in tree:
        #print(point)
        if point[1][0] != 0 or point[1][1] != 0:
            print('Growing tree...')
            # add the direction of growth to the point, work with numpy ndarray
            new_point = (np.array(point[0]) + np.array(point[1]) * growth_distance, np.array([0, 0]))
            # add the new point to the tree
            tree.append((new_point, point[1]))
    return tree


def grow_iteration(tree, attractors):
    # attract the point of the tree to the attractors
    for point in attractors:
        #print(tree)
        attract_closest(point, tree, attractors)
        #print(tree)

    # grow the tree
    tree = grow_tree(tree)
    return tree


# while there are still attractors or 100 iterations have not been reached
iter_count = 0
while len(attractors) > 0 and iter_count < 10:
    tree = grow_iteration(tree, attractors)
    iter_count += 1

print(len(tree))
print(iter_count)

# drawing the tree
lines = []
for i in range(len(tree) - 1):
    lines.append([tree[i][0], tree[i + 1][0]])
lc = LineCollection(lines, linewidths=1)
fig, ax = plt.subplots()
ax.add_collection(lc)
ax.autoscale()
ax.margins(0.1)
plt.show()
