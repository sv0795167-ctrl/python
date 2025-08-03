import pandas as pd

# Lists to hold data
titles, views, likes, comments, upload_dates, durations = [], [], [], [], [], []

n = int(input("How many videos do you want to enter? "))

for i in range(n):
    print(f"\nEnter data for video {i+1}:")
    try:
        title = input("Video Title: ")
        view = int(input("Views: "))
        like = int(input("Likes: "))
        comment = int(input("Comments: "))
        upload_date = input("Upload Date (YYYY-MM-DD): ")
        
        duration_str = input("Duration (MM:SS): ")
        mins, secs = map(int, duration_str.strip().split(":"))
        duration_float = round(mins + secs / 60, 2)

        # Append only after all inputs are successfully parsed
        titles.append(title)
        views.append(view)
        likes.append(like)
        comments.append(comment)
        upload_dates.append(upload_date)
        durations.append(duration_float)

    except Exception as e:
        print(f"⚠️ Error in input: {e}")
        print("⏩ Skipping this video entry. Try again if needed.")

# Create DataFrame (only if lengths match)
if len({len(titles), len(views), len(likes), len(comments), len(upload_dates), len(durations)}) == 1:
    data = {
        "Video_Title": titles,
        "Views": views,
        "Likes": likes,
        "Comments": comments,
        "Upload_Date": upload_dates,
        "Duration_minutes": durations
    }

    df = pd.DataFrame(data)
    filename = input("\nEnter file name to save (e.g. my_channel_data.csv): ")
    df.to_csv(filename, index=False)
    print(f"\n✅ CSV file '{filename}' has been created successfully!")
else:
    print("\n❌ Data lists are not of the same length. File not saved.")
