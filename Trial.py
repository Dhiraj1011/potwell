import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('Quantum Mechanics')
st.header('1-D Potential Well',divider='rainbow')

a=4
x=np.linspace(-a,a,100)

def psi(x, n):
    y = np.sqrt(2 / a) * np.sin((n * np.pi * x) / (a))
    return y

#n=int(input('enter the state:-'))
n=st.number_input('Enter the state')
st.text(n)
#print(x,psi(x,n))
plt.plot(x,(psi(x,n))**2,'--',label=rf'$\psi_{n}$')

plt.ylabel('$\psi(x)^2$')
plt.xlabel('x')
plt.xlim(0,4)
plt.ylim(bottom=0)
plt.savefig('graph.jpg')
st.image('graph.jpg')
#plt.show()

