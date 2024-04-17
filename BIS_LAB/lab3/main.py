from tabulate import tabulate

from calculations import calculation_mechanism_quality_indicators, calculation_probabilities_threat_realization
from data_converters import limit_sufficiency_konf, limit_sufficiency_integrity_soi, limit_sufficiency_availability, \
    limit_sufficiency_integrity

print('\n\t\t\t Показатели качества механизмов')
mechanism_quality_indicators = list(calculation_mechanism_quality_indicators())
print(tabulate(mechanism_quality_indicators, tablefmt="grid"))

mechanism_quality_indicators_values = [i[2] for i in mechanism_quality_indicators]

#
# Расчет вероятностей реализации угроз конфиденциальности
#

print('\n\t\t\t Вероятность реализации угроз конфиденциальности')
print(tabulate(calculation_probabilities_threat_realization(
    mechanism_quality_indicators_values,
    limit_sufficiency_konf,
), tablefmt="grid"))

#
# Расчет вероятностей реализации угроз целостности
#

print('\n\t\t\t Вероятность реализации угроз целостности')
print(tabulate(calculation_probabilities_threat_realization(
    mechanism_quality_indicators_values,
    limit_sufficiency_integrity,
), tablefmt="grid"))

#
# Расчет вероятностей реализации угроз доступности
#

print('\n\t\t\t Вероятность реализации угроз доступности')
print(tabulate(calculation_probabilities_threat_realization(
    mechanism_quality_indicators_values,
    limit_sufficiency_availability,
), tablefmt="grid"))

#
# Расчет вероятностей реализации угроз целостности СОИ.
#
print('\n\t\t\t Вероятность реализации угроз целостности СОИ')
print(tabulate(calculation_probabilities_threat_realization(
    mechanism_quality_indicators_values,
    limit_sufficiency_integrity_soi,
), tablefmt="grid"))

