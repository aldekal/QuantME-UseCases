from qiskit import QuantumRegister, QuantumCircuit

# Truth table:
# q[1] | q[0] ||| q[3] | q[2]
#   0  |   0  |||   0  |   0
#   0  |   1  |||   0  |   1
#   1  |   0  |||   1  |   0
#   1  |   1  |||   1  |   1
# --> searched bit string: s = 00

qc = QuantumCircuit()

q = QuantumRegister(4, 'q')

qc.add_register(q)

qc.cx(q[0], q[2])
qc.cx(q[1], q[3])

def get_circuit(**kwargs):
    """Get oracle circuit."""
    return qc