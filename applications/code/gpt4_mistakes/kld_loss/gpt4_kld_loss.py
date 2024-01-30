import numpy as np
from scipy.stats import entropy

def kld(true_data, predicted_data):
   """
   This function calculates the Kullback–Leibler (KL) divergence loss between true_data and predicted_data.
   """
   loss = entropy(true_data, predicted_data)
   return loss