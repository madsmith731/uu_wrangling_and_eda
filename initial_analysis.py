import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#1
df = pd.read_csv ('./lab_1/ForeignGifts_edu.csv')
df.head()

#2
print(df["Gift Type"].unique())

#3.1
df.groupby("Country of Giftor").sum("Foreign Gift Amount").sort_values(by="Foreign Gift Amount", ascending=False).head(1)

#3.2
df["Country of Giftor"].value_counts()

#3.3
df.groupby("Country of Giftor").mean("Foreign Gift Amount").sort_values(by="Foreign Gift Amount", ascending=False).head(1)

#3.4
df_institution_giftamount = df.groupby("Institution Name").sum("Foreign Gift Amount").sort_values(by="Foreign Gift Amount", ascending=False).head(20)

sns.barplot(data = df_institution_giftamount, x="Institution Name", y = "Foreign Gift Amount")
plt.xticks(rotation=90)
plt.show()

#3.5
df_institution_count = df["Institution Name"].value_counts().reset_index(name='Counts').head(20)
sns.barplot(data = df_institution_count, x="Institution Name", y = "Counts")
plt.xticks(rotation=90)
plt.show()

#3.6 THIS IS NOT DONE
df_institution_giftamount2 = df.groupby("Institution Name").sum("Foreign Gift Amount")
sns.histplot(data = df_institution_giftamount2, x = "Foreign Gift Amount")

#3.7
pd.crosstab(df["Institution Name"], df["Country of Giftor"]).stack().reset_index(name = 'Cross').sort_values(by = "Cross", ascending = False).head(1)

#3.8
import pandas as pd
import plotly.graph_objects as go

#giftor = 'Giftor Name'
giftor = 'Country of Giftor'
recipi = 'Institution Name'
flow = 'Foreign Gift Amount'
N = 25

flows = (
    df.groupby([giftor, 
                recipi])
      [flow]
      .sum()
      .nlargest(N)
      .reset_index()
)

labels = (
    flows[giftor].tolist()
    + flows[recipi].tolist()
)

labels = list(dict.fromkeys(labels))

fig = go.Figure(
    go.Sankey(
        node=dict(label=labels),
        link=dict(
            source=flows[giftor]
                        .map(labels.index),
            target=flows[recipi]
                        .map(labels.index),
            value=flows[flow]
        )
    )
)

fig.show()