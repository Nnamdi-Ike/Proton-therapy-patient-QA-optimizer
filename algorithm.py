import pandas as pd
import numpy as np
from Data import input
from helper import TimeDelay
import operator


def field_array_dim(matrix):
    field_dimensions = 0
    field_array_dim = []
    dummy_matrix = []
    for i in range(input.dimensions):
        for j in range(20):
            try:
                dummy_matrix.append(matrix[i][j])
                field_dimensions += 1
            except:
                field_array_dim.append(field_dimensions)
                field_dimensions = 0
                break

    return field_array_dim


patient_amount = len(field_array_dim(input.qa_matrix))

print('----------------------------------------')
print("Patients and Field: " + str(field_array_dim(input.qa_matrix)))
print('----------------------------------------')

trs3_time_delay = TimeDelay(40, 60, 25, 120)


def intrafraction_time_delay_sum(patient_amount, field_dim, matrix):
    range_shift_factor = 0
    depth_factor = 0
    snout_factor = 0
    rotation_factor = 0

    for i in range(patient_amount):  # the number of patients
        for j in range(field_dim[i]):  # the patient field index
            try:
                if matrix[i][j][3] == matrix[i][j + 1][3] and matrix[i][j][3] == matrix[i][j - 1][3]:
                    range_shift_factor += 0
                    continue
                else:
                    raise Exception

            except:
                # print("adjacent equals at depth exception raised at {}, {}".format(i, j))
                try:
                    if matrix[i][j][3] != matrix[i][j + 1][3] and matrix[i][j][3] != matrix[i][j - 1][3]:
                        if j - 1 < 0:
                            range_shift_factor += 1
                        else:
                            range_shift_factor += 2
                        continue
                    else:
                        raise Exception

                except:
                    try:
                        # print("adjacent non-equals at depth exception raised at {}, {}".format(i, j))
                        if matrix[i][j][3] != matrix[i][j + 1][3] or matrix[i][j][3] != matrix[i][j - 1][3]:
                            if j - 1 < 0:
                                range_shift_factor += 0
                            else:
                                range_shift_factor += 1
                            continue
                        else:
                            raise Exception
                    except:
                        try:
                            # print("Either or non-equals at depth exception raised at {}, {}".format(i, j))
                            if matrix[i][j][3] != matrix[i][j - 1][3]:
                                if j - 1 < 0:
                                    range_shift_factor += 0
                                else:
                                    range_shift_factor += 1
                                continue
                            else:
                                raise Exception
                        except:
                            try:
                                # print("before non-equals at depth exception raised at {}, {}".format(i, j))
                                if matrix[i][j][3] != matrix[i][j + 1][3]:
                                    range_shift_factor += 1
                                    continue
                            except:
                                range_shift_factor += 0
                                # print("potential time delay range shifter error {}, {}".format(i, j))

        for k in range(field_dim[i]):  # the patient field index
            try:
                if matrix[i][k][4] == matrix[i][k + 1][4] and matrix[i][k][4] == matrix[i][k - 1][4]:
                    depth_factor += 0
                    continue
                else:
                    raise Exception

            except:
                # print("adjacent equals at depth exception raised at {}, {}".format(i, k))
                try:
                    if matrix[i][k][4] != matrix[i][k + 1][4] and matrix[i][k][4] != matrix[i][k - 1][4]:
                        if k - 1 < 0:
                            depth_factor += 1
                        else:
                            depth_factor += 2
                        continue
                    else:
                        raise Exception

                except:
                    try:
                        # print("adjacent non-equals at depth exception raised at {}, {}".format(i, k))
                        if matrix[i][k][3] != matrix[i][k + 1][4] or matrix[i][k][4] != matrix[i][k - 1][4]:
                            if k - 1 < 0:
                                depth_factor += 0
                            else:
                                depth_factor += 1
                            continue
                        else:
                            raise Exception
                    except:
                        try:
                            # print("Either or non-equals at depth exception raised at {}, {}".format(i, k))
                            if matrix[i][k][4] != matrix[i][k - 1][4]:
                                if k - 1 < 0:
                                    depth_factor += 0
                                else:
                                    depth_factor += 1
                                continue
                            else:
                                raise Exception
                        except:
                            try:
                                # print("before non-equals at depth exception raised at {}, {}".format(i, k))
                                if matrix[i][k][4] != matrix[i][k + 1][4]:
                                    depth_factor += 1
                                    continue
                            except:
                                depth_factor += 0
                                # print("potential time delay depth error {}, {}".format(i, k))

        for l in range(field_dim[i]):  # the patient field index
            if l - 1 >= 0:
                try:
                    if matrix[i][l][5] >= matrix[i][l + 1][5] and matrix[i][l][5] <= matrix[i][l - 1][5]:
                        snout_factor += 0
                        continue
                    else:
                        raise Exception

                except:
                    try:
                        if matrix[i][l][5] <= matrix[i][l + 1][5] and matrix[i][l][5] >= matrix[i][l - 1][5]:
                            snout_factor += 0
                            continue
                        else:
                            snout_factor += 1
                    except:
                        continue

            else:
                continue
            # print("potential time delay snout error {}, {}".format(i, j))

            continue

        for m in range(field_dim[i]):  # the patient field index
            try:
                if matrix[i][m][3] == matrix[i][m + 1][6] and matrix[i][m][6] == matrix[i][m - 1][6]:
                    rotation_factor += 0
                    continue
                else:
                    raise Exception

            except:
                # print("adjacent equals at depth exception raised at {}, {}".format(i, l))
                try:
                    if matrix[i][m][6] != matrix[i][m + 1][6] and matrix[i][m][6] != matrix[i][m - 1][6]:
                        if m - 1 < 0:
                            rotation_factor += 1
                        else:
                            rotation_factor += 2
                        continue
                    else:
                        raise Exception

                except:
                    try:
                        # print("adjacent non-equals at depth exception raised at {}, {}".format(i, l))
                        if matrix[i][m][6] != matrix[i][m + 1][6] or matrix[i][m][6] != matrix[i][m - 1][6]:
                            if m - 1 < 0:
                                rotation_factor += 0
                            else:
                                rotation_factor += 1
                            continue
                        else:
                            raise Exception
                    except:
                        try:
                            # print("Either or non-equals at depth exception raised at {}, {}".format(i, l))
                            if matrix[i][m][6] != matrix[i][m - 1][6]:
                                if m - 1 < 0:
                                    rotation_factor += 0
                                else:
                                    rotation_factor += 1
                                continue
                            else:
                                raise Exception
                        except:
                            try:
                                # print("before non-equals at depth exception raised at {}, {}".format(i, l))
                                if matrix[i][m][5] != matrix[i][m + 1][6]:
                                    rotation_factor += 1
                                    continue
                            except:
                                rotation_factor += 0
                                # print("potential time delay rotation error {}, {}".format(i, m))

    return int(range_shift_factor / 2), int(depth_factor / 2), int(snout_factor), int(rotation_factor / 2)


