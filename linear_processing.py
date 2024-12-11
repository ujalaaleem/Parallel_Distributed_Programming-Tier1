import pandas as pd
from collections import Counter
import time

def linear_processing(students_file, fees_file):
    students_df = pd.read_csv(students_file)
    fees_df = pd.read_csv(fees_file)

    student_dates = {}

    for index, student_row in students_df.iterrows():
        student_id = student_row['StudentID']

        student_fees = fees_df[fees_df['StudentID'] == student_id]
        fee_submission_dates = student_fees['PaymentDate'].tolist()

        student_dates[student_id] = fee_submission_dates

    all_dates = [date for dates in student_dates.values() for date in dates]
    date_frequency = Counter(all_dates)

    return date_frequency

students_file = "students.csv"
fees_file = "fees.csv"
date_frequency_linear = linear_processing(students_file, fees_file)

# Measure time for linear processing
start_time_linear = time.time()
date_frequency_linear = linear_processing("students.csv", "fees.csv")
end_time_linear = time.time()

print(f"Linear processing (linear processing) time: {end_time_linear - start_time_linear} seconds")

print("Most common fee submission dates (linear processing):")
for date, freq in date_frequency_linear.most_common(10):  # Top 10 most common dates
    print(f"{date}: {freq}")