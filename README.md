# Microsoft_cybersecurity_classifier
A machine learning project to automatically classify cybersecurity incidents (TP, FP, BP) using Microsoft’s GUIDE dataset to improve threat triage and response efficiency.

## 1. **Project Overview**

This project aims to automate the classification of cybersecurity incidents into three triage grades:
- **True Positive (TP)**
- **Benign Positive (BP)**
- **False Positive (FP)**

Using 4.75 million samples from Microsoft’s GUIDE dataset (original size: 9.5M), the model helps **Security Operations Centers (SOCs)** prioritize threats, reduce analyst fatigue, and improve enterprise security.

---

### 2. **Exploratory Data Analysis (EDA)**

- Visualized incident distributions across `Hour`, `Day`, `Month`, and `Category`.

  ![Hourly Incidents](./images/hourly_incidents.png)  
  ![Daily Incidents](./images/daywise_incidents.png)  
  ![Monthly Incidents](./images/monthly_incidents.png)  
  ![Category Distribution](./images/category.png)

- Identified significant class imbalance in the target (`IncidentGrade`):

  ![Target Distribution](./images/target_distribution.png)

- Correlation heatmap to understand co-linearity among numeric features:

  ![Heatmap](./images/heatmap.png)

---

### 3. **Model Training and Evaluation**

- **Baseline Models**:
  - Logistic Regression → Macro F1: 0.3936  
  - Decision Tree → Macro F1: 0.9875 (overfitting)

- **Advanced Models**:
  - Random Forest → Macro F1: 0.8089  
  - Gradient Boosting → Macro F1: 0.8237  
  - XGBoost → Macro F1: 0.8591  
  - LightGBM → Macro F1: 0.8920  
  - Tuned LightGBM → **Macro F1: 0.9418**

  ![Model Comparison](./images/all_models.png)

- Stratified Train-Validation split (70/30) ensured class balance across splits.

---

### 4. **Hyperparameter Tuning**

- Tuned **LightGBM** using `GridSearchCV` with GPU support.
- Best Parameters:
  ```python
  {
      'learning_rate': 0.1,
      'max_depth': 20,
      'n_estimators': 200,
      'num_leaves': 64
  }
5. Feature Importance
Used SHAP for model interpretation.

Top features included:

DetectorId

EntityType

EvidenceRole

Hour

AlertTitle



6. Final Evaluation
Evaluated on unseen test data (4.1M rows).

Final performance:

Metric	Class 0 (TP)	Class 1 (BP)	Class 2 (FP)	Macro Avg
Precision	0.91	0.89	0.92	0.91
Recall	0.93	0.84	0.93	0.90
F1 Score	0.92	0.86	0.93	0.90



 Results Summary
Best Model: Tuned LightGBM

Validation Macro F1 Score: 0.9418

Test Macro F1 Score: 0.9021

Top Features (SHAP): DetectorId, EntityType, Hour, EvidenceRole, AlertTitle

Model Benefits:

Balanced precision & recall for all classes

GPU-accelerated model with low latency

Explainable and efficient

 Recommendations
Deploy via: FastAPI + Docker

Use Cases:

Automated SOC triage

Alert suppression and escalation

Analyst assist dashboards with SHAP

Maintenance:

Retrain monthly

Monitor prediction drift

Audit logs for transparency

Future Improvements:

Include textual fields (e.g., AlertDescription) with NLP

Explore deep learning for time-sequence behavior

Add ensemble modeling for increased robustness

© 2025 – Project by [Mugil]



---

##  What You Need to Do:
1. Place your generated PNGs in the `/images/` folder:
   - `hourly_incidents.png`
   - `daywise_incidents.png`
   - `monthly_incidents.png`
   - `category.png`
   - `target_distribution.png`
   - `heatmap.png`
   - `all_models.png`
   - `hyperparameter_tuning.png`
   - `shap.png`
   - `test_eval.png`

2. Rename `[Your Name]` in the footer.

Would you like me to:
- Package this into a downloadable `.md` file?
- Help you generate the visualizations for missing image paths?

Let me know and I’ll do it right away.
