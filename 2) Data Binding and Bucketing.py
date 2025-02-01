import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.stats as stats
np.random.seed(0)
mu=90
sigma=25
x=mu+sigma*
np.random.randn(5000)
num_bins=25
n,bins,patches=ax.hist(x,num_bins,density=1)
y=stats.norm.pdf(bins,mu,sigma)
ax.plot(bins,y,'--')
ax.set_x.label('Example Data')
x.set_ylabel('Probability density')
sTitle=r'Histogram'+str(len(x))+'entries into'+str(num_bins)+'Bins:$\mu='str(mu)+'$\sigma='+str(sigma)+'$'
ax.set_title(sTitle)
fig.tight_layout()
sPathFig='C:/VKHCG/05-DS/4000-UL/0200-DU/DU-Histogram.png'
fig.savefig(sPathFig)
plt.show()
    
