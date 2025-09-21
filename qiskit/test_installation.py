#!/usr/bin/env python3
"""
Test script to verify Qiskit installation and basic functionality
"""

import sys

def test_qiskit_installation():
    """Test if Qiskit is properly installed and working"""
    print("Testing Qiskit installation...")
    
    try:
        # Test basic imports
        from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
        from qiskit_aer import AerSimulator
        print("✓ Basic Qiskit imports successful")
        
        # Test circuit creation
        qc = QuantumCircuit(1, 1)
        qc.h(0)
        qc.measure(0, 0)
        print("✓ Quantum circuit creation successful")
        
        # Test simulator
        simulator = AerSimulator()
        job = simulator.run(qc, shots=10)
        result = job.result()
        counts = result.get_counts(qc)
        print("✓ Quantum circuit simulation successful")
        print(f"  Sample result: {counts}")
        
        # Test visualization imports
        try:
            from qiskit.visualization import plot_histogram
            print("✓ Visualization modules available")
        except ImportError:
            print("⚠ Visualization modules not available (may need GUI environment)")
        
        print("\n🎉 Qiskit installation test PASSED!")
        print("All examples should work correctly.")
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        print("Please run './setup.sh' to install Qiskit")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

def main():
    """Main test function"""
    print("Qiskit Installation Test")
    print("=" * 30)
    
    success = test_qiskit_installation()
    
    if success:
        print("\nNext steps:")
        print("- Run 'python3 hello_world.py' for a simple example")
        print("- Run 'python3 quantum_circuits.py' for advanced examples")
        print("- Run 'jupyter notebook quantum_circuits_demo.ipynb' for interactive learning")
        sys.exit(0)
    else:
        print("\nPlease fix the installation issues and try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()