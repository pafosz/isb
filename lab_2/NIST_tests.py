from math import sqrt, erfc, fabs
import logging

def frequency_bitwise_test(sequence: str) -> float:
    try:
        s_n = sum([(-1 if bit == '0' else 1) for bit in sequence]) / sqrt(len(sequence))
        return erfc(fabs(s_n) / sqrt(2))
    except Exception as e:  
        logging.error(e)


