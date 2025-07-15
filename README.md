#  Microsoft Cybersecurity Classifier

A machine learning project to automatically classify cybersecurity incidents (`TP`, `FP`, `BP`) using Microsoft’s GUIDE dataset — helping SOCs streamline threat triage, reduce alert fatigue, and improve enterprise response efficiency.

---

##  1. Project Overview

This project classifies security incidents into:

-  **True Positive (TP)** – actual threats  
-  **Benign Positive (BP)** – flagged but safe  
-  **False Positive (FP)** – incorrectly flagged

 **Dataset**: 4.75M rows sampled from the original 9.5M GUIDE dataset  
 **Goal**: Automate incident triage using machine learning  
 **Impact**: Supports SOC teams, improves alert handling, boosts accuracy

---

##  2. Feature Engineering

Feature engineering was a key step in improving model performance. It included:

-  **Datetime Feature Extraction** from `Timestamp`:
  - Extracted `Day`, `Month`, `Year`, `Hour`, and `Time`
-  **Categorical Encoding**:
  - Label Encoding for `Category`, `EntityType`, `EvidenceRole`, etc.
-  **Null Handling**:
  - Dropped columns with >50% nulls: `ActionGrouped`, `ActionGranular`, `MitreTechniques`
-  **Dropped High Cardinality Identifiers**:
  - `Sha256`, `AccountSid`, `DeviceId`, `FolderPath`, etc.
-  **Class Balance Analysis**:
  - Used stratified train-validation split to maintain distribution

---

##  3. Exploratory Data Analysis (EDA)

- Incident trends by **Hour**, **Day**, **Month**, and **Category**:

  ![Incidents](https://github.com/MugilCodes/Microsoft_cybersecurity_classifier/blob/main/images/Incidents.png)

- **Target imbalance** identified across TP, BP, and FP:

  ![Target Distribution](https://github.com/MugilCodes/Microsoft_cybersecurity_classifier/blob/main/images/Distribution_target_variable.png)

- **Correlation heatmap** for numerical features:

  ![Heatmap](https://github.com/MugilCodes/Microsoft_cybersecurity_classifier/blob/main/images/Correlation_Heatmap.png)

---

##  4. Model Training and Evaluation

###  Baseline Models

| Model               | Macro F1 Score |
|---------------------|----------------|
| Logistic Regression | 0.3936         |
| Decision Tree       | 0.9875 *(overfit)* |

![Baseline Comparison](https://github.com/MugilCodes/Microsoft_cybersecurity_classifier/blob/main/images/Baseline_model.png)

---

###  Advanced Models

| Model             | Macro F1 Score |
|------------------|----------------|
| Random Forest     | 0.8089         |
| Gradient Boosting | 0.8237         |
| XGBoost           | 0.8591         |
| LightGBM          | 0.8920         |
| **Tuned LightGBM**| **0.9418**     |

![Advanced Model Comparison](https://github.com/MugilCodes/Microsoft_cybersecurity_classifier/blob/main/images/Final_Comparision.png)

 **Train-Validation Split**: 70/30 (Stratified)

---

##  5. Feature Importance (SHAP)

To interpret the model, we used **SHAP (SHapley Additive Explanations)** — a game-theoretic approach to explain the output of tree-based models.

 **Top 5 Features**:

| Feature      |
|--------------|
| DetectorId   |   
| EntityType   |   
| EvidenceRole |      
| Hour         |      
| AlertTitle   |      

 **SHAP Plot**:

![SHAP](https://github.com/MugilCodes/Microsoft_cybersecurity_classifier/blob/main/images/Feature_Importance.png)

---

##  6. Final Evaluation on Test Set

Tested on **4.1 million unseen records** using a stratified approach.

| Metric     | TP (Class 0) | BP (Class 1) | FP (Class 2) | Macro Avg |
|------------|--------------|--------------|--------------|-----------|
| Precision  | 0.91         | 0.89         | 0.92         | 0.91      |
| Recall     | 0.93         | 0.84         | 0.93         | 0.90      |
| F1 Score   | 0.92         | 0.86         | 0.93         | 0.90      |

![TestData](https://github.com/MugilCodes/Microsoft_cybersecurity_classifier/blob/main/images/Test_Classification.png)

---

##  7. Results Summary

|  Attribute              |  Value                                           |
|--------------------------|----------------------------------------------------|
| Best Model               | Tuned LightGBM                                     |
| Validation Macro F1      | 0.9418                                             |
| Test Macro F1            | 0.9021                                             |
| Top Features (SHAP)      | DetectorId, EntityType, Hour, EvidenceRole, AlertTitle |
| Training Speed           | GPU Accelerated                                   |
| Explainability           | SHAP + Feature Analysis                           |

 **Benefits**:

- Balanced and robust classification  
- Supports real-time inference  
- Interpretable and efficient model pipeline

---

##  8. Recommendations

###  Deployment
- Expose the model via **FastAPI**
- Use **Docker** for containerization
- Deploy on **GPU-enabled servers** for latency-sensitive environments

###  Maintenance
- Retrain **monthly** with new alert data
- Monitor **prediction drift** and performance degradation
- Maintain **logs** for auditing predictions and debugging

###  Future Enhancements
- Add **textual features** using NLP (e.g., Alert Description, Category Names)
- Try **LSTM / Transformer-based** models for sequence-based learning
- Explore **ensemble models** (LightGBM + XGBoost + Neural Nets)

---

 **Timeline**: Completed in 1 week  
 **Author**: [Mugil]  
 **Repo**: `Microsoft_cybersecurity_classifier`
