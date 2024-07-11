import matplotlib.pyplot as plt
from logging_util import log_message

import matplotlib.pyplot as plt
from logging_util import log_message

def visualize_data(df):
    if df is None or df.empty:
        print("No data available for visualization.")
        return

    try:
        df = df.sort_values(by='Market cap (Germany)', ascending=False).head(20)
        
        plt.figure(figsize=(12, 8))
        plt.barh(df['Bank name'], df['Market cap (Germany)'])
        plt.title('Market Cap of Top 20 Largest Banks in Germany in 2022')
        plt.xlabel('Market Cap (US$ billion)')
        plt.ylabel('Bank Name')
        plt.tight_layout()
        plt.gca().invert_yaxis()
        plt.show()
        
    except KeyError as e:
        print(f"Column not found: {e}")
        log_message('ERROR', f"Column not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        log_message('ERROR', f"An unexpected error occurred: {e}")
