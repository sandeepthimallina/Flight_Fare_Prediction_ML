import pandas as pd
import matplotlib.pyplot as plt

# ==================================================
# FLIGHT FARE DATA VISUALIZATION
# ==================================================

print("=" * 50)
print("FLIGHT FARE VISUALIZATION")
print("=" * 50)

# Load dataset
df = pd.read_csv("data/Freshly_cleaned.csv/Freshly_cleaned.csv")

print("\nDataset loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# ==================================================
# 1. AVERAGE FARE BY AIRLINE
# ==================================================

avg_airline_price = (
    df.groupby("airline")["price"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage fare by airline:")
print(avg_airline_price)

plt.figure(figsize=(10, 6))
avg_airline_price.plot(kind="bar")

plt.title("Average Flight Fare by Airline")
plt.xlabel("Airline")
plt.ylabel("Average Fare")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ==================================================
# 2. AVERAGE FARE BY NUMBER OF STOPS
# ==================================================

avg_stops_price = df.groupby("stops")["price"].mean()

print("\nAverage fare by number of stops:")
print(avg_stops_price)

plt.figure(figsize=(8, 5))
avg_stops_price.plot(kind="bar")

plt.title("Average Flight Fare by Number of Stops")
plt.xlabel("Number of Stops")
plt.ylabel("Average Fare")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ==================================================
# 3. AVERAGE FARE BY CLASS
# ==================================================

avg_class_price = df.groupby("class")["price"].mean()

print("\nAverage fare by class:")
print(avg_class_price)

plt.figure(figsize=(8, 5))
avg_class_price.plot(kind="bar")

plt.title("Average Flight Fare by Class")
plt.xlabel("Class")
plt.ylabel("Average Fare")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ==================================================
# 4. TOP 10 ROUTES BY AVERAGE FARE
# ==================================================

avg_route_price = (
    df.groupby("route")["price"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 routes by average fare:")
print(avg_route_price)

plt.figure(figsize=(12, 6))
avg_route_price.plot(kind="bar")

plt.title("Top 10 Routes by Average Flight Fare")
plt.xlabel("Route")
plt.ylabel("Average Fare")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ==================================================
# 5. FLIGHT FARE DISTRIBUTION
# ==================================================

plt.figure(figsize=(10, 6))

plt.hist(
    df["price"],
    bins=50
)

plt.title("Flight Fare Distribution")
plt.xlabel("Flight Fare")
plt.ylabel("Number of Flights")
plt.tight_layout()
plt.show()


# ==================================================
# 6. AVERAGE FARE BY DURATION
# ==================================================

duration_groups = pd.cut(
    df["duration_in_min"],
    bins=[0, 60, 120, 180, 240, 300, 1000],
    labels=[
        "0-60 min",
        "61-120 min",
        "121-180 min",
        "181-240 min",
        "241-300 min",
        "300+ min"
    ]
)

avg_duration_price = df.groupby(
    duration_groups,
    observed=False
)["price"].mean()

print("\nAverage fare by flight duration:")
print(avg_duration_price)

plt.figure(figsize=(10, 6))
avg_duration_price.plot(kind="bar")

plt.title("Average Flight Fare by Duration")
plt.xlabel("Flight Duration")
plt.ylabel("Average Fare")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ==================================================
# COMPLETED
# ==================================================

print("\n" + "=" * 50)
print("ALL VISUALIZATIONS COMPLETED SUCCESSFULLY!")
print("=" * 50)