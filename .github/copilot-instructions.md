# Quantum Programming Playground

A comprehensive quantum programming playground with IBM Qiskit (Python) and Azure Quantum (Q#) examples for learning quantum computing concepts and algorithms.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

### Initial Setup and Dependencies
- **Python 3.12+ is required** - Available at `/usr/bin/python3`
- **pip3 is required** - Available at `/home/runner/.local/bin/pip3`
- **Git is available** - Available at `/usr/bin/git`

### Setting Up Qiskit Environment (Python)
- Navigate to the `qiskit/` directory: `cd qiskit`
- Run the setup script: `./setup.sh` -- takes 60 seconds to complete. NEVER CANCEL. Set timeout to 120+ seconds.
  - **Note**: Setup may fail due to network timeouts but packages are often cached and examples still work
- Test installation: `python3 test_installation.py` -- takes 1 second.
  - **Critical**: This test confirms if examples will work regardless of setup script output

### Setting Up Q# Environment
- Install Q# Python integration: `pip3 install qsharp` -- takes 5 seconds.
- Test Q# capability: `python3 -c "import qsharp; qsharp.init(); print('Q# ready')"` -- takes 0.5 seconds.

### Core Examples and Execution Times
- **Hello World (Qiskit)**: `python3 hello_world.py` -- takes 1.2 seconds.
- **Quantum Circuits (Qiskit)**: `python3 quantum_circuits.py` -- takes 1 second.
- **Installation Test**: `python3 test_installation.py` -- takes 0.7 seconds.

## Validation and Testing

### CRITICAL Validation Steps
Always run the complete validation scenario after making changes:

1. **Setup Qiskit**: `cd qiskit && ./setup.sh` -- NEVER CANCEL: 60 seconds
2. **Test Installation**: `python3 test_installation.py` -- 1 second
3. **Run Hello World**: `python3 hello_world.py` -- 1.2 seconds  
4. **Run Quantum Circuits**: `python3 quantum_circuits.py` -- 1 second
5. **Verify PNG Generation**: `ls -la *.png` -- Should show 4 PNG files
6. **Test Q#**: `cd ../azure_quantum && python3 -c "import qsharp; qsharp.init(); print('Q# ready')"` -- 0.5 seconds

### Manual Validation Requirements
After making changes to quantum examples:
- **ALWAYS** run both hello_world.py and quantum_circuits.py to ensure quantum functionality works
- **ALWAYS** verify PNG files are generated (bell_state_results.png, grover_algorithm_results.png, hello_world_results.png, quantum_teleportation_results.png)
- **ALWAYS** check that Qiskit examples produce expected measurement results (roughly 50/50 distributions for superposition, correlated results for entanglement)

### Expected Output Validation
- **Hello World**: Should show roughly 50% |0⟩ and 50% |1⟩ results due to superposition
- **Bell State**: Should show correlated measurements (00 and 11 states, roughly 50/50)
- **Grover's Algorithm**: Should show amplified |11⟩ state (close to 100%)
- **Quantum Teleportation**: Should show distributed results across all 8 possible 3-bit states

## Repository Structure and Navigation

### Key Directories
- **`qiskit/`**: IBM Qiskit Python examples with setup script and Jupyter notebook
- **`azure_quantum/`**: Azure Quantum Q# examples (4 .qs files)
- **`.vscode/`**: VS Code configuration (minimal launch.json)

### Important Files
- **`qiskit/setup.sh`**: Main setup script for Qiskit environment
- **`qiskit/requirements.txt`**: Python dependencies (qiskit>=1.0.0, qiskit-aer>=0.14.0, matplotlib>=3.5.0, numpy>=1.20.0, jupyter>=1.0.0)
- **`qiskit/test_installation.py`**: Installation verification script
- **`qiskit/hello_world.py`**: Basic superposition example
- **`qiskit/quantum_circuits.py`**: Advanced quantum algorithms (Bell state, teleportation, Grover's)
- **`qiskit/quantum_circuits_demo.ipynb`**: Interactive Jupyter notebook
- **`azure_quantum/*.qs`**: Q# source files (hello_world.qs, cnot_entaglement.qs, random_numbers.qs, teleport.qs)

### Generated Files
The examples generate PNG visualization files in the `qiskit/` directory:
- `hello_world_results.png`
- `bell_state_results.png`
- `quantum_teleportation_results.png` 
- `grover_algorithm_results.png`

## Common Development Tasks

### Running Qiskit Examples
```bash
cd qiskit
./setup.sh                           # Setup (60s, NEVER CANCEL)
python3 test_installation.py         # Verify (1s)
python3 hello_world.py              # Basic example (1.2s)
python3 quantum_circuits.py         # Advanced examples (1s)
```

### Running Jupyter Notebooks
```bash
cd qiskit
jupyter notebook quantum_circuits_demo.ipynb    # Interactive mode
# OR convert to script for testing:
jupyter nbconvert --to script quantum_circuits_demo.ipynb --stdout  # (2.5s)
```

### Working with Q# Files
- Q# files are in `azure_quantum/` directory
- Q# files can be viewed and studied but require Q# tooling for full execution
- Basic Q# operations can be tested via Python: `python3 -c "import qsharp; qsharp.init(); qsharp.eval('use q = Qubit(); H(q); M(q)')"`

### Code Quality and Linting
- No formal linting tools are configured in this repository
- Use basic Python syntax checking: `python3 -m py_compile qiskit/*.py`
- Follow the existing code style in the repository

## Common Issues and Solutions

### Setup Issues
- **"pip3 not found"**: The setup script handles this automatically with apt-get
- **"Permission denied"**: Use `chmod +x qiskit/setup.sh` if needed
- **Network timeout during setup**: Packages may be cached; run `python3 test_installation.py` to verify if examples work
- **Import errors**: Always run `python3 test_installation.py` to verify before running examples

### Execution Issues  
- **"Could not display plot"**: This is normal in headless environments; PNG files are still generated
- **Q# execution errors**: Q# files are for study; use the Python qsharp module for actual execution
- **Jupyter issues**: Ensure you're in the `qiskit/` directory when running jupyter commands

### File Generation Issues
- **Missing PNG files**: Re-run the specific example that should generate them
- **Empty results**: Check that qiskit-aer simulator is properly installed via setup.sh

## No Build System or CI/CD
- This repository has no formal build system, Makefile, or GitHub Actions workflows
- No automated testing beyond the provided test_installation.py script
- No deployment or packaging requirements

## Learning Resources and Next Steps
- Start with `qiskit/hello_world.py` for basic quantum concepts
- Progress to `qiskit/quantum_circuits.py` for advanced algorithms  
- Use `qiskit/quantum_circuits_demo.ipynb` for interactive learning
- Study Q# examples in `azure_quantum/` for different quantum programming approaches
- Refer to generated PNG files for visual understanding of quantum measurement results

## Time Estimates Summary
- **Initial Setup**: 60 seconds (Qiskit) + 5 seconds (Q#) = ~65 seconds total
- **Testing**: ~4 seconds for complete validation
- **Development Cycle**: ~2-3 seconds per example execution
- **NEVER CANCEL**: All setup commands should be given adequate timeout (120+ seconds minimum)