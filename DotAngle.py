import numpy as np

# Define the vectors
u = np.array([1, 8])
v = np.array([-7, -9])

# Compute the dot product
dot_product = np.dot(u, v)

# Compute the magnitudes of the vectors
magnitude_u = np.linalg.norm(u)
magnitude_v = np.linalg.norm(v)

# Compute the cosine of the angle
cos_theta = dot_product / (magnitude_u * magnitude_v)

# Compute the angle in degrees
theta = np.degrees(np.arccos(cos_theta))

# Print the result
print(f"The angle θ between the vectors u and v is approximately {theta:.3f} degrees.")
