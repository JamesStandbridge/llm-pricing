# Language Model API Cost Analysis Tool

This application, built with Streamlit, offers an in-depth analysis of the costs involved with various Language Model APIs, considering factors such as user count, monthly requests, and token consumption. It features comparisons of costs between models, the cost dynamics as user numbers fluctuate, and comprehensive breakdowns of costs for input and output tokens.

## Key Features

- **Cost Comparison Among Models**: Estimate and compare the monthly and per-user costs for different language models.
- **Cost Dynamics Visualization**: See how the costs change with variations in user numbers.
- **In-depth Cost Analysis**: Get insights into the costs related to input and output tokens.
- **Dynamic User Inputs**: Modify user count, monthly requests, and token consumption to observe cost implications in real time.

## Setup Instructions

To deploy this application, ensure you have Python and the necessary libraries. Follow these steps:

1. **Python Installation**: Download and install Python from python.org according to your operating system's guidelines.
2. **Poetry Installation**: Install Poetry for handling dependencies. Follow the instructions on the Poetry website (https://python-poetry.org/docs/).
3. **Project Setup and Dependency Management**:
   - Initialize the project with Poetry if starting from scratch:
     ```bash
     poetry new llm-cost-analysis
     cd llm-cost-analysis
     ```
   - To install dependencies with Poetry, add them to your `pyproject.toml` file or use:
     ```bash
     poetry add streamlit pandas plotly numpy
     ```

## Launching the Tool

With the setup complete, execute the following command in your terminal or command prompt to start the application:

```bash
streamlit run main.py
```
