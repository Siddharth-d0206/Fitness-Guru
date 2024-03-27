from flask import Flask, render_template, request
from openai import OpenAI

client = OpenAI(api_key='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')

app = Flask(__name__)

# Set your OpenAI API key

# Define a function to generate fitness plans using GPT-3
def generate_fitness_plan(height, weight, muscle_mass):
    engine="text-davinci-003"
    stream=True
    prompt = f"Generate a personalized fitness plan for a user with the following details:\nHeight: {height} meters\nWeight: {weight} kg\nMuscle Mass: {muscle_mass} kg"
    response = client.completions.create(engine="text-davinci-003",
    prompt=prompt,
    max_tokens=150)
    return response.choices[0].text.strip()

# Define route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        muscle_mass = float(request.form['muscle_mass'])
        
        # Generate fitness plan based on user input
        fitness_plan = generate_fitness_plan(height, weight, muscle_mass)
        return render_template('result.html', fitness_plan=fitness_plan)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

