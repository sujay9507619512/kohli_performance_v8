import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Virat_Kohli.csv.xls")

print(df.head())

# total no of runs kohli has scored
print("total runs: ", df["Runs"].sum())
# find out the total no balls he  has faced
print("total balls faced:", df["BF"].sum())
# find out the average strike rate of kohli
print("average strike rate:", df["SR"].mean())

# no. of matches he has played at diffrent positions
print(df["Pos"].head(10))

positions = df["Pos"].unique()
print(positions)

df["Pos"] = df["Pos"].map({
    3.0: "batting at 3",
    4.0: "batting at 4",
    2.0: "batting at 2",
    1.0: "batting at 1",
    7.0: "batting at 7",
    5.0: "batting at 5",
    6.0:  "batting at 6"
})
print(df[{"Runs", "Pos"}])

pos_counts = df["Pos"].value_counts()
print(pos_counts)
print(type(pos_counts))


# no. of runs he has played at diffrent positions


# total runs in scored in diffrent positions
pos_counts_values = pos_counts.values
pos_counts_labels = pos_counts.index

fig = plt.figure(figsize=(10, 7))
plt.pie(pos_counts_values, labels=pos_counts_labels)
# plt.show()


# total match  played on different grounds
def show_pie_plots(df, key):
    counts = df[key].value_counts()
    print(counts)
    counts_values = counts.values
    counts_labels = counts.index
    fig = plt.figure(figsize=(10, 7))
    plt.pie(counts_values, labels=counts_labels)
    # plt.show()


# no of matches he has played with different Oppositions
show_pie_plots(df, "Opposition")

# no of matches he has played  at Grounds

show_pie_plots(df, "Ground")


# Total sixes  scored in different positions
runs_at_pos = df.groupby("Pos")["6s"].sum()
print(runs_at_pos, type(runs_at_pos))
runs_at_pos_values = runs_at_pos.values
runs_at_pos_labels = runs_at_pos.index

fig = plt.figure(figsize=(10, 7))
plt.bar(
    runs_at_pos_labels,
    runs_at_pos_values,
    color = "green",
    width = 0.3
    )
# plt.show()

# Total runs scored with different countries
runs_with_countries = df.groupby("Runs")["Opposition"].sum()
print(runs_with_countries, type(runs_with_countries))
runs_with_countries_values = runs_with_countries.values
runs_with_countries_labels = runs_with_countries.index

fig = plt.figure(figsize=(10, 7))
plt.bar(
    runs_with_countries_labels,
    runs_with_countries_values,
    color = "blue",
    width = 0.3
    )
plt.show()


# no. of century scored  by him in 1st and 2nd inning
centuries = df.query("Runs >= 100")
print(centuries)

innings = centuries["Inns"].value_counts()
plt.pie(innings.values, labels = innings.index)
plt.show()
# tons = centuries["Runs"]


# plt.bar(innings, width = 0.3)
# plt.show()



# total runs scored in diffrent position
print(df["Runs"].sum())

# total balls faced in diffrent position
print(df["BF"].sum())

# total runs scored in different position
print(df["Runs"].sum())
print(df["BF"].sum())
print(df["SR"].mean())
print(df["Pos"].unique())
print(df["Pos"].value_counts())


# no. of century scored  by him in 1st and 2nd inning


print(df.loc[df["Runs"] == 6, "BF"].sum())
print(df.loc[df["Runs"] == 12, "BF"].sum())

# calculate the dismissals of kohli
df["Dismissals"] = df["BF"] - df["SR"]
print(df["Dismissals"].sum())

# find out the average dismissal rate of kohli
print("average dismissal rate:", df["Dismissals"].mean())
