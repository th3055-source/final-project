import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from theme import apply_theme

apply_theme()
st.title("⚙️ Hyperparameter Tuning")

st.write("""
This page shows how different Random Forest parameters affect model performance.
Grid Search is used to automatically find the best combination.
""")

# Load data
df = pd.read_csv("insurance.csv")

# Encode categorical variables
df = pd.get_dummies(df, drop_first=True)

X = df.drop("charges", axis=1)
y = df["charges"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Parameters to test
param_grid = {
    "n_estimators":[50,100],
    "max_depth":[5,10,None]
}

grid = GridSearchCV(
    RandomForestRegressor(random_state=42),
    param_grid,
    cv=3,
    scoring="r2"
)

grid.fit(X_train,y_train)

best_model = grid.best_estimator_

prediction = best_model.predict(X_test)

score = r2_score(y_test,prediction)

st.subheader("Best Parameters")

st.success(grid.best_params_)

st.subheader("Best R² Score")

st.metric("R²",f"{score:.3f}")

results = pd.DataFrame(grid.cv_results_)

st.subheader("Grid Search Results")

st.dataframe(
    results[
        [
            "param_n_estimators",
            "param_max_depth",
            "mean_test_score"
        ]
    ]
)