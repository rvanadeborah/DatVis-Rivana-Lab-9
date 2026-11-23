
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Lab 9 | Design Principles & Chartjunk",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"], [data-testid="stApp"] {
    font-family: 'Poppins', sans-serif !important;
}

.stApp {
    background: linear-gradient(
        135deg,
        #dceeff 0%,
        #e9e3ff 35%,
        #fce4f0 70%,
        #ffe9dc 100%
    );
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    padding-top: 2.5rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

h1 {
    color: #25345c !important;
    font-weight: 800 !important;
    font-size: 2.6rem !important;
}

h2 {
    color: #34466f !important;
    font-weight: 700 !important;
}

h3 {
    color: #46577e !important;
    font-weight: 600 !important;
}

p, li, label, .stMarkdown {
    color: #37415b;
    line-height: 1.75;
}

.stButton > button {
    background: linear-gradient(90deg, #8bbcf5, #b7a5ef);
    color: white;
    border: none;
    border-radius: 12px;
    font-family: 'Poppins', sans-serif;
    font-weight: 600;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #78a9e8, #a18be5);
    color: white;
    border: none;
}

[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.65);
    padding: 18px;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.8);
}

[data-testid="stDataFrame"],
[data-testid="stDataEditor"] {
    border-radius: 12px;
}

hr {
    border-color: rgba(91, 111, 160, 0.2);
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# CHART SETTINGS
# --------------------------------------------------

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.titleweight"] = "bold"
plt.rcParams["axes.labelcolor"] = "#46516b"
plt.rcParams["xtick.color"] = "#46516b"
plt.rcParams["ytick.color"] = "#46516b"


def create_cluttered_chart(data):
    fig, ax = plt.subplots(figsize=(8, 4.5))

    colors = ["#f28b82", "#fbbc04", "#81c995", "#8ab4f8",
              "#d7aefb", "#ffb3c6"]

    ax.bar(
        data["Branch"],
        data["Sales"],
        color=colors[:len(data)],
        edgecolor="black",
        linewidth=1.5
    )

    # Truncated y-axis
    ax.set_ylim(95, 101)

    # Excessive gridlines
    ax.set_facecolor("#e5e5e5")
    ax.grid(
        True,
        axis="both",
        color="white",
        linewidth=1.8
    )

    ax.set_title(
        "!!! SALES PERFORMANCE BY BRANCH !!!",
        fontsize=14,
        fontweight="bold",
        color="red"
    )

    ax.set_xlabel("Branch", fontsize=11)
    ax.set_ylabel("Sales", fontsize=11)

    for spine in ax.spines.values():
        spine.set_linewidth(1.5)
        spine.set_color("black")

    fig.tight_layout()
    return fig


def create_improved_chart(data, highlight_highest=True):
    fig, ax = plt.subplots(figsize=(8, 4.5))

    highest_index = data["Sales"].idxmax()

    colors = [
        "#a8c9f0" for _ in range(len(data))
    ]

    if highlight_highest:
        colors[highest_index] = "#f4a6b9"

    bars = ax.bar(
        data["Branch"],
        data["Sales"],
        color=colors,
        width=0.6,
        edgecolor="white"
    )

    # Start y-axis at zero
    ax.set_ylim(0, max(data["Sales"]) * 1.2)

    ax.set_title(
        "Sales Performance by Branch",
        fontsize=15,
        fontweight="bold",
        color="#34466f",
        pad=15
    )

    ax.set_xlabel("Branch", fontsize=11)
    ax.set_ylabel("Sales", fontsize=11)

    # Simple horizontal gridlines
    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.3,
        color="#9aa8c1"
    )

    ax.set_axisbelow(True)

    # Remove unnecessary borders
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Add data labels
    ax.bar_label(
        bars,
        fmt="%.0f",
        padding=4,
        fontsize=10,
        color="#34466f"
    )

    fig.tight_layout()
    return fig


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.title("Design Principles & Chartjunk")

st.markdown(
    "### Lab 9 | Data Visualization"
)