def interfraction_time_delay_sum(patient_amount, field_dim, matrix):
    range_shift_factor = 0
    depth_factor = 0
    snout_factor = 0
    rotation_factor = 0

    # last element vs first element of the next patient
    for i, j in zip(range(patient_amount), field_dim):
        try:
            if matrix[i][j - 1][3] == matrix[i + 1][0][3]:
                range_shift_factor += 0
                # print('F = 0: {}, {}'.format(i, j))
            else:
                range_shift_factor += 1
                # print('F = 1: {}, {}'.format(i, j))
        except:
            # print('Error = 0: {}, {}'.format(i, j))
            continue

    for i, k in zip(range(patient_amount), field_dim):
        try:
            if matrix[i][k - 1][4] == matrix[i + 1][0][4]:
                depth_factor += 0
            else:
                depth_factor += 1
        except:
            continue

    for i, l in zip(range(patient_amount), field_dim):
        try:
            if matrix[i][l - 1][5] == matrix[i + 1][0][5]:
                snout_factor += 0
            else:
                snout_factor += 1
        except:
            continue

    for i, m in zip(range(patient_amount), field_dim):
        try:
            if matrix[i][m - 1][6] == matrix[i + 1][0][6]:
                rotation_factor += 0
            else:
                rotation_factor += 1
        except:
            continue
    return range_shift_factor, depth_factor, snout_factor, rotation_factor


def time_delay_sum(intrafraction, interfraction, range_shifter_time, depth_time, snout_time, rotation_time):
    intrafraction_weighted = []
    interfraction_weighted = []
    for i, j in zip(intrafraction, [range_shifter_time, depth_time, snout_time, rotation_time]):
        intrafraction_weighted.append(i * j)

    for i, j in zip(interfraction, [range_shifter_time, depth_time, snout_time, rotation_time]):
        interfraction_weighted.append(i * j)

    total_sum = sum(list(map(operator.add, intrafraction_weighted, interfraction_weighted)))
    return intrafraction_weighted, interfraction_weighted, total_sum


print(time_delay_sum(
    intrafraction_time_delay_sum(patient_amount, field_array_dim(input.qa_matrix), input.qa_matrix, ),
    interfraction_time_delay_sum(patient_amount, field_array_dim(input.qa_matrix), input.qa_matrix),
    trs3_time_delay.rangeshift, trs3_time_delay.depth, trs3_time_delay.snout, trs3_time_delay.rotation))

initial_stats = time_delay_sum(
    intrafraction_time_delay_sum(patient_amount, field_array_dim(input.qa_matrix), input.qa_matrix, ),
    interfraction_time_delay_sum(patient_amount, field_array_dim(input.qa_matrix), input.qa_matrix),
    trs3_time_delay.rangeshift, trs3_time_delay.depth, trs3_time_delay.snout, trs3_time_delay.rotation)
