import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Grid parameters
Nx, Ny = 100, 100    # 2D grid size
dx = 0.1             # spatial resolution
dt = 0.01            # time resolution
Nt = 800             # number of time steps

# Breathing field parameters
lambda_ = 1.0        # potential strength
v = 1.0              # vacuum expectation value
alpha = 0.5          # CRANKED self-awareness strength

# Initialize the 2D breathing field with random noise
phi = np.random.randn(Nx, Ny) * 0.1
phi_old = np.copy(phi)

# Arrays to save frames
phi_frames = []
gravity_frames = []

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
        phi_frames.append(np.copy(phi))
        
        # Calculate breathing energy density (for gravity)
        grad_phi_x = (np.roll(phi, -1, axis=0) - np.roll(phi, 1, axis=0)) / (2*dx)
        grad_phi_y = (np.roll(phi, -1, axis=1) - np.roll(phi, 1, axis=1)) / (2*dx)
        grad_phi_sq = grad_phi_x**2 + grad_phi_y**2
        rho = 0.5 * grad_phi_sq + lambda_ * (phi**2 - v**2)**2
        gravity_frames.append(rho)

# Create the breathing field animation
fig1, ax1 = plt.subplots()
im1 = ax1.imshow(phi_frames[0], animated=True, cmap='plasma', vmin=-1.5, vmax=1.5)
ax1.set_title('2D Breathing Field with Self-Awareness')
ax1.axis('off')

def update_phi(frame):
    im1.set_array(frame)
    return [im1]

ani1 = animation.FuncAnimation(fig1, update_phi, frames=phi_frames, interval=50, blit=True)
ani1.save('breathing_2D_awareness_femur.gif', writer='pillow')
plt.show()

# Create the gravitational curvature animation
fig2, ax2 = plt.subplots()
im2 = ax2.imshow(gravity_frames[0], animated=True, cmap='inferno')
ax2.set_title('2D Gravitational Breathing Curvature')
ax2.axis('off')

def update_gravity(frame):
    im2.set_array(frame)
    return [im2]

ani2 = animation.FuncAnimation(fig2, update_gravity, frames=gravity_frames, interval=50, blit=True)
ani2.save('breathing_2D_gravity_femur.gif', writer='pillow')
plt.show()
