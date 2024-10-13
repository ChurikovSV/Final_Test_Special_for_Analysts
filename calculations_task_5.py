import numpy as np
from scipy.stats import ttest_ind

# Данные группы A
mean_a = 360
std_dev_a = 40
n_a = 9802

# Данные группы B
mean_b = 352
std_dev_b = 58
n_b = 9789

# Генерация выборок на основе предоставленных параметров
np.random.seed(42)  # Для воспроизводимости результатов
data_a = np.random.normal(mean_a, std_dev_a, n_a)
data_b = np.random.normal(mean_b, std_dev_b, n_b)

# Двухвыборочный t-тест для независимых выборок с предположением о неравных дисперсиях
t_stat, p_value = ttest_ind(data_a, data_b, equal_var=False)

print(t_stat, p_value)
