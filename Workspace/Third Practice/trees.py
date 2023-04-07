import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# settings
x_field_size = 100
y_field_size = 200
attraction_count = 150
attraction_radius = 1000  # heeeh big number
attraction_death_radius = 5
growth_distance = 3

# for drawing
lines = []
leaves = []

# [x, y], [list of active_attractors] - starting point and direction of growth
growth_starting_point = [np.array([x_field_size / 2, 0]), []]
# Create a random set of attractors (from 0 to x_field_size, from 50 to y_field_size)
attractors = np.random.rand(attraction_count, 2) * [x_field_size, y_field_size / 2] + [0, y_field_size / 2]
# print(attractors)
# # draw the attractors as a scatter plot
fig, ax = plt.subplots()
plt.scatter(attractors[:, 0], attractors[:, 1], s=1, c='k')
# plt.show()

tree = [growth_starting_point]


def attract_closest(attractor_point):
    global tree
    global attractors
    # get the index of the closest point to the attractor, search only by x and y
    closest_point_index = 0
    for i in range(len(tree)):
        # print(i, tree)
        # print(tree[i][0], attractor_point)
        if np.linalg.norm(np.array(tree[i][0]) - np.array(attractor_point)) < np.linalg.norm(np.array(tree[closest_point_index][0]) - np.array(attractor_point)):
            closest_point_index = i
    closest_point_cords = tree[closest_point_index][0]
    # get the distance between the attractor and the closest point
    distance = np.linalg.norm(np.array(closest_point_cords) - np.array(attractor_point))
    # print(attractor_point, closest_point[0], distance)
    if distance < attraction_death_radius:
        # find attractor_point index in attractors
        ind = np.where(attractors == attractor_point)[0][0]
        # remove the attractor from the list
        attractors = np.delete(attractors, ind, 0)
        # make closest point a leaf
        leaves.append(closest_point_cords)
    elif distance < attraction_radius:
        # add the attractor to the list of active attractors
        tree[closest_point_index][1].append(attractor_point)


def grow_tree(point):
    global tree
    global lines
    normalized_direction = [0, 0]
    # iterate through all attractors and find those that are within the attraction radius
    for attractor in point[1]:
        normalized_direction += (attractor - point[0]) / (np.linalg.norm(attractor - point[0])**2)  # squared distance
        # to make the closer attractors more important

    if len(point[1]) > 0:
        # normalize the direction
        normalized_direction = normalized_direction / np.linalg.norm(normalized_direction)
        # add the new point to the tree
        new_point = [point[0] + normalized_direction * growth_distance, []]
        tree.append(new_point)
        # add the line to the lines list
        lines.append([point[0], new_point[0]])
        # remove the attractors from the list of active attractors
        point[1] = []


def grow_iteration():
    global tree
    global attractors
    # attract the point of the tree to the attractors
    for point in attractors:
        attract_closest(point)
    # grow the tree
    for point in tree:
        grow_tree(point)


# while there are still attractors or 100 iterations have not been reached
iter_count = 0
while len(attractors) > 0 and iter_count < 200:
    print(iter_count, len(attractors), len(tree))
    grow_iteration()
    iter_count += 1

print(len(tree))
print(iter_count)

# drawing the tree
lc = LineCollection(lines, linewidths=1)
# draw leaves as a scatter plot with circles
leaf_radius = attraction_death_radius
for leaf in leaves:
    circle = plt.Circle(leaf, leaf_radius, alpha=0.5, color='g')
    ax.add_patch(circle)

ax.add_collection(lc)
ax.set_aspect('equal')
ax.set_xlim(-10, x_field_size + 10)
ax.set_ylim(-10, y_field_size + 10)
plt.show()
