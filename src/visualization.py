import os
import matplotlib.pyplot as plt

def plot_prices(data, output_path="output/stock_price_trends.png", show_plot=True):

    plt.figure(figsize=(8,5))

    for col in data.columns[1:]:
        plt.plot(data['Date'], data[col], label=col)

    plt.legend()
    plt.title("Stock Price Trends")
    plt.xlabel("Date")
    plt.ylabel("Price")

    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)

    if show_plot:
        plt.show()
    else:
        plt.close()

    return output_path