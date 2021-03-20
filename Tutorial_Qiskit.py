# https://quantum-computing.ibm.com/lab/files/qiskit-tutorials/tutorials/circuits/1_getting_started_with_qiskit.ipynb

import numpy as np
from qiskit import *
from qiskit.visualization import matplotlib
# %matplotlib
from qiskit import Aer

# Create a Quantum Circuit acting on a quantum register of three qubits
circ = QuantumCircuit(3)
# Add a H gate on qubit 0, putting this qubit in superposition.
circ.h(0)
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting
# the qubits in a Bell state.
circ.cx(0, 1)
# Add a CX (CNOT) gate on control qubit 0 and target qubit 2, putting
# the qubits in a GHZ state.
circ.cx(0, 2)
backend = Aer.get_backend('statevector_simulator')
# Create a Quantum Program for execution
job = execute(circ, backend)
result = job.result()
outputstate = result.get_statevector(circ, decimals=3)
print(outputstate)