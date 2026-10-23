import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Stock Risk Prediction", page_icon="📦")

@st.cache_resource
def load_model():
    return joblib.load("stock_risk_prediction_model.pkl")

model = load_model()

st.title("Inventory Stock-Risk Prediction")
st.write("Enter inventory details to predict stock risk.")

with st.form("stock_form"):
    current_stock = st.number_input("Current Stock", min_value=0.0, value=100.0)
    avg_daily_demand = st.number_input("Average Daily Demand", min_value=0.0, value=10.0)
    lead_time_days = st.number_input("Lead Time (Days)", min_value=0.0, value=5.0)
    reorder_point = st.number_input("Reorder Point", min_value=0.0, value=50.0)
    sales_last_30_days = st.number_input("Sales in Last 30 Days", min_value=0.0, value=300.0)
    stock_turnover_ratio = st.number_input("Stock Turnover Ratio", min_value=0.0, value=2.0)
    forecast_error = st.number_input("Forecast Error", value=0.0)

    season = st.selectbox(
        "Season", ["Winter", "Spring", "Summer", "Autumn"]
    )
    item_category = st.selectbox(
        "Item Category", ["Electronics", "Clothing", "Food", "Home"]
    )
    supplier_reliability = st.slider(
        "Supplier Reliability", 0.0, 1.0, 0.9
    )

    submitted = st.form_submit_button("Predict Stock Risk")

if submitted:
    input_data = pd.DataFrame([{
        "current_stock": current_stock,
        "avg_daily_demand": avg_daily_demand,
        "lead_time_days": lead_time_days,
        "reorder_point": reorder_point,
        "sales_last_30_days": sales_last_30_days,
        "stock_turnover_ratio": stock_turnover_ratio,
        "forecast_error": forecast_error,
        "season": season,
        "item_category": item_category,
        "supplier_reliability": supplier_reliability
    }])

    try:
        prediction = model.predict(input_data)[0]
        st.success(f"Predicted Stock Risk: {prediction}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")