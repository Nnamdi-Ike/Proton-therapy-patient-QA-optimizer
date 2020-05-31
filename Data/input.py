import pandas as pd
import numpy as np
from math import isnan
from helper import Patient


patientQAData = 'Data/input.xlsx'
patientQAData = pd.read_excel(patientQAData)

raw_array_patient_data = patientQAData.to_numpy()


def nan_index(qa_array):
    nan_index = []
    for i in range(qa_array.shape[0]-1):
        if type(qa_array[i][2]) == float:
            if isnan(qa_array[i][2]):
                nan_index.append(i)
        else: continue
    return nan_index


white_space_index = nan_index(raw_array_patient_data)
no_space_patient_data = np.delete(raw_array_patient_data, white_space_index, 0)

patientList = []
for patient in range(len(no_space_patient_data)):
    patient = Patient(no_space_patient_data[patient][0], no_space_patient_data[patient][1])
    patientList.append(patient)

fieldList = []
for field in range(len(no_space_patient_data)):
    patientList[field].Field = patientList[field].Field(no_space_patient_data[field][2],
                                                        no_space_patient_data[field][3],
                                                        no_space_patient_data[field][4],
                                                        no_space_patient_data[field][5],
                                                        no_space_patient_data[field][6])


dimensions = 1
for i in range(0, len(patientList)-1):
    if patientList[i].mrn != patientList[i+1].mrn:
        dimensions += 1

mrn_value = set()
for i in range(len(patientList)):
    mrn_value.add(patientList[i].mrn)

print('Mrn Values: {}'.format(mrn_value))
# generate QA matrix
qa_matrix = []
temp = np.empty(0)
for i in mrn_value:
    stack = 0
    for j in range(len(patientList)):
        if patientList[j].mrn == i:
            stack += 1
            temp = np.append(temp,[patientList[j].mrn, patientList[j].name, patientList[j].Field.fname,
                                   patientList[j].Field.rangeshifter, patientList[j].Field.depth,
                                   patientList[j].Field.snout, patientList[j].Field.rotation])
            if stack > 1:
                temp = np.split(temp, stack)
            else:
                temp = np.expand_dims(temp, axis=0)
    qa_matrix.append(temp)
    temp = np.empty(0)
print("Imported QA Matrix: {}".format(qa_matrix))
