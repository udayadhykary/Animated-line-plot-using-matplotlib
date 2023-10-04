import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define your data
x = [1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	25,	26,	27,	28,	29,	30,	31,
]  
y = [890343,	1743974,	1766346,	2026119,	1363075,	1912901,	511380,	851859,	1143166,	1679879,	620421,	2360356,	1591791,	658442,	2066952,	1352830,	1905753,	2235927,	1911251,	1878802,	2352436,	1474884,	2360396,	1015390,	633609,	1277108,	811653,	1603553,	1313998,	2163883,	620912,
]  # y values

x2 = [1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	25,	26,	27,	28,	29,	30,	31,
]  
y2 = [190343,	743974,	766346,	1026119,	5363075,	912901,	811380,	151859,	2143166,	1679879,	620421,	2360356,	1591791,	658442,	2066952,	1352830,	1905753,	2235927,	1911251,	1878802,	2352436,	1474884,	2360396,	1015390,	633609,	1277108,	811653,	1603553,	1313998,	2163883,	620912,
]  # y values

# Create an initial empty plot
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], color='green')

# Define the initialization function for the animation
def init():
    ax.set_xlim(0, 40)
    ax.set_ylim(100000, 3000000)
    line.set_data([], [])
    line.set_label("Data1")
    line2.set_data([], [])
    line2.set_label("Data2")
    return line,

# Define the update function for the animation
def update(frame):
    x_data = x[:frame]
    y_data = y[:frame]
    line.set_data(x_data, y_data)
    x_data2 = x2[:frame]
    y_data2 = y2[:frame]
    line2.set_data(x_data2, y_data2)
    return line,line2

# Create the animation
ani = FuncAnimation(fig, update, frames=len(x), init_func=init, blit=True, repeat=False)

# Set axis labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Animated Line Plot')

plt.legend()

# Show the animated plot
plt.show()