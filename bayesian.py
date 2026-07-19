from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('Rain', 'Sprinkler'),
    ('Rain', 'WetGrass'),
    ('Sprinkler', 'WetGrass')
])

cpd_rain = TabularCPD(variable='Rain', variable_card=2, values=[[0.8], [0.2]])

cpd_sprinkler = TabularCPD(
    variable='Sprinkler',
    variable_card=2,
    values=[[0.60, 0.99],
            [0.40, 0.01]],
    evidence=['Rain'],
    evidence_card=[2]
)

cpd_wet_grass = TabularCPD(
    variable='WetGrass',
    variable_card=2,
    values=[[1.00, 0.20, 0.10, 0.01],
            [0.00, 0.80, 0.90, 0.99]],
    evidence=['Rain', 'Sprinkler'],
    evidence_card=[2, 2]
)

model.add_cpds(cpd_rain, cpd_sprinkler, cpd_wet_grass)
inference = VariableElimination(model)

print(inference.query(variables=['Rain']))
print(inference.query(variables=['Sprinkler']))
print(inference.query(variables=['WetGrass']))

print(inference.query(variables=['Rain'], evidence={'WetGrass': 1}))
print(inference.query(variables=['Sprinkler'], evidence={'WetGrass': 1}))

print(inference.query(variables=['WetGrass'], evidence={'Rain': 1}))
print(inference.query(variables=['WetGrass'], evidence={'Sprinkler': 1}))
print(inference.query(variables=['Sprinkler'], evidence={'Rain': 1}))

print(inference.query(variables=['Rain'], evidence={'WetGrass': 1, 'Sprinkler': 1}))
print(inference.query(variables=['Sprinkler'], evidence={'WetGrass': 1, 'Rain': 1}))
print(inference.query(variables=['Rain'], evidence={'WetGrass': 1, 'Sprinkler': 0}))
