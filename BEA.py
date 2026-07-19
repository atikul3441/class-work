from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


model = DiscreteBayesianNetwork([
    ("Burglary", "Alarm"),
    ("Earthquake", "Alarm"),
    ("Alarm", "John Call"),
    ("Alarm", "Marry Call")
])

cpd_B = TabularCPD(
    variable="Burglary",
    variable_card=2,
    values=[[0.99], [0.01]]
)

cpd_E = TabularCPD(
    variable="Earthquake",
    variable_card=2,
    values=[[0.998], [0.002]]
)

cpd_A = TabularCPD(
    variable="Alarm",
    variable_card=2,
    values=[
        [0.999, 0.71, 0.06, 0.05], 
        [0.001, 0.29, 0.94, 0.95] 
 ],
    evidence=["Burglary", "Earthquake"],
    evidence_card=[2,2]
)

cpd_J = TabularCPD(
    variable="John Call",
    variable_card=2,
    values=[
        [0.95, 0.10],   
        [0.05, 0.90]  
 ],
    evidence=["Alarm"],
    evidence_card=[2]
)

cpd_M = TabularCPD(
    variable="Marry Call",
    variable_card=2,
    values=[
        [0.99, 0.30],   
        [0.01, 0.70]  
 ],
    evidence=["Alarm"],
    evidence_card=[2]
)

model.add_cpds(cpd_B, cpd_E, cpd_A, cpd_J, cpd_M)

print(model.check_model())




infer = VariableElimination(model)

print("Probability of John calling: \n",infer.query(variables=["John Call"]))
print()
print()
print("Probability of Merry calling: \n",infer.query(variables=["Marry Call"]))
print()
print()
print("Probability of Alarm given no Burglary and no Earthquake: \n",infer.query(variables=["Alarm"], evidence={"Burglary": 0,"Earthquake": 0}))
print()
print()
