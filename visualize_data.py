import matplotlib.pyplot as plt

def visualize_data(df):
    # Sample visualization (modify as needed)
    df.plot(kind='bar', x='Bank name', y='Market cap(US$ billion)')
    plt.show()
