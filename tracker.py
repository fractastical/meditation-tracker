import matplotlib.pyplot as plt

def plot_meditation(days, target_time_per_day, daily_sessions, negative_times):
    fig, ax = plt.subplots(figsize=(days + 5, 10))

    # Plotting the daily meditation times
    for i in range(days):
        total_day_time = sum(daily_sessions[i])
        # Plot the target meditation time for the day
        ax.add_patch(plt.Rectangle((i + 1, 0), 0.8, target_time_per_day, color='gray', alpha=0.3))
        # Plot each meditation session for the day
        cumulative_time = 0
        for session_time in daily_sessions[i]:
            ax.add_patch(plt.Rectangle((i + 1, cumulative_time), 0.8, session_time, color='blue', alpha=0.6))
            cumulative_time += session_time
    
    # Plotting the total meditation time rectangle
    total_time = sum(sum(sessions) for sessions in daily_sessions)
    ax.add_patch(plt.Rectangle((0, 0), 0.8, total_time, color='green', alpha=0.6))
    
    # Plotting the negative elements
    for i in range(len(negative_times)):
        ax.add_patch(plt.Rectangle((i * 1.5, -total_time - 5), 1, negative_times[i], color='black'))
        ax.text(i * 1.5 + 0.5, -total_time - 5 - negative_times[i] / 2, f'{negative_times[i]} min', ha='center', color='white', fontsize=10)

    # Setting the labels and titles
    ax.set_xlim(-1, days + 2)
    ax.set_ylim(-total_time - 10, max(target_time_per_day, total_time) + 10)
    ax.set_xlabel('Days')
    ax.set_ylabel('Time (minutes)')
    ax.set_title('Meditation Times')
    
    plt.show()

# Example usage
days = 4
target_time_per_day = 60  # in minutes
daily_sessions = [
    [20, 30, 40],  # Day 1
    [10, 20, 50, 70, 40, 90],  # Day 2
    [50, 30, 40, 30, 40],  # Day 3
    [60, 60],  # Day 4
]
negative_times = [45, 15, 120]  # time in minutes for each negative element

plot_meditation(days, target_time_per_day, daily_sessions, negative_times)
