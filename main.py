from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram

# Create a quantum circuit with one qubit and one classical bit
qc = QuantumCircuit(1, 1)

# Apply a Hadamard gate to the qubit
qc.h(0)

# Measure the qubit and store the result in the classical bit
qc.measure(0, 0)

# Print the quantum circuit
print("Quantum Circuit:")
print(qc.draw())
