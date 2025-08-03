import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('youtube_data_shubham.csv')
print(df.head())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('youtube_data_shubham.csv')

# ------------------- 1. Basic Exploration -------------------
print("📄 First 5 Rows:")
print(df.head())

print("\n📊 Summary Statistics:")
print(df.describe())

print("\n🧠 Column Names:", df.columns.tolist())

# ------------------- 2. Correlation Matrix -------------------
plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="Blues", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# ------------------- 3. Views vs Likes Scatter Plot -------------------
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Views", y="Likes", hue="Video_Title", s=100)
plt.title("Views vs Likes")
plt.tight_layout()
plt.show()

# ------------------- 4. Views per Video (Bar Chart) -------------------
plt.figure(figsize=(10, 6))
sns.barplot(data=df, y="Video_Title", x="Views", palette="coolwarm")
plt.title("Total Views per Video")
plt.xlabel("Views")
plt.ylabel("Video Title")
plt.tight_layout()
plt.show()

# ------------------- 5. Likes to Views Ratio -------------------
df["Like_View_Ratio"] = df["Likes"] / df["Views"]
print("\n👍 Likes to Views Ratio:")
print(df[["Video_Title", "Like_View_Ratio"]])

# ------------------- 6. Longest and Most Viewed Videos -------------------
most_viewed = df.loc[df['Views'].idxmax()]
longest_video = df.loc[df['Duration_minutes'].idxmax()]
print(f"\n🔥 Most Viewed Video: {most_viewed['Video_Title']} ({most_viewed['Views']} views)")
print(f"⏱️ Longest Video: {longest_video['Video_Title']} ({longest_video['Duration_minutes']} mins)")
