import streamlit as st
import pandas as pd
import plotly.express as px
import time

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
from theme import apply_theme

apply_theme()

df = pd.read_csv("insurance.csv")
df_encoded = pd.get_dummies(df, drop_first=True)

X = df_encoded.drop("charges", axis=1)
y = df_encoded["charges"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

st.title("⚙️ Hyperparameter Tuning")

st.markdown("""
<div class="card">
This page shows how hyperparameter tuning improves the Random Forest model.
Users can select parameter ranges, run Grid Search, and compare the results.
</div>
""", unsafe_allow_html=True)

st.divider()

st.header("Tuning Settings")

col1, col2, col3 = st.columns(3)

with col1:
    n_estimators_options = st.multiselect(
        "Number of Trees",
        [50, 100, 150, 200],
        default=[50, 100]
    )

with col2:
    max_depth_options = st.multiselect(
        "Max Tree Depth",
        [3, 5, 10, None],
        default=[5, 10, None]
    )

with col3:
    cv_folds = st.slider(
        "Cross Validation Folds",
        3,
        5,
        3
    )

st.markdown("""
<div class="card">
<strong>Explanation:</strong> Grid Search tests different parameter combinations and selects the best one based on R² score.
</div>
""", unsafe_allow_html=True)

run_tuning = st.button("🚀 Run Grid Search")

if run_tuning:
    if len(n_estimators_options) == 0 or len(max_depth_options) == 0:
        st.error("Please select at least one value for each parameter.")
    else:
        st.subheader("Tuning Progress")

        progress_bar = st.progress(0)
        status_text = st.empty()

        total_steps = len(n_estimators_options) * len(max_depth_options)

        for i in range(total_steps):
            progress_bar.progress((i + 1) / total_steps)
            status_text.write(f"Testing parameter combination {i + 1} of {total_steps}...")
            time.sleep(0.25)

        param_grid = {
            "n_estimators": n_estimators_options,
            "max_depth": max_depth_options
        }

        grid_search = GridSearchCV(
            RandomForestRegressor(random_state=42),
            param_grid,
            cv=cv_folds,
            scoring="r2",
            return_train_score=True
        )

        grid_search.fit(X_train, y_train)

        best_model = grid_search.best_estimator_
        y_pred = best_model.predict(X_test)

        best_r2 = r2_score(y_test, y_pred)
        best_mse = mean_squared_error(y_test, y_pred)

        st.success("Grid Search completed successfully!")

        st.divider()

        st.header("Best Model Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
            <div class="small-card">
                <div class="metric-number">{best_r2:.3f}</div>
                <div class="metric-label">Best R² Score</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="small-card">
                <div class="metric-number">{grid_search.best_params_["n_estimators"]}</div>
                <div class="metric-label">Best Trees</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="small-card">
                <div class="metric-number">{grid_search.best_params_["max_depth"]}</div>
                <div class="metric-label">Best Max Depth</div>
            </div>
            """, unsafe_allow_html=True)

        st.divider()

        st.header("Grid Search Results")

        results = pd.DataFrame(grid_search.cv_results_)

        results_table = results[
            ["param_n_estimators", "param_max_depth", "mean_test_score", "rank_test_score"]
        ].sort_values("rank_test_score")

        st.dataframe(results_table, use_container_width=True)

        st.header("Tuning Performance Chart")

        chart_df = results_table.copy()
        chart_df["Combination"] = (
            "trees=" + chart_df["param_n_estimators"].astype(str)
            + ", depth=" + chart_df["param_max_depth"].astype(str)
        )

        fig = px.bar(
            chart_df,
            x="Combination",
            y="mean_test_score",
            title="Grid Search Mean R² Score by Parameter Combination",
            labels={"mean_test_score": "Mean CV R² Score", "Combination": "Parameter Combination"}
        )
        fig.update_layout(height=500, plot_bgcolor="white", paper_bgcolor="white")
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        <div class="card">
        💡 <strong>Tuning Insight:</strong>
        Hyperparameter tuning improves model performance by finding the best Random Forest settings.
        The best model balances complexity and prediction accuracy.
        </div>
        """, unsafe_allow_html=True)

else:
    st.warning("Choose parameter values and click **Run Grid Search** to start tuning.")