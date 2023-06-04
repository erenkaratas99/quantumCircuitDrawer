from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram


qc = QuantumCircuit(3)

qc.h(0)

qc.swap(0, 2)
qc.h(2)
qc.cp(-3.14159/2, 1, 2)
qc.h(1)
qc.cp(-3.14159/4, 0, 2)
qc.cp(-3.14159/2, 0, 1)
qc.h(0)

qc.h(1)

qc.cp(0, 0, 1)


qc.measure_all()

qc.draw('mpl')
