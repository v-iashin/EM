#==============================================================================
# EM-algorithm
#==============================================================================

# function that calculates the approximation for parameters of two normal 
# distributions given: a list of numbers (X), initial values for parameters
# for the first dist (mu1 and sigma1), initial values for the second dist
# (mu2 and sigma2), how many elements correspond to each dist, and whether
# to show routine progress
#
# return in the following order: mu1, sigma1, mu2, sigma2
#
def em_alg(X, mu1_, sigma1_, mu2_, sigma2_, n1, n2, verbose=True):
    
    # function that returns a probability for a given quantile (norm dist)
    def dnorm(x, mu, sigma_sq):
        
        pi = 3.14159265359
        e  = 2.71828182846
        
        # calculating prob according to gaussian formula for normal pdf
        p = 1 / ((2 * pi * sigma_sq) ** 0.5) * e ** (-((x - mu) ** 2) / (2 * sigma_sq)) 
    
        return p

    # we need params list for calculating the diff between iterations
    params = [[mu1_, sigma1_, mu2_, sigma2_]]
    # mu_f0, mu_m0, sigma_m0, sigma_f0
    # setting up the initial values
    mu1, sigma1, mu2, sigma2 = params[0]
    i = 1
    delta = 1
    
    # while delta is too large impliment the algorithm
    while delta >= 0.1 and i <= 100:
        
        # E-step
        # calc the probability Pr(X_i | first dist) and Pr(X_i | second dist)
        P_X_1 = [dnorm(X[i], mu1, sigma1) for i in range(len(X))]
        P_X_2 = [dnorm(X[i], mu2, sigma2) for i in range(len(X))]
        
        # calc the Bayes' probability Pr(first dist | x_i) and Pr(second dist | x_i)
        # note: n1 should be the ratio of n1 in (n1 + n2) as well as n2
        # but you may factorize (n1 + n2) and eliminate this factor from fraction
        assert len(P_X_1) == len(P_X_2)
        P_1_X = [(P_X_1[i] * n1) / (P_X_1[i] * n1 + P_X_2[i] * n2) for i in range(len(P_X_1))]
        P_2_X = [(P_X_2[i] * n2) / (P_X_1[i] * n1 + P_X_2[i] * n2) for i in range(len(P_X_2))]
        
        # M-step
        # calc new mu and new sigma for both distributions
        sigma1 = sum([P_1_X[i] * (X[i] - mu1) ** 2 for i in range(len(X))]) / sum(P_1_X)
        sigma2 = sum([P_2_X[i] * (X[i] - mu2) ** 2 for i in range(len(X))]) / sum(P_2_X)
        
        # taking the square root from sigmas
        sigma1, sigma2 = sigma1 ** 0.5, sigma2 ** 0.5
        
        assert len(P_1_X) == len(X)
        mu1 = sum([P_1_X[i] * X[i] for i in range(len(X))]) / sum(P_1_X)
        mu2 = sum([P_2_X[i] * X[i] for i in range(len(X))]) / sum(P_2_X)
        
        # calc delta: the previous state - the new state and pop out the prev state
        params.append([mu1, sigma1, mu2, sigma2])
        delta = sum([abs(params[0][i] - params[1][i]) for i in range(len(params[0]))])
        params.pop(0)
        
        # if a user choose to see the progress
        if verbose == True:
            
            print('iteration:', i, 'delta =', delta)
        
        # add count after one iteration
        i += 1
            
    return mu1, sigma1, mu2, sigma2
