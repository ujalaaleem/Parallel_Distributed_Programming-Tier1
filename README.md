
## **Ujala Aleem (21B-104-CS-A)**
---
# Student Fee Submission Analysis: Linear vs Parallel Processing

This assignment demonstrates the use of linear and parallel processing techniques to analyze student fee submission patterns. The goal is to identify the most common fee submission dates and compare execution times between the two approaches.

---
## **Assignment Overview**

This assignment focuses on:
- **Linear Processing**: A step-by-step sequential approach for processing data, suitable for smaller datasets.
- **Parallel Processing**: A faster alternative that uses Python’s `multiprocessing` module, ideal for handling large datasets efficiently.

The assignment analyzes two CSV files:
1. `students.csv`: Contains student details:
   - `StudentID`: Unique identifier for each student.
   - `Name`: Name of the student.
   - `Gender`: Gender of the student.
   - `EnrollmentYear`: The year the student enrolled.
2. `fees.csv`: Contains fee payment records:
   - `FeeID`: Unique identifier for each fee payment record.
   - `StudentID`: Reference to the student making the payment.
   - `Semester`: Semester for which the fee is paid.
   - `Amount`: Fee amount paid.
   - `PaymentDate`: Date the payment was made.

Both approaches calculate the frequency of fee submission dates and list the most common dates along with their frequencies.

---

## **How to Run the assignment**

### **1. Setup the Environment**
1. Create a virtual environment:
   ```bash
   python -m venv env
   ```
2. Activate the virtual environment:
   - **Windows**:
     ```bash
     env\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source env/bin/activate
     ```
3. Install the required library:
   ```bash
   pip install pandas
   ```

### **2. Run the Scripts**

#### **For Linear Processing**
Execute the linear processing script:
```bash
python linear_processing.py
```

#### **For Parallel Processing**
Execute the parallel processing script:
```bash
python parallel_processing.py
```

---

# Time Comparison: Linear vs Parallel Processing

Here is a comparison of the execution times between the linear and parallel processing approaches.
### **Linear Processing**
- **Execution Time**: **100.98 seconds**
### **Parallel Processing**
- **Execution Time**: **82.57 seconds**

![Time Comparison](assets/processing_time_comparison.png)

- **Top 10 Most Common Fee Submission Dates**:
  | Date       | Frequency |
  |------------|-----------|
  | 2024-02-23 | 3609      |
  | 2024-02-16 | 3571      |
  | 2024-02-29 | 3540      |
  | 2024-02-13 | 3526      |
  | 2024-02-17 | 3526      |
  | 2024-02-28 | 3520      |
  | 2024-02-12 | 3500      |
  | 2024-02-11 | 3493      |
  | 2024-02-07 | 3464      |
  | 2024-02-10 | 3452      |

---

## **Features**
1. Linear approach to process fee submission data step by step.
2. Parallel approach using Python’s `multiprocessing` module for faster execution.
3. Analysis of the most frequent fee submission dates.
4. Comparison of execution times to demonstrate performance improvements.

---

## **Dependencies**
This assignment uses:
- **pandas**: For efficient data manipulation and analysis.
- **multiprocessing**: To implement parallel processing.

---
