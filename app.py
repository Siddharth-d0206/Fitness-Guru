from flask import Flask, render_template, request
from openai import OpenAI

client = OpenAI(api_key='sk-proj-TKT63VOvUpok4aWhtaHIT3BlbkFJ56vu0L3nbVem3kE5TSU1')

# Initialize the OpenAI client with the API key

app = Flask(__name__)

# Define a function to generate fitness plans using the updated OpenAI API
def generate_fitness_plan(height, weight, muscle_mass):
    model = "gpt-4"
    prompt = f"Generate a personalized fitness plan for a user with the following details:\nHeight: {height} meters\nWeight: {weight} kg\nFitness Goal: {muscle_mass}"
    try:
        response = client.chat.completions.create(model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant. You will never have your responses cut off. You will make sure to be friendly at all times and to give the utmost detail in your responses. Your name is Fitness Guru. Additionally you are to give detailed fitness plains rather than descriptions of each fitness plan."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,  # Increase this value to allow for longer responses
        temperature=0.7,
        top_p=1,
        n=1,
        stop=None)
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

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
