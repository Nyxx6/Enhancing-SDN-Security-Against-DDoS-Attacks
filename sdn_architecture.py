import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, FancyArrowPatch

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Set background color
ax.set_facecolor('#f8f8f8')

# Define colors
control_color = '#4472C4'
data_color = '#70AD47'
app_color = '#FFC000'
attack_color = '#FF5050'
text_color = '#333333'

# Draw layers
ax.add_patch(Rectangle((1, 1), 8, 2, facecolor=app_color, alpha=0.7, edgecolor='black', linewidth=1))
ax.add_patch(Rectangle((1, 4), 8, 2, facecolor=control_color, alpha=0.7, edgecolor='black', linewidth=1))
ax.add_patch(Rectangle((1, 7), 8, 2, facecolor=data_color, alpha=0.7, edgecolor='black', linewidth=1))

# Add layer labels
ax.text(5, 2, 'Application Layer', ha='center', va='center', fontsize=14, fontweight='bold', color=text_color)
ax.text(5, 5, 'Control Layer', ha='center', va='center', fontsize=14, fontweight='bold', color=text_color)
ax.text(5, 8, 'Infrastructure Layer (Data Plane)', ha='center', va='center', fontsize=14, fontweight='bold', color=text_color)

# Add components
# Application layer components
ax.text(2.5, 1.5, 'Network\nApplications', ha='center', va='center', fontsize=10, color=text_color)
ax.text(5, 1.5, 'Management\nTools', ha='center', va='center', fontsize=10, color=text_color)
ax.text(7.5, 1.5, 'Business\nApplications', ha='center', va='center', fontsize=10, color=text_color)

# Control layer components
ax.text(2.5, 4.5, 'SDN\nController', ha='center', va='center', fontsize=10, color=text_color)
ax.text(5, 4.5, 'Network\nServices', ha='center', va='center', fontsize=10, color=text_color)
ax.text(7.5, 4.5, 'Network\nFunctions', ha='center', va='center', fontsize=10, color=text_color)

# Data plane components
ax.text(2, 7.5, 'Switch', ha='center', va='center', fontsize=10, color=text_color)
ax.text(4, 7.5, 'Switch', ha='center', va='center', fontsize=10, color=text_color)
ax.text(6, 7.5, 'Switch', ha='center', va='center', fontsize=10, color=text_color)
ax.text(8, 7.5, 'Switch', ha='center', va='center', fontsize=10, color=text_color)

# Add interfaces
ax.text(0.5, 3, 'Northbound\nAPI', ha='center', va='center', rotation=90, fontsize=10, color=text_color)
ax.text(0.5, 6, 'Southbound\nAPI\n(OpenFlow)', ha='center', va='center', rotation=90, fontsize=10, color=text_color)

# Add arrows for normal operation
arrow1 = FancyArrowPatch((5, 3), (5, 4), arrowstyle='->', mutation_scale=20, color=control_color, linewidth=2)
ax.add_patch(arrow1)
arrow2 = FancyArrowPatch((5, 6), (5, 7), arrowstyle='->', mutation_scale=20, color=control_color, linewidth=2)
ax.add_patch(arrow2)

# Add attack vector
attack_arrow = FancyArrowPatch((9.5, 8), (5, 6), arrowstyle='->', mutation_scale=20, color=attack_color, linewidth=2, linestyle='--')
ax.add_patch(attack_arrow)
ax.text(9.7, 8, 'DDoS Attack\n(Data-to-Control\nPlane Saturation)', ha='left', va='center', fontsize=10, color=attack_color, fontweight='bold')

# Set limits and remove axes
ax.set_xlim(0, 11)
ax.set_ylim(0, 10)
ax.axis('off')

# Add title
ax.set_title('SDN Architecture and Data-to-Control Plane Saturation Attack', fontsize=16, fontweight='bold', pad=20)

# Save the figure
plt.tight_layout()
plt.savefig('/home/ubuntu/sdn_research/diagrams/sdn_architecture.png', dpi=300, bbox_inches='tight')
plt.close()
