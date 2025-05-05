# SGPA Predictor using Linear Regression

This project predicts a student's SGPA using academic and lifestyle inputs. It uses a simple linear regression model from Scikit-learn.

---

## 📊 Dataset Used

- `sgpa_prediction_dataset.csv` contains:
  - Study Hours/Day
  - Previous SGPA
  - Attendance (%)
  - Assignment Submission Rate (%)
  - Sleep Hours/Day
  - SGPA (Target)

---

## 🔧 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

---

## 🚀 How It Works

1. Dataset is loaded and normalized.
2. Model is trained using Linear Regression.
3. It predicts SGPA on unseen data.
4. Output is evaluated using R² score.
5. Visualization compares predicted and actual SGPA.

---

## 📈 Example Output

- **R² Score:** Varies per run (usually decent for simple models)
- **Plot:** Actual vs Predicted SGPA values

---

## ▶️ Run It Yourself

```bash
pip install pandas matplotlib scikit-learn
python pj2.py

