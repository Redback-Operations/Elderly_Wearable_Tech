import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# 1. Generate mock mental health trends data
def generate_dashboard_data():
    np.random.seed(42)
    years = np.arange(2015, 2026)
    states = ['NSW', 'VIC', 'QLD', 'WA', 'SA', 'TAS']
    age_groups = ['18-29', '30-44', '45-59', '60+']
    activity_levels = ['Low', 'Medium', 'High']

    # Create a cartesian product of all categories and years
    records = []
    for year in years:
        for state in states:
            for age in age_groups:
                for activity in activity_levels:
                    # Simulate average distress score (10-50 scale)
                    base = 30 - (0.5 * activity_levels.index(activity))  # more activity lowers distress
                    age_adj = 0.1 * age_groups.index(age)  # older groups slightly higher distress
                    trend = (year - 2015) * 0.2  # slight upward trend
                    score = base + age_adj + trend + np.random.normal(0, 1)
                    records.append({
                        'Year': year,
                        'State': state,
                        'AgeGroup': age,
                        'ActivityLevel': activity,
                        'AvgDistressScore': round(score, 1)
                    })

    df = pd.DataFrame(records)
    return df

# 2. Plotting function for displaying graphs
def plot_trends_by_state(df):
    states = df['State'].unique()
    plt.figure(figsize=(8, 5))
    for state in states:
        subset = df[df['State'] == state].groupby('Year')['AvgDistressScore'].mean()
        plt.plot(subset.index, subset.values, label=state)
    plt.title('Avg Distress Score by State (2015–2025)')
    plt.xlabel('Year')
    plt.ylabel('Average Distress Score')
    plt.legend()
    plt.tight_layout()
    st.pyplot(plt)

def plot_trends_by_age_group(df):
    age_groups = df['AgeGroup'].unique()
    plt.figure(figsize=(8, 5))
    for age in age_groups:
        subset = df[df['AgeGroup'] == age].groupby('Year')['AvgDistressScore'].mean()
        plt.plot(subset.index, subset.values, label=age)
    plt.title('Avg Distress Score by Age Group (2015–2025)')
    plt.xlabel('Year')
    plt.ylabel('Average Distress Score')
    plt.legend()
    plt.tight_layout()
    st.pyplot(plt)

def plot_activity_level_bar_chart(df):
    latest = df[df['Year'] == df['Year'].max()]
    activity_avg = latest.groupby('ActivityLevel')['AvgDistressScore'].mean()
    plt.figure(figsize=(6, 4))
    activity_avg.plot(kind='bar')
    plt.title(f'Avg Distress by Activity Level in {df["Year"].max()}')
    plt.xlabel('Activity Level')
    plt.ylabel('Average Distress Score')
    plt.tight_layout()
    st.pyplot(plt)

# 3. Display the data and plots in Streamlit
def run_dashboard():
    st.title("Dashboard: Mental Health Trends")
    
    df = generate_dashboard_data()

    # Show sample data
    st.write("### Sample of Generated Data")
    st.write(df.head(10))

    # Display the graphs
    st.write("### Trends by State")
    plot_trends_by_state(df)

    st.write("### Trends by Age Group")
    plot_trends_by_age_group(df)

    st.write("### Distress by Activity Level")
    plot_activity_level_bar_chart(df)

    # Sample pandas filtering & grouping logic
    st.write("### NSW Average Distress by Year")
    nsw_avg = df[df['State']=='NSW'].groupby('Year')['AvgDistressScore'].mean()
    st.write(nsw_avg)

    st.write("### 18-29 Age Group with High Activity")
    young_high = df[(df['AgeGroup']=='18-29') & (df['ActivityLevel']=='High')]
    st.write(young_high.head())
