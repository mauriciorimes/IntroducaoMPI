#writefile MPI_exemplo.py
#Importando as bibliotecas
from mpi4py import MPI
import random

random.seed(1)

#Iniciando o MPI
comm = MPI.COMM_WORLD
pid      = comm.Get_rank()          #PID do Processos atual
numProcs = comm.Get_size()          #total de processos iniciados
MaqNome  = MPI.Get_processor_name() #Nome da máquina

#Processo 0 vai gerar um número e encaminhar ao processo 1
if pid == 0:
  num_enviado = random.randint(1,10)
  print('Processo %d enviando %d' %(pid, num_enviado))
  for i in range(1, numProcs):
    comm.send(num_enviado, dest=i)
else:
  num_recebido = comm.recv(source=0)
  print('Processo %d recebendo %d' %(pid, num_recebido))
