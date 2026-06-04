# Iris Classification Project Instructions

## Files
- `data/Iris.csv` - Iris dataset CSV file.
- `classify_iris.py` - Python classification program using a decision tree.
- `instruction.md` - This instruction file.

## Setup
1. Install required Python packages:
   ```bash
   pip install pandas scikit-learn
   ```

## Run the program
1. Open a terminal in the `Iris-ml-model` folder.
2. Run:
   ```bash
   python classify_iris.py
   ```

## What it does
- Loads `data/Iris.csv`.
- Uses feature columns `SepalLengthCm`, `SepalWidthCm`, `PetalLengthCm`, and `PetalWidthCm`.
- Trains a decision tree classifier.
- Prints test accuracy and a classification report.
- Predicts the species for a sample iris measurement.

## Notes
- The CSV file must remain in the `data` folder.
- The script is designed to be minimal and easy to run.
