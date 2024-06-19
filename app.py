from flask import Flask, render_template, request
from openai import OpenAI

client = OpenAI(api_key='sk-proj-TKT63VOvUpok4aWhtaHIT3BlbkFJ56vu0L3nbVem3kE5TSU1')


app = Flask(__name__)

# Define a function to generate fitness plans using the updated OpenAI API
def generate_fitness_plan(height, weight, muscle_mass):
    model = "gpt-4"
    prompt = f"Generate a personalized fitness plan for a user with the following details:\nHeight: {height} meters\nWeight: {weight} kg\nMuscle Mass: {muscle_mass} kg"
    response = client.chat.completions.create(model=model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant. You will never have your repsonses cutout. You will make sure to be freindly at all times and to give the utmost detail in your responses. Your name is fitness guru"},
        {"role": "user", "content": prompt}
    ],
    max_tokens=150)
    return response.choices[0].message.content.strip()

# Define route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        muscle_mass = (request.form['muscle_mass'])

        # Generate fitness plan based on user input
        fitness_plan = generate_fitness_plan(height, weight, muscle_mass)
        return render_template('result.html', fitness_plan=fitness_plan)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
