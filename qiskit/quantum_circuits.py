"""
Quantum Circuits Examples with Qiskit
Demonstrates various quantum gates and circuit visualization
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import plot_histogram, circuit_drawer
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

def bell_state_circuit():
    """Create and visualize a Bell state (quantum entanglement) circuit"""
    print("Creating Bell State Circuit (Quantum Entanglement)")
    
    # Create a quantum circuit with 2 qubits and 2 classical bits
    qc = QuantumCircuit(2, 2)
    
    # Apply Hadamard gate to qubit 0
    qc.h(0)
    
    # Apply CNOT gate with qubit 0 as control and qubit 1 as target
    qc.cx(0, 1)
    
    # Measure both qubits
    qc.measure([0, 1], [0, 1])
    
    # Display the circuit
    print("\nBell State Circuit:")
    print(qc.draw())
    
    return qc

def quantum_teleportation_circuit():
    """Create a quantum teleportation circuit"""
    print("\nCreating Quantum Teleportation Circuit")
    
    # Create a quantum circuit with 3 qubits and 3 classical bits
    qc = QuantumCircuit(3, 3)
    
    # Prepare the state to be teleported (|+⟩ state)
    qc.h(0)
    qc.barrier()
    
    # Create Bell pair between qubits 1 and 2
    qc.h(1)
    qc.cx(1, 2)
    qc.barrier()
    
    # Bell measurement on qubits 0 and 1
    qc.cx(0, 1)
    qc.h(0)
    qc.barrier()
    
    # Measure qubits 0 and 1
    qc.measure([0, 1], [0, 1])
    
    # Apply corrections based on measurement results
    qc.cx(1, 2)
    qc.cz(0, 2)
    
    # Measure the final qubit
    qc.measure(2, 2)
    
    # Display the circuit
    print("\nQuantum Teleportation Circuit:")
    print(qc.draw())
    
    return qc

def grover_circuit():
    """Create a simple 2-qubit Grover's algorithm circuit"""
    print("\nCreating Grover's Algorithm Circuit (2 qubits)")
    
    # Create a quantum circuit with 2 qubits and 2 classical bits
    qc = QuantumCircuit(2, 2)
    
    # Initialize superposition
    qc.h([0, 1])
    qc.barrier()
    
    # Oracle: mark the |11⟩ state
    qc.cz(0, 1)
    qc.barrier()
    
    # Diffusion operator
    qc.h([0, 1])
    qc.x([0, 1])
    qc.cz(0, 1)
    qc.x([0, 1])
    qc.h([0, 1])
    qc.barrier()
    
    # Measure
    qc.measure([0, 1], [0, 1])
    
    # Display the circuit
    print("\nGrover's Algorithm Circuit:")
    print(qc.draw())
    
    return qc

def run_and_visualize_circuit(circuit, title, shots=1000):
    """Run a quantum circuit and visualize the results"""
    # Simulate the circuit
    simulator = AerSimulator()
    job = simulator.run(circuit, shots=shots)
    result = job.result()
    counts = result.get_counts(circuit)
    
    print(f"\nMeasurement results for {title} ({shots} shots): {counts}")
    
    # Plot the results
    try:
        plot_histogram(counts, title=f"{title} Results")
        filename = f"{title.lower().replace(' ', '_')}_results.png"
        plt.savefig(filename)
        plt.show()
        print(f"Results saved as '{filename}'")
    except Exception as e:
        print(f"Could not display plot: {e}")

def main():
    """Main function to run all quantum circuit examples"""
    print("Quantum Circuits Examples with Qiskit")
    print("=" * 40)
    
    # Bell State Circuit
    bell_circuit = bell_state_circuit()
    run_and_visualize_circuit(bell_circuit, "Bell State")
    
    # Quantum Teleportation Circuit
    teleport_circuit = quantum_teleportation_circuit()
    run_and_visualize_circuit(teleport_circuit, "Quantum Teleportation")
    
    # Grover's Algorithm Circuit
    grover_circuit_obj = grover_circuit()
    run_and_visualize_circuit(grover_circuit_obj, "Grover Algorithm")
    
    print("\nAll circuit examples completed!")
    print("Check the generated PNG files for visualization results.")

if __name__ == "__main__":
    main()