import matplotlib.pyplot as plt
from pipe1 import binary_matrix
from pipe1 import trajectory
from pipe1 import *
# Create a figure and axis

matrix=binary_matrix
fig, ax = plt.subplots()

# Loop through the matrix to plot cells
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            # Cells with value 1 are colored red
            ax.add_patch(plt.Rectangle((j, -i - 1), 1, 1, color='red'))
        else:
            # Cells with value 0 are left blank
            ax.add_patch(plt.Rectangle((j, -i - 1), 1, 1, color='white', edgecolor='black'))

# Highlight points in 'highlightline' with black color
highlightline = trajectory
for point in highlightline:
    ax.add_patch(plt.Rectangle((point[1], -point[0] - 1), 1, 1, color='black'))

# Set aspect ratio to be equal, so cells are square
ax.set_aspect('equal')
ax.add_patch(plt.Rectangle((38, -7 - 1), 1, 1, color='pink'))
ax.add_patch(plt.Rectangle((149, -11 - 1), 1, 1, color='black'))
# Set axis limits based on matrix size
plt.xlim(0, len(matrix[0]))
plt.ylim(-len(matrix), 0)

# Remove axis ticks and labels for better visualization
plt.xticks([])
plt.yticks([])

# Show the grid visualization
plt.show()
