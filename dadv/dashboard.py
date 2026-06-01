import matplotlib.pyplot as plt
from database import get_top_scores

def show_analytics_dashboard():
    """
    Fetches the top scores from the database and displays them
    in a beautiful Matplotlib Bar Chart.
    """
    scores_data = get_top_scores(limit=10)
    
    if not scores_data:
        return False # No data to show
        
    # Extract data for plotting
    # scores_data is a list of tuples: (player_name, score, levels)
    # We might have duplicate names, so we add an index to make labels unique if needed
    labels = []
    scores = []
    
    for idx, row in enumerate(scores_data):
        name = row[0]
        score = row[1]
        labels.append(f"{name}\n({score})")
        scores.append(score)

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Colors: Indian Flag Theme (Saffron, Green, Navy Blue)
    colors = ['#FF6F00', '#0A7E07', '#1A237E'] * (len(scores) // 3 + 1)
    
    # Create bar chart
    bars = ax.bar(labels, scores, color=colors[:len(scores)], edgecolor='black', linewidth=1.2)
    
    # Customize the plot
    ax.set_title('🏆 Swadeshi Quest - Top 10 High Scores 🏆', fontsize=18, fontweight='bold', color='#1A237E', pad=20)
    ax.set_xlabel('Players', fontsize=14, fontweight='bold')
    ax.set_ylabel('Total Score', fontsize=14, fontweight='bold')
    
    # Add gridlines behind bars for better readability
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    
    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=12, fontweight='bold')

    # Add a Saffron/Green border to the figure
    fig.patch.set_linewidth(5)
    fig.patch.set_edgecolor('#FF6F00')
    
    # Adjust layout and display
    plt.tight_layout()
    plt.show()
    return True
