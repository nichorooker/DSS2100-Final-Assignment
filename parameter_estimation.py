import numpy as np
import pandas as pd


def bs_replicate_1d(data, func):
    """Generate bootstrap replicate of data"""

    # Generate random sample from data of same length as the data
    bs_sample = np.random.choice(data, len(data))
    
    # Return random sample under specified function
    return func(bs_sample)


def draw_bs_reps(data, func, size=1):
    """Draw specified number of bootstrap replicates"""

    # Initialise empty array of specified size to store replicates: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates and store them to the array
    for i in range(size):
        bs_replicates[i] = bs_replicate_1d(data, func)
        
    return bs_replicates


def main():
    """Generating 95% confidence interval for mean of 2 types of fish in given dataset"""

    # Read in the data
    fish_data = pd.read_csv('gandhi_et_al_bouts.csv', skiprows=4)

    # Store the relevant data in numpy arrays
    fish_mut = fish_data[fish_data.genotype == 'het'].bout_length
    fish_wt = fish_data[fish_data.genotype == 'wt'].bout_length
    
    # Generate new arrays of bootstrap replicates of the mean
    bs_reps_mut = draw_bs_reps(fish_mut, np.mean, size=10000)
    bs_reps_wt = draw_bs_reps(fish_wt, np.mean, size=10000)

    # Generate the 95% confidence interval of the mean
    conf_int_mut = np.percentile(bs_reps_mut, [2.5, 97.5])
    conf_int_wt = np.percentile(bs_reps_wt, [2.5, 97.5])

    # Print results
    print('95% confidence interval for mean bout length of mutant fish:', conf_int_mut)
    print('95% confidence interval for mean bout length of wild type fish:', conf_int_wt)


# Main guard so others can import script as module
if __name__ == "__main__":
    main()
