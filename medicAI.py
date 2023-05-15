symptoms = open("symptoms.txt", 'r').read()

medicAI = "ai_goals: \n- 'Research possible diagnoses for: " + symptoms + "'\n- Narrow down the current diagnoses to the 5 that are most likely to be correct. the diagnoses will be listed from 5 being least likely and 1 being most likely\n- also find common treatments for each of the five diagnoses\n- Save the list of diagnoses and common treatments as a text file\n- Exit when finished\nai_name: MedicAI\nai_role: an AI designed to diagnose medical problems and create a list of 5 diagnoses"
YAML = open("diagnose.yaml", "w")
YAML.write(medicAI)
YAML.close()

from os import system
system("python3 -m autogpt -c --ai-settings diagnose.yaml")