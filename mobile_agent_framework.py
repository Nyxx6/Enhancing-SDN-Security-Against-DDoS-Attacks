import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle, Ellipse
from matplotlib.lines import Line2D

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 9))

# Set background color
ax.set_facecolor('#f8f8f8')

# Define colors
monitor_color = '#4472C4'  # Blue
analyzer_color = '#70AD47'  # Green
mitigation_color = '#FFC000'  # Yellow
switch_color = '#D9D9D9'  # Light gray
controller_color = '#5B9BD5'  # Light blue
attack_color = '#FF5050'  # Red
text_color = '#333333'  # Dark gray

# Draw SDN infrastructure
# Controller
controller = Rectangle((4, 7), 4, 1.5, facecolor=controller_color, alpha=0.7, edgecolor='black', linewidth=1)
ax.add_patch(controller)
ax.text(6, 7.75, 'SDN Controller', ha='center', va='center', fontsize=12, fontweight='bold', color=text_color)

# Switches
switch_positions = [(2, 3), (5, 3), (8, 3), (11, 3)]
switches = []
for i, pos in enumerate(switch_positions):
    switch = Rectangle((pos[0]-0.75, pos[1]-0.75), 1.5, 1.5, facecolor=switch_color, alpha=0.7, edgecolor='black', linewidth=1)
    ax.add_patch(switch)
    ax.text(pos[0], pos[1], f'Switch {i+1}', ha='center', va='center', fontsize=10, color=text_color)
    switches.append(switch)

# Connect switches to controller
for pos in switch_positions:
    arrow = FancyArrowPatch((pos[0], pos[1]+0.8), (6, 7), arrowstyle='<->', mutation_scale=15, color='gray', linewidth=1, linestyle='-')
    ax.add_patch(arrow)

# Draw agents
# Monitor agents
monitor_positions = [(2, 4.5), (5, 4.5), (8, 4.5), (11, 4.5)]
for pos in monitor_positions:
    monitor = Circle(pos, 0.4, facecolor=monitor_color, alpha=0.8, edgecolor='black', linewidth=1)
    ax.add_patch(monitor)
    ax.text(pos[0], pos[1], 'M', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Analyzer agents
analyzer_positions = [(3.5, 6), (8.5, 6)]
for pos in analyzer_positions:
    analyzer = Circle(pos, 0.5, facecolor=analyzer_color, alpha=0.8, edgecolor='black', linewidth=1)
    ax.add_patch(analyzer)
    ax.text(pos[0], pos[1], 'A', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Mitigation agents
mitigation_positions = [(2, 1.5), (5, 1.5), (8, 1.5), (11, 1.5)]
for pos in mitigation_positions:
    mitigation = Circle(pos, 0.4, facecolor=mitigation_color, alpha=0.8, edgecolor='black', linewidth=1)
    ax.add_patch(mitigation)
    ax.text(pos[0], pos[1], 'Mt', ha='center', va='center', fontsize=10, fontweight='bold', color=text_color)

# Add communication lines
# Monitor to Analyzer
for m_pos in monitor_positions[:2]:
    arrow = FancyArrowPatch(m_pos, analyzer_positions[0], arrowstyle='->', mutation_scale=15, color=monitor_color, linewidth=1, linestyle='-')
    ax.add_patch(arrow)

for m_pos in monitor_positions[2:]:
    arrow = FancyArrowPatch(m_pos, analyzer_positions[1], arrowstyle='->', mutation_scale=15, color=monitor_color, linewidth=1, linestyle='-')
    ax.add_patch(arrow)

# Analyzer to Controller
for a_pos in analyzer_positions:
    arrow = FancyArrowPatch(a_pos, (6, 7), arrowstyle='<->', mutation_scale=15, color=analyzer_color, linewidth=1, linestyle='-')
    ax.add_patch(arrow)

# Analyzer to Mitigation
arrow1 = FancyArrowPatch(analyzer_positions[0], mitigation_positions[0], arrowstyle='->', mutation_scale=15, color=mitigation_color, linewidth=1, linestyle='-')
ax.add_patch(arrow1)
arrow2 = FancyArrowPatch(analyzer_positions[0], mitigation_positions[1], arrowstyle='->', mutation_scale=15, color=mitigation_color, linewidth=1, linestyle='-')
ax.add_patch(arrow2)
arrow3 = FancyArrowPatch(analyzer_positions[1], mitigation_positions[2], arrowstyle='->', mutation_scale=15, color=mitigation_color, linewidth=1, linestyle='-')
ax.add_patch(arrow3)
arrow4 = FancyArrowPatch(analyzer_positions[1], mitigation_positions[3], arrowstyle='->', mutation_scale=15, color=mitigation_color, linewidth=1, linestyle='-')
ax.add_patch(arrow4)

# Add attack vector
attack_start = (13.5, 2.5)
attack_arrow = FancyArrowPatch(attack_start, (11.5, 3), arrowstyle='->', mutation_scale=20, color=attack_color, linewidth=2, linestyle='--')
ax.add_patch(attack_arrow)
ax.text(13.7, 2.5, 'DDoS Attack', ha='left', va='center', fontsize=10, color=attack_color, fontweight='bold')

# Add defense action
defense_arrow = FancyArrowPatch(mitigation_positions[3], (12, 2.5), arrowstyle='-|>', mutation_scale=20, color=mitigation_color, linewidth=2)
ax.add_patch(defense_arrow)
ax.text(12.2, 2.3, 'Mitigation', ha='left', va='center', fontsize=10, color=mitigation_color, fontweight='bold')

# Add legend
legend_elements = [
    Circle((0, 0), 0.4, facecolor=monitor_color, edgecolor='black', label='Monitor Agent'),
    Circle((0, 0), 0.4, facecolor=analyzer_color, edgecolor='black', label='Analyzer Agent'),
    Circle((0, 0), 0.4, facecolor=mitigation_color, edgecolor='black', label='Mitigation Agent'),
    Rectangle((0, 0), 1, 1, facecolor=controller_color, edgecolor='black', label='SDN Controller'),
    Rectangle((0, 0), 1, 1, facecolor=switch_color, edgecolor='black', label='SDN Switch')
]

ax.legend(handles=legend_elements, loc='upper left', fontsize=10)

# Add title and labels
ax.set_title('Distributed Mobile Agent Framework for SDN Security', fontsize=16, fontweight='bold', pad=20)
ax.text(6.5, 0.5, 'Mobile agents detect and mitigate data-to-control plane saturation attacks', 
        ha='center', va='center', fontsize=12, style='italic')

# Set limits and remove axes
ax.set_xlim(0, 14)
ax.set_ylim(0, 9)
ax.axis('off')

# Save the figure
plt.tight_layout()
plt.savefig('/home/ubuntu/sdn_research/diagrams/mobile_agent_framework.png', dpi=300, bbox_inches='tight')
plt.close()
