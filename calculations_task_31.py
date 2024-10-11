import scipy.stats as stats
import numpy as np

# Данные о конверсиях
conversions = np.array([25000, 30000, 32000])
total_users = 40000 * 3  # общее количество пользователей
sample_size_per_group = 258086.253202639

# Текущая конверсия и ожидаемое улучшение
p1 = 0.05
p2 = 0.052

# Размер выборки для каждой группы
n = sample_size_per_group

# Расчет конверсий для каждой группы
p1_observed = conversions[0] / n
p2_observed = conversions[1] / n
p3_observed = conversions[2] / n

# Расчет стандартной ошибки
se_p1 = np.sqrt(p1_observed * (1 - p1_observed) / n)
se_p2 = np.sqrt(p2_observed * (1 - p2_observed) / n)
se_p3 = np.sqrt(p3_observed * (1 - p3_observed) / n)

# Z-статистика и p-значение
z1 = (p1_observed - p1) / se_p1
p_value1 = stats.norm.sf(abs(z1)) * 2  # двусторонний тест

z2 = (p2_observed - p1) / se_p2
p_value2 = stats.norm.sf(abs(z2)) * 2

z3 = (p3_observed - p1) / se_p3
p_value3 = stats.norm.sf(abs(z3)) * 2

# Результаты
results = {
    "Group 1": {"Observed Conversion": p1_observed, "Z-Statistic": z1, "P-Value": p_value1},
    "Group 2": {"Observed Conversion": p2_observed, "Z-Statistic": z2, "P-Value": p_value2},
    "Group 3": {"Observed Conversion": p3_observed, "Z-Statistic": z3, "P-Value": p_value3},
}

print(results)
