from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import pyrebase

# Firebase configuration
firebase_config = {
    # enter creds here
}   

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()
#enter openai key
client = OpenAI(api_key='')

app = Flask(__name__)

def generate_fitness_plan(height, weight, muscle_mass):
    model = "gpt-4"
    prompt = f"Generate a personalized fitness plan for a user with the following details:\nHeight: {height} feet\nWeight: {weight} lb\nFitness Goal: {muscle_mass}"
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant. You will never have your responses cut off. You will make sure to be friendly at all times and to give the utmost detail in your responses. Your name is Fitness Guru. Additionally you are to give detailed fitness plans rather than descriptions of each fitness plan. Weight and height are provided in the United States Metric system."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=5000,
            temperature=0.7,
            top_p=1,
            n=1,
            stop=None
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        muscle_mass = request.form['muscle_mass']
        fitness_plan = generate_fitness_plan(height, weight, muscle_mass)
        
        user = auth.current_user
        if user:
            user_id = user['localId']
            db.child('users').child(user_id).child('fitness_plans').push({'height': height, 'weight': weight, 'muscle_mass': muscle_mass, 'fitness_plan': fitness_plan})
        
        fitness_score = calculate_fitness_score(height, weight, muscle_mass)
        
        return render_template('result.html', fitness_plan=fitness_plan, fitness_score=fitness_score)
    return render_template('index.html')

@app.route('/calorie-tracker', methods=['GET', 'POST'])
def calorie_tracker():
    return render_template('calorie_tracker.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question')
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Keep responses short and concise. Your name is fitenss guru. You do not need to provide full workout plans. You are to just provide insight into workouts. Users already know their workout plan."},
                {"role": "user", "content": question}
            ],
            max_tokens=2500,
            temperature=0.7,
            top_p=1,
            n=1,
            stop=None
        )
        answer = response.choices[0].message.content.strip()
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def calculate_fitness_score(height, weight, muscle_mass):
    # Placeholder fitness score calculation
    return (height * weight) / 10

if __name__ == '__main__':
    app.run(debug=True)
