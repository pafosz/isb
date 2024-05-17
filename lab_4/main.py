import multiprocessing as mp

from modules import work_with_files

cores = mp.cpu_count()
print("Ядер на железе:", cores)
