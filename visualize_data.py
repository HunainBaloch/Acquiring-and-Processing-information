import matplotlib.pyplot as plt

def visualize_data(df):
    df.plot(kind='bar', x='Bank Name', y='Assets (in billion USD)')
    plt.title('Top Banks by Assets')
    plt.xlabel('Bank Name')
    plt.ylabel('Assets (in billion USD)')
    plt.show()
