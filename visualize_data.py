import matplotlib.pyplot as plt
from logging_util import log_message

def visualize_data(df):
    if df is None or df.empty:
        print("No data available for visualization.")
        return

    try:
        # Sort the DataFrame by 'Total assets (2022) (US$ billion)' in descending order and take the top 20 for clarity
        df = df.sort_values(by='Total assets (2022) (US$ billion)', ascending=False).head(20)
        
        plt.figure(figsize=(12, 8))
        plt.barh(df['Bank name'], df['Total assets (2022) (US$ billion)'])
        plt.title('Total Assets of Top 20 Largest Banks in 2022')
        plt.xlabel('Total Assets (US$ billion)')
        plt.ylabel('Bank Name')
        plt.tight_layout()
        plt.legend(['Total assets (2022) (US$ billion)'], loc='best')
        plt.gca().invert_yaxis()  # Invert y-axis to have the largest bank on top
        plt.show()
        
    except KeyError as e:
        print(f"Column not found: {e}")
        log_message('ERROR', f"Column not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        log_message('ERROR', f"An unexpected error occurred: {e}")
