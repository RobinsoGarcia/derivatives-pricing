import numpy as np

def get_path(S0,vol,rf,T,N,n):
    '''
    S0
    vol
    rf
    N - number of time steps
    n - number of simulations


    dt = T/N
    mu = np.log(S0)+(rf-0.5*vol**2)*dt
    sigma = dt*vol**2

    results = np.random.normal(mu,sigma)[np.newaxis,:]
    for x in np.arange(n-1):
        results = np.vstack((results,np.random.normal(mu,sigma)[np.newaxis,:]))

    mean_value = np.mean(results,axis=0)

    '''
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
