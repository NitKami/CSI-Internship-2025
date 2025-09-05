## 📋 Project Overview

This week's assignment focused on the crucial machine learning processes of model evaluation and hyperparameter tuning. The goal was to build, evaluate, and optimize several classification models using the classic Wine dataset from Scikit-learn.

The project demonstrates how to assess a model's performance using various metrics and how to systematically improve it by searching for the optimal combination of hyperparameters. Three different models were compared: Support Vector Machine (SVM), Random Forest, and Logistic Regression.

## 📚 Key Concepts & Techniques

This project covers several core machine learning concepts:

* **Model Evaluation Metrics:** Understanding and calculating key metrics to measure model performance:
    * **Accuracy:** The proportion of correctly classified instances.
    * **Precision:** The ability of the classifier not to label a negative sample as positive.
    * **Recall:** The ability of the classifier to find all the positive samples.
    * **F1-Score:** A weighted average of Precision and Recall.
    * **Classification Report:** A comprehensive report showing the main classification metrics on a per-class basis.
* **Feature Scaling:** Using `StandardScaler` to standardize features, which is essential for distance-based algorithms like SVM.
* **Hyperparameter Tuning:** The process of finding the optimal parameters for a model to improve its performance.
    * **GridSearchCV:** An exhaustive search over a specified parameter grid to find the best combination of hyperparameters.
    * **RandomizedSearchCV:** A search over a randomized subset of the parameter space, which is more efficient for large search spaces.
* **Pipelines:** Using `sklearn.pipeline` to streamline workflows by chaining multiple processing steps (like scaling and modeling) together.

## 🛠️ Tools & Libraries Used

* **Language:** `Python`
* **Libraries:** `Scikit-learn`, `Pandas`, `NumPy`
* **Environment:** `Jupyter Notebook`

## ⚙️ Workflow & Models

The project followed a structured machine learning workflow:

1.  **Data Loading & Splitting:** The Wine dataset was loaded from `sklearn.datasets`, and then split into training (80%) and testing (20%) sets.
2.  **Feature Scaling:** The features were standardized using `StandardScaler` to ensure all features have a mean of 0 and a standard deviation of 1.

3.  **Model 1: Support Vector Machine (SVM)**
    * A baseline SVM with a linear kernel was trained and evaluated, achieving a test accuracy of **97.2%**.
    * **GridSearchCV** was then used to find the optimal hyperparameters for the SVM, searching through different values for `C`, `kernel`, and `gamma`. The best combination achieved a cross-validation accuracy of **97.9%**.

    ```python
    # GridSearchCV for SVM hyperparameter tuning
    param_grid = {
        'C': [0.1, 1, 10, 100],
        'kernel': ['linear', 'rbf', 'poly'],
        'gamma': ['scale', 'auto']
    }

    grid = GridSearchCV(SVC(), param_grid, cv=3, scoring='accuracy')
    grid.fit(X_train_scaled, y_train)
    ```

4.  **Model 2: Random Forest Classifier**
    * To demonstrate a different tuning strategy, **RandomizedSearchCV** was applied to a Random Forest model. This method is computationally cheaper than a full grid search.
    * The best parameters found through the randomized search yielded a cross-validation accuracy of **98.6%**.

5.  **Model 3: Logistic Regression**
    * A Logistic Regression model was trained on the scaled data as a final comparison point.
    * This model performed exceptionally well on the test set, achieving a perfect accuracy of **100%**.

## 📊 Results Summary

The performance of the tuned models and the baseline were compared to select the best approach for this dataset.

| Model                                            | CV Accuracy (on Training Set) | Test Set Accuracy |
| ------------------------------------------------ | ----------------------------- | ----------------- |
| Baseline SVM                                     | -                             | 97.2%             |
| SVM (tuned with GridSearchCV)                    | 97.9%                         | -                 |
| Random Forest (tuned with RandomizedSearchCV)    | 98.6%                         | -                 |
| **Logistic Regression** | -                             | **100%** |

*(Note: Test set accuracy was not explicitly calculated for the tuned models in the notebook, but CV accuracy is a strong indicator of performance.)*

## 💡 Conclusion

While all models performed extremely well, the **Logistic Regression** model achieved a perfect score on the test data, making it the top performer for this particular dataset and train/test split. This project highlights that while complex models like SVM and Random Forest are powerful, simpler models like Logistic Regression can sometimes be highly effective, especially on well-structured datasets. It also effectively demonstrates two key methods for hyperparameter optimization: `GridSearchCV` and `RandomizedSearchCV`.
