from collections import deque
from PIL import Image, ImageDraw

from heapq import heappop, heappush
from PIL import Image, ImageDraw

def draw_trajectory_on_image(trajectory, image_path, output_path, square_size):
    # Open the original image
    img = Image.open(image_path)
    
    # Create a drawing context
    draw = ImageDraw.Draw(img)
    
    # Draw the trajectory on the image
    for point in trajectory:
        y, x = point
        # Convert square coordinates back to pixel coordinates
        x_pixel = x * square_size
        y_pixel = y * square_size
        # Draw a solid black rectangle at the current position with a width of 10 pixels
        draw.rectangle([x_pixel, y_pixel, x_pixel + square_size, y_pixel + square_size], fill="black")
    
    # Save the modified image to the output path
    img.save(output_path)


def find_adjacent_pink_pixels(image_path):
    target_color = (255, 0, 255)  # RGB color for pink
    image = Image.open(image_path)
    width, height = image.size

    for x in range(width - 1):
        for y in range(height - 1):
            pixel_color = image.getpixel((x, y))
            if pixel_color == target_color:
                # Check adjacent pixels (right and bottom)
                right_pixel_color = image.getpixel((x + 1, y))
                bottom_pixel_color = image.getpixel((x, y + 1))
                if right_pixel_color == target_color or bottom_pixel_color == target_color:
                    return  (x, y)
    return  None
from PIL import Image

def find_adjacent_orange_pixels(image_path):
    target_color = (255, 165, 0)  # RGB color for orange
    image = Image.open(image_path)
    width, height = image.size

    for x in range(width - 1):
        for y in range(height - 1):
            pixel_color = image.getpixel((x, y))
            if pixel_color == target_color:
                # Check adjacent pixels (right and bottom)
                right_pixel_color = image.getpixel((x + 1, y))
                bottom_pixel_color = image.getpixel((x, y + 1))
                if right_pixel_color == target_color or bottom_pixel_color == target_color:
                    return (x, y)
    return None

def is_red(pixel, tolerance=20):
    # Check if the pixel is within the tolerance range of pure red (#FF0000)
    return pixel[0] >= 255 - tolerance and pixel[1] <= tolerance and pixel[2] <= tolerance

def process_image(image_path, square_size):
    img = Image.open(image_path)
    width, height = img.size

    # Calculate the number of squares in rows and columns
    num_squares_x = width // square_size
    num_squares_y = height // square_size

    binary_matrix = []

    for y in range(num_squares_y):
        row = []
        for x in range(num_squares_x):
            # Crop the image to the current square
            left = x * square_size
            upper = y * square_size
            right = left + square_size
            lower = upper + square_size
            square_img = img.crop((left, upper, right, lower))

            # Check if the square contains a pixel close to pure red
            is_red_square = any(is_red(pixel) for pixel in square_img.getdata())

            # Append 1 if red or 0 if not
            row.append(1 if is_red_square else 0)
        binary_matrix.append(row)

    return binary_matrix, num_squares_x, num_squares_y


from collections import deque


import math

def find_closest_distance(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    queue = deque([(start, 0, [start])])
    visited = set()
    visited.add(start)
    
    while queue:
        current, distance, path = queue.popleft()
        if current == end:
            return distance, path
        
        for dx, dy in directions:
            new_x, new_y = current[0] + dx, current[1] + dy
            
            # Calculate the step distance using Euclidean method
            step_distance = math.sqrt((new_y - current[1])**2 + (new_x - current[0])**2)
            
            if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 0 and (new_x, new_y) not in visited:
                queue.append(((new_x, new_y), distance + step_distance, path + [(new_x, new_y)]))
                visited.add((new_x, new_y))
    
    return -1, []



image_path = "input.jpg"
square_size = 5  # Size of each square in pixels

binary_matrix, num_squares_x, num_squares_y = process_image(image_path, square_size)
print(binary_matrix)
print(num_squares_x)
print(num_squares_y)

tuplestart= find_adjacent_pink_pixels("input.jpg")
tupleend = find_adjacent_orange_pixels("input.jpg")
start=(round(tuplestart[1]/square_size), round(tuplestart[0]/square_size))
end=(round(tupleend[1]/square_size), round(tupleend[0]/square_size))
print(start, end)
distance, trajectory = find_closest_distance(binary_matrix, start, end)
print("Closest distance between start and end points:", distance)
print("Trajectory:", trajectory)
draw_trajectory_on_image(trajectory, "input.jpg", "output.jpg", square_size)
