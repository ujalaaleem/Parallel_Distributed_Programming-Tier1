import pandas as pd
from collections import Counter
from multiprocessing import Pool
import time

def process_student(student_id, fees_df):
    student_fees = fees_df[fees_df['StudentID'] == student_id]
    return student_fees['PaymentDate'].tolist()

def parallel_processing_multiprocessing(students_file, fees_file):
    students_df = pd.read_csv(students_file)
    fees_df = pd.read_csv(fees_file)

    student_ids = students_df['StudentID'].tolist()

    # Using multiprocessing Pool to parallelize the task
    with Pool() as pool:
        results = pool.starmap(process_student, [(student_id, fees_df) for student_id in student_ids])

    all_dates = [date for dates in results for date in dates]
    date_frequency = Counter(all_dates)
    return date_frequency

# Measure time for multiprocessing
start_time_parallel = time.time()
date_frequency_parallel = parallel_processing_multiprocessing("students.csv", "fees.csv")
end_time_parallel = time.time()

print(f"Parallel processing (multiprocessing) time: {end_time_parallel - start_time_parallel} seconds")

# Print the most common fee submission dates
print("Most common fee submission dates (parallel processing):")
for date, freq in date_frequency_parallel.most_common(10):  # Top 10 most common dates
    print(f"{date}: {freq}")
