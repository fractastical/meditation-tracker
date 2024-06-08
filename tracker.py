import matplotlib.pyplot as plt

def plot_meditation(days, target_time_per_day, actual_times, total_time, negative_elements, negative_times):
    fig, ax = plt.subplots(figsize=(10, days + 5))
    
    # Plotting the daily meditation times
    for i in range(days):
        ax.add_patch(plt.Rectangle((0, i + 1), target_time_per_day, 0.8, color='gray', alpha=0.3))
        ax.add_patch(plt.Rectangle((0, i + 1), actual_times[i], 0.8, color='blue', alpha=0.6))
    
    # Plotting the total meditation time rectangle
    ax.add_patch(plt.Rectangle((0, 0), total_time, 0.8, color='green', alpha=0.6))
    
    # Plotting the negative elements
    for i in range(len(negative_times)):
        ax.add_patch(plt.Rectangle((i * 1.5, -1), 1, 1, color='black'))
        ax.text(i * 1.5 + 0.5, -1.5, f'{negative_times[i]} min', ha='center', color='white', fontsize=10)
    
    # Setting the labels and titles
    ax.set_xlim(0, max(target_time_per_day, max(actual_times), total_time) + 1)
    ax.set_ylim(-3, days + 2)
    ax.set_xlabel('Time (minutes)')
    ax.set_ylabel('Days')
    ax.set_title('Meditation Times')
    
    plt.show()

# Example usage
days = 7
target_time_per_day = 60  # in minutes
actual_times = [50, 30, 45, 60, 55, 20, 25]  # actual meditation times for each day
total_time = sum(actual_times)
negative_elements = 2  # number of times you engaged in negative elements
negative_times = [10, 15]  # time in minutes for each negative element

plot_meditation(days, target_time_per_day, actual_times, total_time, negative_elements, negative_times)