st.write(
    "Understanding how good design choices can make data "
    "visualizations clearer, more accurate, and easier to understand."
)

st.caption("TFB3133 / TEB3133 · Data Visualization")

st.divider()


# --------------------------------------------------
# INTRODUCTION
# --------------------------------------------------

st.header("01. Understanding Data Visualization")

st.write(
    "Data visualization is the process of presenting information "
    "through charts and graphs. A good visualization should help "
    "readers understand the data quickly without unnecessary "
    "decoration or misleading design choices."
)

st.write(
    "In this lesson, we compare two charts using the same sales "
    "data. The first chart contains several design problems, while "
    "the second chart applies better visualization principles."
)

st.divider()


# --------------------------------------------------
# LESSON 1: ORIGINAL DATA
# --------------------------------------------------

st.header("02. Lesson 1 — Improving Data Visualization")

st.subheader("Original Dataset")

original_data = pd.DataFrame({
    "Branch": ["North", "South", "East", "West"],
    "Sales": [96, 99, 98, 100]
})

st.dataframe(
    original_data,
    use_container_width=True,
    hide_index=True
)

st.caption(
    "The dataset contains fictional sales values from four branches."
)

st.subheader("Chart Comparison")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### A. Cluttered Chart")
    st.write(
        "This chart uses a shortened y-axis, too many colors, "
        "a grey background, and excessive gridlines."
    )

    fig1 = create_cluttered_chart(original_data)
    st.pyplot(fig1)
    plt.close(fig1)

with col2:
    st.markdown("#### B. Improved Chart")
    st.write(
        "This chart starts the y-axis at zero, uses simple colors, "
        "clear labels, and fewer gridlines."
    )

    fig2 = create_improved_chart(original_data)
    st.pyplot(fig2)
    plt.close(fig2)

st.subheader("Why Can a Shortened Axis Be Misleading?")

st.write(
    "The cluttered chart starts its y-axis at 95 instead of zero. "
    "Because the values are close to each other, the differences "
    "between branches appear much larger than they actually are."
)

st.write(
    "The improved chart starts at zero, allowing readers to compare "
    "the values more fairly and understand the actual differences."
)

st.info(
    "Important: For a standard bar chart, starting the y-axis at zero "
    "helps prevent exaggerated visual differences."
)

st.divider()


# --------------------------------------------------
# LESSON 2: DESIGN STANDARDS
# --------------------------------------------------

st.header("03. Lesson 2 — Ten Design Standards")

st.write(
    "These ten standards can be used to evaluate whether a data "
    "visualization is clear, accurate, and effective."
)

standards = [
    (
        "1. Chart Format",
        "Choose a chart type that matches the data and the purpose of the presentation."
    ),
    (
        "2. Color",
        "Use suitable colors consistently. Avoid using too many colors without a reason."
    ),
    (
        "3. Text and Labels",
        "Provide clear titles, axis labels, and readable text."
    ),
    (
        "4. Readability",
        "Make sure the chart is easy to read and understand."
    ),
    (
        "5. Scales",
        "Use appropriate axis scales so the visualization does not mislead readers."
    ),
    (
        "6. Data Integrity",
        "Present the data accurately without changing or distorting its meaning."
    ),
    (
        "7. Chartjunk",
        "Avoid unnecessary decorations, excessive gridlines, and other distracting elements."
    ),
    (
        "8. Data Density",
        "Present an appropriate amount of information without overcrowding the chart."
    ),
    (
        "9. Data Richness",
        "Include useful information that helps readers understand the data."
    ),
    (
        "10. Attribution",
        "Provide information about the data source and the person who created the chart."
    )
]

for title, description in standards:
    with st.expander(title):
        st.write(description)

st.divider()


# --------------------------------------------------
# LESSON 3: EDITABLE DATASET
# --------------------------------------------------

st.header("04. Lesson 3 — Improve Your Own Chart")

st.write(
    "Now, edit the dataset below. You can change the branch names "
    "and sales values or add two additional categories."
)

