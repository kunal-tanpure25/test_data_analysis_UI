from flask import Flask, render_template
from filter_data import filter_program_data
from plot_data import plotting

app = Flask(__name__)

@app.route('/')
def index():
    # Assuming filter_program_data returns the filtered DataFrame
    data = filter_program_data("PRG-3 (11_32_21 am).xlsx")  # Update with your file path

    if data is not None:
        # Assuming plotting function generates plots and saves them as images
        plotting(data)
        # Pass the DataFrame as HTML table to the template
        data_table = data.to_html(classes='data', header="true", index=False)
    else:
        data_table = "<p>Error: Failed to process data.</p>"

    return render_template('index.html', data_table=data_table)

if __name__ == '__main__':
    app.run(debug=True)
