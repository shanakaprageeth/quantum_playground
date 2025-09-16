"""
Hello World with Qiskit
A simple introduction to quantum programming with Qiskit
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

def hello_world_quantum():
    """Create a simple quantum circuit with a Hadamard gate"""
    print("Hello Quantum World with Qiskit!")
    
    # Create a quantum circuit with 1 qubit and 1 classical bit
    qc = QuantumCircuit(1, 1)
    
    # Apply Hadamard gate to create superposition
    qc.h(0)
    
    # Measure the qubit
    qc.measure(0, 0)
    
    # Display the circuit
    print("\nQuantum Circuit:")
    print(qc.draw())
    
    # Simulate the circuit
    simulator = AerSimulator()
    job = simulator.run(qc, shots=1000)
    result = job.result()
    counts = result.get_counts(qc)
    
    print(f"\nMeasurement results (1000 shots): {counts}")
    print("Expected: roughly 50% |0⟩ and 50% |1⟩ due to superposition")
    
    # Plot the results
    try:
        plot_histogram(counts, title="Hello World Quantum Circuit Results")
        plt.savefig("hello_world_results.png")
        plt.show()
        print("Results saved as 'hello_world_results.png'")
    except Exception as e:
        print(f"Could not display plot: {e}")

if __name__ == "__main__":
    hello_world_quantum()