edited_data = pd.DataFrame({
    "Branch": ["North", "South", "East", "West", "Central", "Coastal"],
    "Sales": [96, 99, 98, 100, 97, 95]
})

st.subheader("Edit Dataset")

st.caption(
    "You can modify the values directly in the table. "
    "The chart below will update automatically."
)

user_data = st.data_editor(
    edited_data,
    use_container_width=True,
    num_rows="dynamic",
    hide_index=True,
    column_config={
        "Branch": st.column_config.TextColumn(
            "Branch Name",
            help="Enter the category or branch name.",
            required=True
        ),
        "Sales": st.column_config.NumberColumn(
            "Sales Value",
            help="Enter the sales value.",
            min_value=0,
            step=1,
            required=True
        )
    },
    key="editable_sales_data"
)

# Clean data before plotting
user_data = user_data.copy()
user_data["Branch"] = user_data["Branch"].fillna("").astype(str)
user_data["Sales"] = pd.to_numeric(
    user_data["Sales"],
    errors="coerce"
)

user_data = user_data[
    (user_data["Branch"].str.strip() != "") &
    (user_data["Sales"].notna())
]

user_data = user_data[user_data["Sales"] >= 0]

st.subheader("Your Improved Visualization")

if len(user_data) > 0:
    fig3 = create_improved_chart(user_data)
    st.pyplot(fig3, use_container_width=True)
    plt.close(fig3)

    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric("Total Categories", len(user_data))

    with metric2:
        st.metric(
            "Highest Sales",
            f"{user_data['Sales'].max():,.0f}"
        )

    with metric3:
        st.metric(
            "Lowest Sales",
            f"{user_data['Sales'].min():,.0f}"
        )

else:
    st.warning(
        "Please enter at least one valid category and sales value "
        "to display the chart."
    )

st.caption(
    "Data: fictional practice values (2026) | Chart: Your Name"
)

st.divider()


# --------------------------------------------------
# CRITIQUE CHECKLIST
# --------------------------------------------------

st.header("05. Chart Critique")

st.write(
    "Use the checklist below to identify design standards that "
    "were improved in the second chart."
)

critique_items = [
    "The chart uses an appropriate format.",
    "The colors are simple and consistent.",
    "The title and labels are clear.",
    "The chart is easy to read.",
    "The y-axis starts at zero.",
    "The data is presented accurately.",
    "Unnecessary chart decorations are removed.",
    "The chart does not contain too much information.",
    "The visualization provides useful information.",
    "The data source and chart author are included."
]

selected_items = []

for item in critique_items:
    checked = st.checkbox(item, key=f"critique_{item}")
    if checked:
        selected_items.append(item)

st.write(
    f"**Standards identified: {len(selected_items)} / 10**"
)

if len(selected_items) >= 5:
    st.success("You have identified at least five design improvements.")
else:
    st.info("Identify at least five improvements to complete this section.")

st.divider()


# --------------------------------------------------
# REFLECTION
# --------------------------------------------------

st.header("06. Reflection")

st.write(
    "Write a short reflection of 150–200 words about what you "
    "learned from this activity."
)

st.write(
    "You may discuss the differences between the two charts, "
    "how chart design can affect the interpretation of data, "
    "and which design standards are important when creating "
    "a visualization."
)

reflection = st.text_area(
    "Your Reflection",
    placeholder="Write your reflection here...",
    height=220,
    key="reflection_text"
)

word_count = len(reflection.split())

st.caption(f"Word count: {word_count} words")

if 150 <= word_count <= 200:
    st.success("Your reflection meets the 150–200 word requirement.")
elif word_count < 150:
    st.info(f"You need approximately {150 - word_count} more words.")
else:
    st.warning(f"Your reflection is approximately {word_count - 200} words over the limit.")

st.divider()


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("### Lab 9 Completed")

st.write(
    "Good data visualization is not only about making charts look "
    "attractive. It is also about presenting information clearly, "
    "accurately, and honestly."
)

st.caption("Data Visualization | Lab 9")
