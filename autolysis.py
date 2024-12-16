import sys
import pandas as pd
from dotenv import load_dotenv
import os
import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns
import io

load_dotenv()
api_key = os.getenv("api_key")

if len(sys.argv) < 2:
	print("Usage: python3 autolysis-v2.py <path_to_csv>")
	sys.exit(1)

datasetCSV = sys.argv[1]
directory_name = datasetCSV.split('.')[0]
try:
    df = pd.read_csv(datasetCSV, encoding='latin1')
except UnicodeDecodeError:
    print("Failed to decode file. Try another encoding like 'utf-16'.")
    sys.exit(1)



# Capture the output in a string buffer
output_buffer = io.StringIO()

# General information
output_buffer.write("Dataset Information:\n")
df.info(buf=output_buffer)

# Summary statistics for numeric columns
output_buffer.write("\n\nSummary Statistics (Numeric Columns):\n")
output_buffer.write(df.describe().to_string())

# Summary statistics for categorical columns
categorical_columns = df.select_dtypes(include=['object']).columns
output_buffer.write("\n\nSummary Statistics (Categorical Columns):\n")
for column in categorical_columns:
    output_buffer.write(f"\nColumn: {column}\n")
    output_buffer.write(df[column].value_counts().head(10).to_string())  # Top 10 most common values

# Check for missing values
output_buffer.write("\n\nMissing Values:\n")
output_buffer.write(df.isnull().sum().to_string())

# Select only numeric columns
numeric_df = df.select_dtypes(include=['number'])

# Check if there are any numeric columns
if not numeric_df.empty:
    output_buffer.write("\n\nCorrelation Matrix:\n")
    output_buffer.write(numeric_df.corr().to_string())
else:
    output_buffer.write("\n\nNo numeric columns found for correlation matrix.")

# Retrieve the entire output as a string
analysis_output = output_buffer.getvalue()
output_buffer.close()

#print(analysis_output)



response_analyze = requests.post(
        "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
                "model": "gpt-4o-mini",
                "messages": [
                        {"role": "system" , "content": "To analyze and visualize the given data. Create README.md and png files for the same."},
                        {"role": "user", "content": f"Analyze the following dataset and provide a detailed analysis, including insights, trends, and potential outliers:\n\n{analysis_output}"  }
                ]
}
)



analysis = response_analyze.json()

if 'choices' in analysis and len(analysis['choices']) > 0:
    analysis_text = analysis['choices'][0]['message']['content']
else:
    print("Failed to get analysis from LLM.")
    sys.exit(1)

# Step 2: Save Analysis to README File
with open("./%s/README.md" % directory_name,"w") as readme_file:
    readme_file.write("# Data Analysis Report\n\n")
    readme_file.write(analysis_text)

print("Analysis saved to README.md.")

#Remove or Encode Non-numeric data
df_numeric = df.select_dtypes(include=[float, int])

#Convert non-numeric columsn to numeric



# Step 3: Generate Visualizations
# Example Visualization: Correlation Heatmap

sns.set(style="whitegrid")

plt.figure(figsize=(12, 10))  # Increase figure size for better visibility
heatmap = sns.heatmap(df_numeric.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap", fontsize=16)  # Add a larger title for better aesthetics
plt.xticks(rotation=45, ha='right', fontsize=10)  # Rotate x-axis labels for readability
plt.yticks(fontsize=10)  # Adjust y-axis label font size
plt.tight_layout()  # Automatically adjust layout to fit all elements
plt.savefig("./%s/correlation_heatmap.png" % directory_name)
plt.close()


# Example Visualization: Pairplot
sns.pairplot(df_numeric, diag_kind='kde')
plt.savefig("./%s/pairplot.png" % directory_name)
plt.close()

#print("Visualizations saved as PNG files.")
