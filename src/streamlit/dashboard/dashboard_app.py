import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the Excel file
file_path = 'testdata.xlsx'
data = pd.read_excel(file_path)

# Convert Intimes and Outtimes to datetime
data['Intimes'] = pd.to_datetime(data['Date'] + ' ' + data['Intimes'], format='%d-%m-%Y %H:%M')
data['Outtimes'] = pd.to_datetime(data['Date'] + ' ' + data['Outtimes'], format='%d-%m-%Y %H:%M')

# Function to plot the distribution of in-time and out-time
# Function to plot the distribution of in-time and out-time and identify peak hours
def plot_in_out_distribution(data):
    plt.figure(figsize=(12, 6))
    in_time_hours = data['Intimes'].dt.hour
    out_time_hours = data['Outtimes'].dt.hour
    
    sns.histplot(in_time_hours, bins=24, kde=False, color='blue', label='In-time')
    sns.histplot(out_time_hours, bins=24, kde=False, color='red', label='Out-time')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Vehicles')
    plt.title('Vehicle In-time and Out-time Distribution')
    plt.legend()
    st.pyplot(plt.gcf())
    
    peak_in_hour = in_time_hours.value_counts().idxmax()
    peak_out_hour = out_time_hours.value_counts().idxmax()
    st.write(f"Peak In-time Hour: {peak_in_hour}:00 - Indicates when the parking lot is busiest in terms of entries.")
    st.write(f"Peak Out-time Hour: {peak_out_hour}:00 - Suggests the most frequent time for vehicles leaving the lot.")

# Function to plot the number of vehicles per date and identify the peak date
def plot_vehicles_per_date(data):
    vehicle_count_per_date = data.groupby('Date').size().reset_index(name='Vehicle Count')
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Date', y='Vehicle Count', data=vehicle_count_per_date, palette='magma')
    plt.xlabel('Date')
    plt.ylabel('Number of Vehicles')
    plt.title('Number of Vehicles Per Date')
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())

    peak_date = vehicle_count_per_date.loc[vehicle_count_per_date['Vehicle Count'].idxmax(), 'Date']
    st.write(f"Date with Maximum Vehicles: {peak_date} - Highlights a day with significantly higher parking demand.")

# Function to plot parking occupancy over time and identify peak occupancy hour
def plot_parking_occupancy(data):
    time_range = pd.date_range(start=data['Intimes'].min(), end=data['Outtimes'].max(), freq='H')
    occupancy = pd.DataFrame(index=time_range, columns=['Occupancy'])
    occupancy['Occupancy'] = 0
    for _, row in data.iterrows():
        occupancy.loc[row['Intimes']:row['Outtimes'], 'Occupancy'] += 1
    plt.figure(figsize=(12, 6))
    plt.plot(occupancy.index, occupancy['Occupancy'], label='Occupancy')
    plt.fill_between(occupancy.index, occupancy['Occupancy'], alpha=0.4)
    plt.xlabel('Time')
    plt.ylabel('Number of Vehicles')
    plt.title('Parking Occupancy Over Time')
    plt.legend()
    st.pyplot(plt.gcf())

    peak_occupancy_hour = occupancy['Occupancy'].idxmax().hour
    st.write(f"Peak Parking Occupancy Hour: {peak_occupancy_hour}:00 - Represents the hour with the highest parking demand.")
    
# Function to plot the number of different types of vehicles per date and identify the most common vehicle type
def plot_vehicles_by_type(data):
    vehicle_type_count = data.groupby(['Date', 'Vehicle Name']).size().reset_index(name='Vehicle Count')
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='Vehicle Count', hue='Vehicle Name', data=vehicle_type_count)
    plt.xlabel('Date')
    plt.ylabel('Number of Vehicles')
    plt.title('Number of Different Types of Vehicles Per Date')
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())

    most_common_vehicle = vehicle_type_count.loc[vehicle_type_count['Vehicle Count'].idxmax(), 'Vehicle Name']
    st.write(f"Most Common Vehicle Type: {most_common_vehicle} - Indicates the preferred type of vehicle among users.")

# Function to plot authorized vehicles (sumo and bus)
# Function to plot authorized and unauthorized vehicles activity per date
def plot_authorized_unauthorized_vehicles(data):
    # Count authorized vehicles
    authorized_vehicles = data[data['Vehicle Name'].isin(['sumo', 'bus'])]
    authorized_count_per_date = authorized_vehicles.groupby('Date').size().reset_index(name='Authorized Vehicle Count')

    # Count unauthorized vehicles
    unauthorized_vehicles = data[~data['Vehicle Name'].isin(['sumo', 'bus'])]
    unauthorized_count_per_date = unauthorized_vehicles.groupby('Date').size().reset_index(name='Unauthorized Vehicle Count')

    # Merge counts into a single DataFrame
    combined_counts = pd.merge(authorized_count_per_date, unauthorized_count_per_date, on='Date', how='outer').fillna(0)

    # Plotting the results
    plt.figure(figsize=(12, 6))
    combined_counts.set_index('Date').plot(kind='bar', stacked=False, color=['blue', 'orange'], ax=plt.gca())
    plt.xlabel('Date')
    plt.ylabel('Number of Vehicles')
    plt.title('Authorized vs Unauthorized Vehicles Per Date')
    plt.xticks(rotation=45)
    plt.legend(['Authorized Vehicles', 'Unauthorized Vehicles'])
    st.pyplot(plt.gcf())

    # Identify peak dates for both types of vehicles
    peak_authorized_date = combined_counts.loc[combined_counts['Authorized Vehicle Count'].idxmax(), 'Date']
    peak_unauthorized_date = combined_counts.loc[combined_counts['Unauthorized Vehicle Count'].idxmax(), 'Date']
    
    st.write(f"Date with Maximum Authorized Vehicles: {peak_authorized_date}")
    st.write(f"Date with Maximum Unauthorized Vehicles: {peak_unauthorized_date}")


data['DayOfWeek'] = data['Intimes'].dt.day_name()
def plot_busiest_days(data):
    busiest_days = data['DayOfWeek'].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(x=busiest_days.index, y=busiest_days.values, palette='rocket')
    plt.xlabel('Day of the Week')
    plt.ylabel('Number of Vehicles')
    plt.title('Busiest Days of the Week')
    st.pyplot(plt.gcf())

    busiest_day = busiest_days.idxmax()
    st.write(f"Busiest Day of the Week: {busiest_day} - This is the day with the highest parking activity.")



st.set_page_config(layout="wide")
# Streamlit dashboard
st.title('Vehicle Management System Dashboard')

# Create a 3x2 layout for the dashboard
cols = st.columns(3)

# Row 1
with cols[0]:
    st.subheader('In-time and Out-time Distribution')
    plot_in_out_distribution(data)

with cols[1]:
    st.subheader('Number of Vehicles Per Date')
    plot_vehicles_per_date(data)

with cols[2]:
    st.subheader('Parking Occupancy Over Time')
    plot_parking_occupancy(data)

# Row 2
cols = st.columns(3)

with cols[0]:
    st.subheader('Vehicles by Type')
    plot_vehicles_by_type(data)

with cols[1]:
    st.subheader('Authorized vs Unauthorized Vehicles')
    plot_authorized_unauthorized_vehicles(data)

with cols[2]:
    st.subheader('Busiest Day of the week')
    plot_busiest_days(data)