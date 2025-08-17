import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

def create_restaurant_review_dataset():
    """Creates a sample DataFrame simulating a restaurant review dataset."""
    data = {
        'timestamp': pd.to_datetime([
            '2025-08-01', '2025-08-01', '2025-08-01',
            '2025-08-02', '2025-08-02',
            '2025-08-03', '2025-08-03', '2025-08-03', '2025-08-03',
            '2025-08-04', '2025-08-04',
            '2025-08-05', '2025-08-05', '2025-08-05',
            '2025-08-06',
            '2025-08-07', '2025-08-07'
        ]),
        'review_text': [
            "Amazing food!", "Service was slow.", "It was okay.",
            "Loved the ambiance.", "My soup was cold.",
            "Perfect experience!", "Great value for money.", "The waiter was rude.", "Will come back!",
            "Best noodles ever.", "Not worth the price.",
            "A fantastic dinner.", "The place was too noisy.", "Average, nothing special.",
            "Could be better.",
            "Absolutely wonderful!", "The dessert was terrible."
        ],
        'sentiment': [
            'positive', 'negative', 'neutral',
            'positive', 'negative',
            'positive', 'positive', 'negative', 'positive',
            'positive', 'negative',
            'positive', 'negative', 'neutral',
            'negative',
            'positive', 'negative'
        ]
    }
    df = pd.DataFrame(data)
    return df

def plot_sentiment_trends(df: pd.DataFrame, start_date: str, end_date: str):
    """
    Generates and saves a bar plot of sentiment trends for a given date range.
    
    Args:
        df: The DataFrame containing review data.
        start_date: The start of the date range (e.g., '2025-08-01').
        end_date: The end of the date range (e.g., '2025-08-07').
    """
    
    mask = (df['timestamp'] >= start_date) & (df['timestamp'] <= end_date)
    filtered_df = df[mask].copy()
    
    if filtered_df.empty:
        print(f"No data available for the selected date range: {start_date} to {end_date}")
        return

    # Aggregate the data
    sentiment_counts = filtered_df.groupby([filtered_df['timestamp'].dt.date, 'sentiment']).size().unstack(fill_value=0)
    
    # Plotting
    sentiment_counts.plot(kind='bar', stacked=False, figsize=(12, 7),
                          color=sns.color_palette("viridis", 3))
    
    plt.title(f'Sentiment Trends from {start_date} to {end_date}', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Number of Reviews', fontsize=12)
    plt.xticks(rotation=45)
    plt.legend(title='Sentiment')
    plt.tight_layout()
    
    
    output_filename = f"sentiment_plot_{start_date}_to_{end_date}.png"
    plt.savefig(output_filename)
    print(f"\nPlot saved as '{output_filename}'")
    plt.show()


print("\n--- Sentiment Visualization Agent Demo ---")


review_df = create_restaurant_review_dataset()


start_day = "2025-08-01"
end_day = "2025-08-07"
plot_sentiment_trends(review_df, start_day, end_day)
