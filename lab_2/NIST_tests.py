from math import sqrt, erfc
import logging

PI = {0: 0.2148, 1: 0.3672, 2: 0.2305, 3: 0.1875}

def frequency_bitwise_test(sequence: str) -> float:
    try:
        s_n = sum([(-1 if bit == '0' else 1) for bit in sequence]) / sqrt(len(sequence))
        return erfc(abs(s_n) / sqrt(2))
    except Exception as e:  
        logging.error(e)

def same_consecutive_bits_test(sequence: str) -> float:
    try:
        percentage_of_units = sequence.count("1") / len(sequence)
        if abs((percentage_of_units - 0.5)) >= 2 / sqrt(len(sequence)):
            return 0 
        v_n = sum([(0 if sequence[i] == sequence[i + 1] else 1) for i in range(0, (len(sequence) - 1))])

        return erfc((abs(v_n - (2 * len(sequence) * percentage_of_units * (1 - percentage_of_units))))
                    / (2 * sqrt(2 * len(sequence)) * percentage_of_units * (1 - percentage_of_units)))
    except Exception as e:
        logging.error(e)

#def longest_sequence_test(sequence: str) -> float:

