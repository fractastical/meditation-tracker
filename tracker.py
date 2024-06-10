import matplotlib.pyplot as plt

def plot_meditation(days, daily_targets, daily_sessions, daily_negative_times, daily_edifying_practices):
    fig, ax = plt.subplots(figsize=(days + 5, 12))

    # Plotting the daily meditation times
    for i in range(days):
        total_day_time = sum(daily_sessions[i])
        target_time = daily_targets[i]
        # Plot the target meditation time for the day
        ax.add_patch(plt.Rectangle((i + 1, 0), 0.8, target_time, color='gray', alpha=0.3))
        cumulative_time = 0
        for session_time in daily_sessions[i]:
            ax.add_patch(plt.Rectangle((i + 1, cumulative_time), 0.7, session_time, color='blue', alpha=0.6))
            ax.text(i + 1.2, cumulative_time + session_time / 2, f'{session_time} min', va='center', color='black')
            cumulative_time += session_time

    # Plotting the total meditation time rectangle
    total_time = sum(sum(sessions) for sessions in daily_sessions)
    ax.add_patch(plt.Rectangle((0, 0), 0.8, total_time, color='green', alpha=0.6))

    # Plotting the negative elements
    for i in range(days):
        cumulative_time = -400  # start plotting further below the x-axis
        for negative_time in daily_negative_times[i]:
            ax.add_patch(plt.Rectangle((i + 1, cumulative_time), 0.9, negative_time * 4, color='black'))
            ax.text(i + 1.2, cumulative_time + ( negative_time )/ 2, f'{negative_time} min', va='center', ha='left', fontsize=10, color='white')
            cumulative_time -= (negative_time + 5)  # add more space between negative time slots

    # Adding labels for edifying practices
    for i in range(days):
        cumulative_time = max(max(daily_targets), total_time) + 10  # start plotting above the highest meditation target
        practices = '\n'.join([f'• {practice}' for practice in daily_edifying_practices[i]])
        ax.text(i + 1, cumulative_time, practices, va='top', ha='left', fontsize=10, bbox=dict(facecolor='white', alpha=0.6))

    # Setting the labels and titles
    ax.set_xlim(-1, days + 2)
    ax.set_ylim(-total_time - 40, max(max(daily_targets), total_time) + 50)
    ax.set_xlabel('Days')
    ax.set_ylabel('Time (minutes)')
    ax.set_title('Meditation Times')

    plt.show()

# Example usage
days = 6
daily_targets = [45, 60, 75, 90, 30, 30]  # target meditation times per day in minutes
daily_sessions = [
    [30, 30, 30],  # Day 1 actual sessions
    [60, 55, 45, 45, 45, 40, 30],  # Day 2 actual sessions
    [75, 60, 60, 60, 45, 40, 50],  # Day 3 actual sessions
    [60, 60, 50, 40],  # Day 4 actual sessions
    [30, 30],  # Day 4 actual sessions
    [30, 30]  # Day 4 actual sessions

]
daily_negative_times = [
    [10, 15],  # Day 1 negative times
    [45, 10],  # Day 2 negative times
    [30],  # Day 3 negative time
    [50],  # Day 4 negative time
    [100],  # Day 4 negative time
    [10]  # Day 4 negative time

]
daily_edifying_practices = [
    ["Reading", "Yoga", "Agni Sara"],  # Day 1 edifying practices
    ["Know Thyself 25", "Schelling",  "Agni Sara"],  # Day 2 edifying practices
    ["Know Thyself 25", "Le Guin 1",  "Agni Sara"],  # Day 3 edifying practices
    ["Le Guin 2", "Paglia 1",  "Agni Sara"],  # Day 4 edifying practices
    ["Le Guin 3", "Paglia 2"],  # Day 4 edifying practices
    ["Le Guin 4", "Paglia 3"]  # Day 4 edifying practices

]

plot_meditation(days, daily_targets, daily_sessions, daily_negative_times, daily_edifying_practices)
