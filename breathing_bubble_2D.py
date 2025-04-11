import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Grid parameters
Nx, Ny = 100, 100    # 2D grid size
dx = 0.1             # spatial resolution
dt = 0.01            # time resolution
Nt = 300             # number of time steps

# Breathing field parameters
lambda_ = 1.0        # potential strength
v = 1.0              # vacuum expectation value
alpha = 0.05         # consciousness strength

# Initialize the 2D breathing field with random noise
phi = np.random.randn(Nx, Ny) * 0.1
phi_old = np.copy(phi)

# Arrays to save frames
frames = []

# Potential derivative
def potential_derivative(phi):
    return 4 * lambda_ * phi * (phi**2 - v**2)

# Evolution loop
for t in range(Nt):
    # Compute global breathing average
    phi_mean = np.mean(phi)
    
    # 2D Laplacian (finite difference)
    laplacian_phi = (
        np.roll(phi, 1, axis=0) + np.roll(phi, -1, axis=0) +
        np.roll(phi, 1, axis=1) + np.roll(phi, -1, axis=1) -
        4 * phi
    ) / dx**2
    
    # Consciousness breathing force
    consciousness_force = alpha * (phi - phi_mean)
    
    # Full breathing evolution
    phi_new = (2 * phi - phi_old +
               dt**2 * (laplacian_phi - potential_derivative(phi) - consciousness_force))
    
    # Update fields
    phi_old = np.copy(phi)
    phi = np.copy(phi_new)
    
    # Save frames
    if t % 5 == 0:
        frames.append(np.copy(phi))

# Create the animation
fig, ax = plt.subplots()
im = ax.imshow(frames[0], animated=True, cmap='plasma', vmin=-1.5, vmax=1.5)
ax.set_title('2D Breathing Field with Self-Awareness')
ax.axis('off')

def update(frame):
    im.set_array(frame)
    return [im]

ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)
ani.save('breathing_2D_awareness.gif', writer='pillow')
plt.show()
