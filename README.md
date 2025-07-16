# Approximation of 1D Quantum Particle Energy Levels with Neural Networks


This project uses a neural network built with TensorFlow to predict the energy levels of a quantum particle confined in a one dimensional box (infinite potential well). It applies regression techniques to learn the relationship between the quantum number **`n`**, the mass **`m`** of the particle, and the length **`L`** of the box to estimate the corresponding energy **`E`**.

## Overview


The model learns to approximate the relationship given by the quantum mechanical equation:

  

$$

E_n = \frac{n^2 h^2}{8mL^2}

$$

  

Rather than calculating energy using the above formula explicitly, this project demonstrates a data driven machine learning approach where the neural network generalizes the mapping from inputs (**`n`, `m`, `L`**) to output (**`E`**).

## Dataset

The dataset is generated synthetically using:

- Quantum number **`n`** (positive integers)

- Particle mass **`m`** (range: 1e-30 to 1e-27 kg)

- Box length **`L`** (range: nanometers to micrometers)

- Planck's constant $h = 6.62607015 \times 10^{-34}\ \text{J}\cdot\text{s}$

The energy `E` is computed and stored in `data/Energy-Level-data.csv`.

### Features Used

To improve model performance and capture the nonlinear patterns:

- `n_squared = n^2`

- `inv_mass = 1 / m`

- `inv_length_squared = 1 / L^2`

These engineered features are used as the model input.

## Model Architecture

The model was built using TensorFlow's Sequential API with the following structure:

- Input Layer: 4 engineered features

- Dense Layer: **128 units**, **ReLU**

- **Batch Normalization**

- Dense Layer: **256 units, ReL**U

- Dropout Layer: rate = **0.2**

- Dense Layer: **128 units,** **ReLU**

- Dense Layer: **64 units,** **ReLU**

- Output Layer: 1 unit (predicted energy)

### Compilation Details

- Loss: Mean Squared Error (MSE)

- Optimizer: Adam

- Metrics: Mean Absolute Error (MAE)

### Final Performance

- R-squared Score: **0.9531** on the test set

- Indicates high correlation and accurate prediction capability
### Installation

```bash

pip install -r requirements.txt

```
  

1. Run the dataset generator script to create `Energy-Level-data.csv`

2. Load the dataset and apply preprocessing

3. Train the model using the provided training pipeline

4. Evaluate and export model metrics and predictions
