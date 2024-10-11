import math
from statsmodels.stats.power import zt_ind_solve_power


# Текущая конверсия и ожидаемое улучшение
p1 = 0.05
p2 = 0.052

# Альфа и бета
alpha = 0.03
power = 0.87

effect_size = (p2 - p1) / math.sqrt(p1 * (1 - p1))
print("Расчет среднего и разности пропорций ", effect_size)

sample_size_per_group = zt_ind_solve_power(effect_size=effect_size, nobs1=None, alpha=alpha, power=power, ratio=1.0)
print("Расчет размера выборки для одного теста ", sample_size_per_group)

daily_users = 40000 / 30
print("Количество пользователей в день ", daily_users)

total_users_needed = sample_size_per_group * 2
print("Количество пользователей, необходимых для одного теста ", total_users_needed)

days_needed = total_users_needed / daily_users
print("Количество дней для одного теста ", days_needed)

total_days_needed = days_needed * 3
print("Количество дней для всех трех тестов ", total_days_needed)

# Попробуем пересчитать необходимые параметры для теста с увеличенным ожидаемым улучшением до 0,5%.

# Новые параметры
p2_new = 0.055

effect_size_new = (p2_new - p1) / math.sqrt(p1 * (1 - p1))
print("Новое ожидаемое улучшение ", effect_size_new)

sample_size_per_group_new = zt_ind_solve_power(effect_size=effect_size_new, nobs1=None, alpha=alpha, power=power, ratio=1.0)
print("Новый расчет размера выборки для одного теста ", sample_size_per_group_new)

total_users_needed_new = sample_size_per_group_new * 2
print("Новое количество пользователей, необходимых для одного теста", total_users_needed_new)

days_needed_new = total_users_needed_new / daily_users
print("Новое количество дней для одного теста ", days_needed_new)

total_days_needed_new = days_needed_new * 3
print("Новое количество дней для всех трех тестов", total_days_needed_new)
