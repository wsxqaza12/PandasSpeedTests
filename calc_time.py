import time
import gc

def time_read_csv(read_function, file_path):
    start_time = time.time()
    df = read_function(file_path)
    read_time = time.time() - start_time
    del df  
    gc.collect()
    return read_time