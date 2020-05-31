from numba import cuda
import numpy as np
import pandas as pd
import algorithm as algo
import random
import Data.input as input
import time
start = time.process_time()


print("Initial Time Sum: " + str(algo.initial_stats[2]) + " seconds")


#@cuda.jit
def bruteforce(iterations):
    intra_key = []
    inter_key = []
    scores = []
    for i in range(iterations): #intraseed
        random.seed(i)
        temp_qa_matrix = random.sample(input.qa_matrix, algo.patient_amount)
        # print("--New Patient scramble---")
        for j in range(iterations):
            random.seed(j)
            inter_key.append(i)
            intra_key.append(j)
            # algo.field_array_dim(temp_qa_matrix)
            # print("--New field scramble---")
            for x in range(algo.patient_amount):  # the number of patients
                # print(len(temp_qa_matrix[x]))
                try: temp_qa_matrix[x] = random.sample(input.qa_matrix[x], len(input.qa_matrix[x]))
                except: continue


            scores.append((algo.time_delay_sum(
                algo.intrafraction_time_delay_sum(algo.patient_amount, algo.field_array_dim(input.qa_matrix),
                                                  temp_qa_matrix, ),
                algo.interfraction_time_delay_sum(algo.patient_amount, algo.field_array_dim(temp_qa_matrix),
                                                  temp_qa_matrix),
                algo.trs3_time_delay.rangeshift, algo.trs3_time_delay.depth, algo.trs3_time_delay.snout,
                algo.trs3_time_delay.rotation))[2])
    return scores, intra_key, inter_key

solution = bruteforce(500)
inter_key = solution[2]
intra_key = solution[1]

min_score = min(solution[0])
min_score_index = solution[0].index(min_score)


print("Minimum Time Sum: "+ str(min(solution[0])) + " seconds")
print("@index: " + str(min_score_index))
print("Time to complete: " + str(time.process_time() - start) + " seconds")

random.seed(0)
temp = random.sample(input.qa_matrix, algo.patient_amount)
for x in range(algo.patient_amount):  # the number of patients
    # print(len(temp_qa_matrix[x]))
    try:
        temp[x] = random.sample(input.qa_matrix[x], len(input.qa_matrix[x]))
    except:
        continue
print("--------------------------------")
print("Final Matrix: " + str(temp))
print("--------------------------------")

random.seed(inter_key[min_score_index])
min_qa_matrix = []
min_qa_matrix = random.sample(input.qa_matrix, len(algo.field_array_dim(input.qa_matrix)))
random.seed(intra_key[min_score_index])
for x in range(algo.patient_amount):  # the number of patients
    # print(len(temp_qa_matrix[x]))
    try:
        min_qa_matrix[x] = random.sample(input.qa_matrix[x], len(input.qa_matrix[x]))
    except:
        min_qa_matrix[x] = input.qa_matrix[x]
        continue

min_qa_matrix = np.roll(min_qa_matrix, -1)

for i in range(algo.patient_amount):
    min_qa_matrix[i] = np.array(min_qa_matrix[i]).squeeze()
min_qa_matrix = np.array(min_qa_matrix).squeeze()


df = pd.DataFrame(min_qa_matrix)
df.to_excel(excel_writer = "Data/output.xlsx")
print(str(algo.initial_stats[2] - min(solution[0])) + " seconds saved")
print("Excel file created")