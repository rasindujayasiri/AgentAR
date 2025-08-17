# AgentAR
# Automated Restaurant Feedback Agent for SteamNoodles - [Your Name]

This project contains a multi-agent framework designed to enhance the customer feedback process for the "SteamNoodles" restaurant chain, as outlined in the AgentX Project Guideline Book. It features two distinct AI agents: one for generating automated responses to customer feedback and another for visualizing sentiment trends over time.

  - [cite\_start]**Project:** AgentX Guildline Book [cite: 5]
  - [cite\_start]**Organization:** Leos of SriLanka & Maldives, Leo Club of University of Moratuwa [cite: 1, 7]
  - [cite\_start]**Sponsor:** ZONE24x7 [cite: 6]

## Contributor Information

  - **Name:** `Rasindu Lakshan`
  - **University:** `University of Moratuwa`
  - **Year:** `2nd year`

## Summary of Approach

This solution implements the two required agents using a combination of LangChain for language model interactions and standard Python libraries for data analysis and visualization.

1.  [cite\_start]**Customer Feedback Response Agent**: This agent leverages the **LangChain** framework with an **OpenAI GPT-3.5-turbo** model[cite: 36, 39]. [cite\_start]A specific prompt template was engineered to instruct the model to analyze the sentiment of a customer's review (positive, negative, or neutral) and generate a polite, context-aware reply that acknowledges the user's key points[cite: 25, 27].

2.  [cite\_start]**Sentiment Visualization Agent**: This agent uses the **pandas** library for data manipulation and **matplotlib/seaborn** for plotting[cite: 40]. It processes a dataset of reviews with timestamps and sentiment labels. [cite\_start]The agent is designed to take a date range as input, aggregate the sentiment data within that period, and generate a bar plot to visualize the daily count of positive, negative, and neutral reviews dynamically[cite: 29, 31]. [cite\_start]The dataset used is a simulation of the required Kaggle restaurant review dataset[cite: 41].

[cite\_start]The entire solution is presented as a single Python script for ease of execution and testing[cite: 42].

## Setup Instructions

Follow these steps to set up the environment and run the project.

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/steamnoodles-feedback-agent-[your-name].git
    cd steamnoodles-feedback-agent-[your-name]
    ```

2.  **Create a Virtual Environment (Recommended)**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies**
    A `requirements.txt` file is included for easy installation.

    ```bash
    pip install -r requirements.txt
    ```

    *The `requirements.txt` file should contain:*

    ```
    langchain-openai
    pandas
    matplotlib
    seaborn
    ```

4.  **Set Up OpenAI API Key**
    This project requires an OpenAI API key. Set it as an environment variable for security.

    ```bash
    export OPENAI_API_KEY='your_openai_api_key_here'
    ```

## How to Test Each Agent

The project is contained in a single Python script (`main.py`). You can run it directly from your terminal to see the demo outputs for both agents.

```bash
python main.py
```

### Agent 1: Customer Feedback Response Agent

[cite\_start]The script will automatically run demos for Agent 1. It will process one sample for each sentiment (positive and negative) and print the automated response to the console[cite: 53].

### Agent 2: Sentiment Visualization Agent

The script will also automatically run the demo for Agent 2. It will:

1.  Use a sample dataset of reviews.
2.  [cite\_start]Define a date range (e.g., "August 1 to August 7")[cite: 29].
3.  [cite\_start]Generate a bar plot showing the sentiment trends for that period[cite: 30].
4.  [cite\_start]The plot will be displayed on the screen and saved as a PNG file in the project's root directory[cite: 54].

## Sample Prompts and Expected Outputs

### Agent 1: Sample Prompts & Outputs

**Sample 1 (Positive Feedback):**

  - **Input Prompt:** `"The spicy ramen was absolutely delicious, and the service was incredibly fast! Best noodles in town."`
  - **Expected Output:**
    ```
    [=] Automated Response:
    'Thank you so much for your kind words! We are thrilled to hear you enjoyed our spicy ramen and found our service to be fast. We look forward to welcoming you back to SteamNoodles again soon!'
    ```

**Sample 2 (Negative Feedback):**

  - **Input Prompt:** `"I was really disappointed with my visit. The broth was lukewarm, and my order took almost 45 minutes to arrive."`
  - **Expected Output:**
    ```
    [=] Automated Response:
    'Thank you for taking the time to share your feedback. We sincerely apologize that your broth was not served at the right temperature and for the significant delay in receiving your order. This is not the standard of service we aim for, and we will be looking into this with our kitchen and service teams to ensure it does not happen again.'
    ```

### Agent 2: Sample Prompt & Output

  - **Input Prompt:** A date range of `"2025-08-01"` to `"2025-08-07"`.
  - **Expected Output:** A plot image file named `sentiment_plot_2025-08-01_to_2025-08-07.png` will be generated in the project directory, displaying the daily sentiment counts.
