from flask import Flask, render_template, request
import openai

openai.api_key = 'sk-proj-oaa5ZKq8WWOtqV1glSHtT3BlbkFJPgloVM3quccxED8KVj1f'

app = Flask(__name__)

# Define a function to generate fitness plans using the updated OpenAI API
def generate_fitness_plan(height, weight, muscle_mass):
    model = "gpt-3.5-turbo"
    prompt = f"Generate a personalized fitness plan for a user with the following details:\nHeight: {height} meters\nWeight: {weight} kg\nMuscle Mass: {muscle_mass} kg"
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response['choices'][0]['message']['content'].strip()

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
