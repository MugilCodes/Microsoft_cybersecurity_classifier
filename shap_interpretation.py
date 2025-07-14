# shap_interpretation.py

import shap
import matplotlib.pyplot as plt

def explain_model_with_shap(model, X_sample, max_display=20):
    print("[INFO] Generating SHAP explanations...")

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_sample)

    print("[INFO] Plotting SHAP summary plot...")
    shap.summary_plot(shap_values, X_sample, plot_type="bar", max_display=max_display)
    plt.show()

    print("[INFO] Plotting SHAP detailed plot for all classes...")
    shap.summary_plot(shap_values, X_sample, max_display=max_display)
    plt.show()
