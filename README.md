# ReadMe

A set of data on Canadian Supreme Court cases circa late 2014, with focus on constitutional law cases. The goal was to use this historical data to predict how the Supreme Court would respond to a challenge to bill C-24.

A simple random forest model predicted that the court would strike down citizenship stripping provisions from bill C-24. 

This random forest model was fed into a GMCR model as part of a SYDE533 project.

# Data Format
**Case:** The informal name of the case

**Constitutional Challenge Succeeded:** 1 if the challenge succeeded, 0 otherwise

**Charter Right:** 1 if the case involved a charter right, or specifically referenced the CORF, 0 otherwise

**Federal Government:** 1 if the Federal Government, the Federal AG, or a Federal Law was challenged in the case, 0 otherwise

**Provincial Government:** 1 if a provincial government, provincial AG, or provincial law was challenged in the case, 0 otherwise

**Criminal:** 1 if the case dealt with a criminal conviction

**International:** 1 if the case dealt with international law, 0 otherwise

**Assenting Justices:** A `;` separated list of assenting justices, LastName(FirstName)

**Dissenting Justices:** A `;` separated list of dissenting justices, LastName(FirstName)

**Tag1:** First descriptive tag, gives information on the right the case deals with, or key thrust of the case

**Tag2:** Clarification or expansion of **tag1**
