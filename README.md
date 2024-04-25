# LLM API Cost Analysis Application

This Streamlit application provides a comprehensive analysis of the costs associated with different Language Model APIs based on various parameters like number of users, requests per month, and tokens used. It includes features like cost comparison across models, cost evolution with user numbers, and detailed breakdowns of input and output costs.

## Features

- **Model Cost Comparison**: Compare estimated monthly costs and per-user costs across different models.
- **Evolution of Cost**: Visualize how costs evolve as the number of users changes.
- **Detailed Cost Breakdown**: Understand the proportion of costs attributable to input versus output tokens.
- **Interactive Controls**: Adjust parameters like number of users, requests per month, and token usage to see real-time changes in costs.

## Installation

To run this application, you'll need Python and several libraries installed. Follow these steps:

1. **Install Python**: If you don't already have Python installed, download it from python.org and follow the installation instructions for your operating system.
2. **Set up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv llm-api-env
   source llm-api-env/bin/activate  # On Windows use `llm-api-env\Scripts\activate`
   ```
3. **Install Required Libraries**:
   ```bash
   pip install streamlit pandas plotly numpy
   ```

## Running the Application

Once you have everything installed, you can run the application using the following command in your terminal or command prompt:
