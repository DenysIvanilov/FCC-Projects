import pandas as pd

df = pd.read_csv("adult.data.csv")

race_count = df["race"].value_counts()

average_age_men = round(df[df["sex"] == "Male"].age.mean(), 2)

percentage_bachelors = round(df.education.value_counts(normalize=True).Bachelors * 100, 2)

higher_education = ((df["education"] == "Bachelors")
                    | (df["education"] == "Doctorate")
                    | (df["education"] == "Masters"))
lower_education = ~higher_education
higher_education_rich = round(df[higher_education].salary.value_counts(normalize=True)[">50K"] * 100, 2)
lower_education_rich = round(df[lower_education].salary.value_counts(normalize=True)[">50K"] * 100, 2)

min_work_hours = df["hours-per-week"].min()

num_min_workers = df[df["hours-per-week"] == min_work_hours]
rich_percentage = round(num_min_workers.salary.value_counts(normalize=True)[">50K"] * 100, 2)

highest_earning_country = (df.groupby("native-country")["salary"].value_counts(normalize=True)
                           [:, ">50K"].sort_values(ascending=False).index[0])
highest_earning_country_percentage = (round(df.groupby("native-country")["salary"].value_counts(normalize=True)
                                            [:, ">50K"].sort_values(ascending=False)[0] * 100, 2))

top_IN_occupation = (df[df["native-country"] == "India"].groupby("salary")["occupation"].value_counts()[">50K"]
                     .sort_values(ascending=False).index[0])

