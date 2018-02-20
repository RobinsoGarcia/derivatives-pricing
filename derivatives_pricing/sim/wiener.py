import numpy as np

def eoption_value(S0,vol,rf,T,n):
        mu = rf-(0.5*vol**2)*T
        sigma = np.sqrt(T)*vol**2
        return S0*np.exp(sigma*np.random.randn(n)+mu)


def get_path(S0,vol,rf,T,N,n):

    dt = T/N

    drift = (rf-0.5*vol**2)*dt
    sigrootT = vol*np.sqrt(dt)

    def f(x):
        return np.multiply(x,np.exp(drift+sigrootT*np.random.randn(n)))

    results = np.empty((N+1,n))
    results[0] = S0
    time = []
    for i in np.arange(N)+1:
        results[i,:] = f(results[i-1])
        time.append(dt)

    mean_value = np.mean(results,axis=1)
    time =np.cumsum(np.array(time))

    return mean_value,time,results
