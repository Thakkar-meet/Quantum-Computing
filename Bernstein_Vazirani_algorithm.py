from qiskit import QuantumCircuit, assemble, Aer
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

def draw(qc):
    qc.draw(output='mpl')
    plt.show()


n = 6
s = "110101"
circuit = QuantumCircuit(n+1,n)

for i in range(n):
    circuit.h(i)
circuit.x(n)
circuit.h(n)
circuit.barrier()

rev_s = s[::-1]
for i in range(len(rev_s)):
    if rev_s[i] == "0":
        circuit.i(i)
    else:
        circuit.cx(i,n)
circuit.barrier()

for i in range(n):
    circuit.h(i)
circuit.barrier()

for i in range(n):
    circuit.measure(i,i)

draw(circuit)

aer_sim = Aer.get_backend("aer_simulator")
q_obj = assemble(circuit)
result = aer_sim.run(q_obj).result()
counts = result.get_counts(circuit)
print(counts)
plot_histogram(counts)
plt.show()

