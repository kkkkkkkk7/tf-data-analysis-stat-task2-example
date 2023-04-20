import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 750949272 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
   level_of_trust = 0.8
b = 5
size_of_array = 10
significance_levels = np.random.uniform(low=0.092, high=b, size=size_of_array)
   num_greater = np.sum(significance_levels > level_of_trust)
