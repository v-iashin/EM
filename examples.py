#==============================================================================
# EXAMPLE (EASY)
#==============================================================================
import random

mu1_true = 170
mu2_true = 100
sigma1_true = 7
sigma2_true = 6

# draws a set of random variable from two dist using given parameters
random.seed(a=0)
X1 = [random.gauss(mu=mu1_true, sigma=sigma1_true) for _ in range(5000)]
X2 = [random.gauss(mu=mu2_true, sigma=sigma2_true) for _ in range(5000)]

# round them to integers
X1 = [round(X1[i]) for i in range(len(X1))]
X2 = [round(X2[i]) for i in range(len(X2))]

# let's stack them together
X = X1 + X2

# let's plot them
import matplotlib as plt

plt.pyplot.hist(X, bins=40)

# EM-algorithm implementation
mu1_pred, sigma1_pred, mu2_pred, sigma2_pred = em_alg(X, 
                                                      mu1_ = 150, sigma1_ = 2, 
                                                      mu2_ = 200, sigma2_ = 16, 
                                                      n1 = 5000, n2 = 5000)

# let's compare the results with true values
print('true:', '\t', 'predicted:', '\n',
      mu1_true, '\t', round(mu1_pred, 2), '\n',
      sigma1_true, '\t', round(sigma1_pred, 2), '\n',
      mu2_true, '\t', round(mu2_pred, 2), '\n',
      sigma2_true, '\t', round(sigma2_pred, 2))


#==============================================================================
# EXAMPLE (HARD)
#==============================================================================
mu1_true = 172
mu2_true = 166
sigma1_true = 7
sigma2_true = 6

# draws a set of random variable from two dist using given parameters
random.seed(a=0)
X1 = [random.gauss(mu=mu1_true, sigma=sigma1_true) for _ in range(5000)]
X2 = [random.gauss(mu=mu2_true, sigma=sigma2_true) for _ in range(5000)]

# round them to integers
X1 = [round(X1[i]) for i in range(len(X1))]
X2 = [round(X2[i]) for i in range(len(X2))]

# let's stack them together
X = X1 + X2

# let's plot them
import matplotlib as plt

plt.pyplot.hist(X, bins=40)

# EM-algorithm implementation
mu1_pred, sigma1_pred, mu2_pred, sigma2_pred = em_alg(X, 
                                                      mu1_ = 151, sigma1_ = 8, 
                                                      mu2_ = 150, sigma2_ = 1, 
                                                      n1 = 9000, n2 = 1000)

# let's compare the results with true values
print('true:', '\t', 'predicted:', '\n',
      mu1_true, '\t', round(mu1_pred, 2), '\n',
      sigma1_true, '\t', round(sigma1_pred, 2), '\n',
      mu2_true, '\t', round(mu2_pred, 2), '\n',
      sigma2_true, '\t', round(sigma2_pred, 2))
