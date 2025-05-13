import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError ("List must contain nine numbers.")
    
    # Convert list into 3x3 NumPy Array
    matrix = np.array(list).reshape(3, 3)

    # Perform calculations
    mean = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix).tolist()]
    variance = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix).tolist()]
    standard_deviation = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix).tolist()]
    max_value = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix).tolist()]
    min_value = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix).tolist()]
    sum_value = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix).tolist()]

    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': standard_deviation,
        'max': max_value,
        'min': min_value,
        'sum': sum_value
    }

    return calculations
