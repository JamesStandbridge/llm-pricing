import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def calculate_cost(
    model_prices, num_users, num_requests_per_month, avg_tokens_input, avg_tokens_output
):
    price_1k_tokens_input, price_1k_tokens_output = model_prices
    input_cost_daily = (
        ((price_1k_tokens_input / 1000) * avg_tokens_input)
        * (num_requests_per_month / 30)
        * num_users
    )
    output_cost_daily = (
        ((price_1k_tokens_output / 1000) * avg_tokens_output)
        * (num_requests_per_month / 30)
        * num_users
    )
    total_monthly_cost = (input_cost_daily + output_cost_daily) * 30
    cost_per_user_per_month = total_monthly_cost / num_users

    return (
        total_monthly_cost,
        input_cost_daily * 30,
        output_cost_daily * 30,
        cost_per_user_per_month,
    )


st.title("LLM API Cost Analysis")


model_prices = {
    "Mistral AI": (0.0027, 0.024),
    "OpenAPI GPT4": (0.03, 0.06),
    "OpenAPI GPT3.5-turbo": (0.00050, 0.00150),
    "Claude3 Haiku": (0.25 / 1000, 1.25 / 1000),
    "Claude3 Sonnet": (3 / 1000, 15 / 1000),
    "Claude3 Opus": (15 / 1000, 75 / 1000),
}

avg_tokens_input = st.number_input(
    "Average tokens used in input", min_value=10, max_value=10000, value=500, step=100
)
avg_tokens_output = st.number_input(
    "Average tokens used in output", min_value=10, max_value=10000, value=200, step=100
)
num_users = st.slider("Number of users", 100, 20000, 2000)
num_requests_per_month = st.slider(
    "Number of requests per month per user", 30, 1000, 150
)

model_comparison_data = []
for m in model_prices:
    total_cost, _, _, cost_per_user = calculate_cost(
        model_prices[m],
        num_users,
        num_requests_per_month,
        avg_tokens_input,
        avg_tokens_output,
    )
    model_comparison_data.append(
        {
            "Model": m,
            "Estimated Monthly Cost": total_cost,
            "Cost per User per Month": cost_per_user,
        }
    )

model_comparison_df = pd.DataFrame(model_comparison_data)
fig_comparison = px.bar(
    model_comparison_df,
    x="Model",
    y=["Estimated Monthly Cost", "Cost per User per Month"],
    title="Model Cost Comparison",
    color="Model",
    barmode="group",
)
st.plotly_chart(fig_comparison)

evolution_data = []
user_range = range(100, 20001, 1900)
for m in model_prices:
    for num_u in user_range:
        total_cost, _, _, cost_per_user = calculate_cost(
            model_prices[m],
            num_u,
            num_requests_per_month,
            avg_tokens_input,
            avg_tokens_output,
        )
        evolution_data.append(
            {
                "Model": m,
                "Number of users": num_u,
                "Monthly cost": total_cost,
                "Cost per User per Month": cost_per_user,
            }
        )

evolution_df = pd.DataFrame(evolution_data)
fig_evolution = px.line(
    evolution_df,
    x="Number of users",
    y=["Monthly cost", "Cost per User per Month"],
    color="Model",
    title="Evolution of Cost with Number of Users for All Models",
    markers=True,
)
st.plotly_chart(fig_evolution)


model = st.selectbox(
    "Select a model",
    (
        "Mistral AI",
        "OpenAPI GPT4",
        "OpenAPI GPT3.5-turbo",
        "Claude3 Haiku",
        "Claude3 Sonnet",
        "Claude3 Opus",
    ),
)

total_cost, input_cost, output_cost, cost_per_user_per_month = calculate_cost(
    model_prices[model],
    num_users,
    num_requests_per_month,
    avg_tokens_input,
    avg_tokens_output,
)
st.metric(
    label=f"Estimated monthly cost for {model}",
    value=f"${total_cost:,.2f}".replace(",", " "),
)
st.metric(
    label=f"Cost per user per month for {model}",
    value=f"${cost_per_user_per_month:,.2f}".replace(",", " "),
)

cost_data = {
    "Cost Type": ["Input Tokens", "Output Tokens"],
    "Amount": [input_cost, output_cost],
}
cost_df = pd.DataFrame(cost_data)
fig_pie = px.pie(
    cost_df, values="Amount", names="Cost Type", title="Cost Breakdown by Token Type"
)
st.plotly_chart(fig_pie)

hide_menu_style = """<style>.stDeployButton {visibility: hidden;} footer {visibility: hidden;}</style>"""
st.markdown(hide_menu_style, unsafe_allow_html=True)
