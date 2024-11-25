import numpy as np
import matplotlib.pyplot as plt

def read_coordinates(file_path):
    """
    Reads a text file containing cylindrical coordinates (r, θ, z).
    Each line should have r, θ, z separated by spaces.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    coordinates = []
    for line in lines:
        r, theta, z = map(float, line.split())
        coordinates.append((r, theta, z))
    return coordinates

def cylindrical_to_cartesian(r, theta, z):
    """
    Converts cylindrical coordinates to Cartesian coordinates.
    θ is expected to be in degrees.
    """
    theta_rad = np.radians(theta)
    x = r * np.cos(theta_rad)
    y = r * np.sin(theta_rad)
    return x, y, z

def plot_3d_coordinates(cartesian_coords):
    """
    Plots 3D coordinates.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    xs, ys, zs = zip(*cartesian_coords)
    ax.scatter(xs, ys, zs, c='b', marker='o')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Plot of Coordinates')
    
    plt.show()

def main():
    file_path = input("Enter the path to the txt file with coordinates: ")
    cylindrical_coords = read_coordinates(file_path)
    cartesian_coords = [cylindrical_to_cartesian(r, theta, z) for r, theta, z in cylindrical_coords]
    plot_3d_coordinates(cartesian_coords)

if __name__ == "__main__":
    main()
