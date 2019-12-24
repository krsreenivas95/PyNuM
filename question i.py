import matplotlib.pyplot as plt
import numpy as np
def rk4(th,w,t,fd):
    dt=0.01
    g=1
    l=1
    ohm=2/3
    gam=0.5
    j=0
    tol=1e-6
    jmax=100
    k=lambda thet,om,t:(-(g/l)*np.sin(thet))-(gam*om)+(fd*np.sin(ohm*t)*om)
    while True:
        k1a=dt*w
        k1b=dt*k(th,w,t)
    
        k2a=dt*(w+(k1b/2))
        k2b=dt*k(th+(k1a/2),w+(k1b/2),t+(dt/2))

        k3a=dt*(w+(k2a/2))
        k3b=dt*k(th+(k2a/2),w+(k2b/2),t+(dt/2))

        k4a=dt*(w+k3a)
        k4b=dt*k(t+k3a,w+k3b,t+dt)

   
        th=th+((k1a+2*k2a+2*k3a+k4a)/6)
        w=w+((k1b+2*k2b+2*k3b+k4b)/6)
        t=t+dt
        j+=1

        if j >=jmax:
            break
    return(th,w)
print("Theta","\t\t\t","omega")

t=np.linspace(0,60,1000)
for i in [0,0.5,1.2]:
    s=[]
    l =[]
    
    print("for Fd= ",str(i))
    for j in t:
        m,k=rk4(0.2,0,j,i)
        s.append(m)
        l.append(k)
        print(m,"\t",k)
    plt.scatter(t,s,s=5,label="Theta")
    plt.scatter(t,l,s=5,label="omega")
    plt.xlabel("Time in seconds")
    plt.ylabel(" Theta and omega")
    plt.title("the Fd=")
    plt.legend()
    plt.show()
    list.clear(s)
    list.clear(s)
    
