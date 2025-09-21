# Qiskit Quantum Programming Examples

This directory contains Qiskit examples and setup for quantum programming with IBM's Qiskit framework.

## Setup

### Quick Setup
Run the setup script to install Qiskit and dependencies:
```bash
./setup.sh
```

### Manual Setup
If you prefer to set up manually:
```bash
pip3 install -r requirements.txt
```

## Examples

### 1. Hello World (`hello_world.py`)
A simple introduction to quantum programming with a single qubit in superposition.

**Features:**
- Basic quantum circuit creation
- Hadamard gate for superposition
- Measurement and visualization
- Histogram of results

**Run:**
```bash
python3 hello_world.py
```

### 2. Quantum Circuits (`quantum_circuits.py`)
Comprehensive examples of various quantum circuits and algorithms.

**Features:**
- Bell state (quantum entanglement)
- Quantum teleportation
- Grover's algorithm (2-qubit version)
- Circuit visualization and measurement results

**Run:**
```bash
python3 quantum_circuits.py
```

### 3. Interactive Jupyter Notebook (`quantum_circuits_demo.ipynb`)
An interactive notebook with step-by-step quantum circuit examples.

**Features:**
- Single qubit operations
- Multi-qubit entanglement
- Complex gate combinations
- Quantum random number generator
- Visual circuit diagrams

**Run:**
```bash
jupyter notebook quantum_circuits_demo.ipynb
```

## What You'll Learn

1. **Basic Quantum Concepts:**
   - Superposition with Hadamard gates
   - Quantum measurement
   - Qubit states |0⟩ and |1⟩

2. **Quantum Entanglement:**
   - Bell states
   - Correlated measurements
   - Non-local quantum effects

3. **Quantum Algorithms:**
   - Quantum teleportation protocol
   - Grover's search algorithm
   - Quantum random number generation

4. **Qiskit Framework:**
   - Circuit creation and manipulation
   - Quantum simulators
   - Result visualization
   - Circuit drawing and plotting

## Dependencies

- **qiskit**: Main quantum computing framework
- **qiskit-aer**: High-performance quantum circuit simulators
- **matplotlib**: For plotting and visualization
- **numpy**: Numerical operations
- **jupyter**: Interactive notebook environment

## Output Files

The examples will generate PNG files showing:
- Measurement result histograms
- Circuit execution statistics
- Visual representations of quantum states

## Tips

1. **Start with `hello_world.py`** to understand basic concepts
2. **Use Jupyter notebook** for interactive exploration
3. **Check generated PNG files** for visual results
4. **Experiment with different gate combinations** in the examples

## Next Steps

After running these examples, you can:
- Modify circuits to see different behaviors
- Add more qubits to existing circuits
- Implement other quantum algorithms
- Explore quantum error correction
- Try quantum machine learning examples

## Resources

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [Qiskit Textbook](https://qiskit.org/textbook/)
- [IBM Quantum Experience](https://quantum-computing.ibm.com/)
- [Quantum Computing Fundamentals](https://quantum-computing.ibm.com/learn)