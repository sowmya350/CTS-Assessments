# Exercise 7: Financial Forecasting

## 1. Understand Recursive Algorithms
A recursive algorithm solves a problem by breaking it into a smaller version of the same problem. In this exercise, each new forecast is calculated from the latest historical value and the average change observed so far.

## 2. Setup
The program uses a simple financial forecasting model:
- Input: a list of past values
- Method: calculate the average change between consecutive values
- Goal: predict future values for a chosen number of periods

## 3. Implementation
The implementation is stored in `financial_forecasting.py`.

Run it with:

```bash
python financial_forecasting.py
```

## 4. Analysis
The forecasting logic is simple and easy to understand, but it works best when the data follows a fairly steady trend. If the values change unpredictably, the results may be less accurate.
