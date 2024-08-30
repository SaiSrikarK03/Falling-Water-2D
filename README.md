# Falling-Water-2D
This project features a simple falling water simulation using Pygame. Water particles are added to an 800x800 grid by clicking the mouse, where they flow and interact, simulating realistic fluid dynamics. The simulation uses randomization to create natural movement and leverages Pygame for graphics and NumPy for grid management.

## Features

- **Interactive Simulation**: Users can click on the screen to add water particles.
- **Realistic Water Flow**: The water particles flow downwards and spread out, simulating natural water behavior.
- **Randomized Movement**: Randomization is used to create more fluid and natural water movement.
- **Simple Graphics**: Utilizes Pygame for rendering water particles as blue tiles.

## Requirements

- Python 3.x
- Pygame
- NumPy

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Falling_Water_2D_simulation.git

2.Navigate to the project directory:
   ```bash
   cd Falling_Water_2D_simulation

3.Install the required packages:
   ```bash
   pip install pygame numpy


## Usage

1. Run the simulation:

   ```bash
   python FallingWater2D.py
   ```

2. Click and hold the left mouse button on the window to add water particles at the cursor's location. Release the mouse button to stop adding water.

3. Watch as the water particles flow and interact with the environment.

## How It Works

- The grid is managed using NumPy to efficiently keep track of water particle positions.
- Water particles are represented as blue tiles on a grid.
- Water movement is influenced by gravity, causing particles to flow downwards, with randomized movement to either side to simulate fluidity.
  
## Future Improvements

- Add obstacles to the simulation for water particles to interact with.
- Implement different fluid types with varying flow behaviors.
- Add a GUI for better control over simulation parameters.

## License

This project is open-source and available under the MIT License.
```
