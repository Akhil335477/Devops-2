from flask import Flask, render_template, request

app = Flask(_name_)

# Define your questions
questions = [
    {"question": "What color are apples?", "options": ["Red/Green", "Purple", "Orange"], "answer": "Red/Green"},
    {"question": "What color are bananas?", "options": ["Teal", "Magenta", "Yellow"], "answer": "Yellow"},
    {"question": "What color are strawberries?", "options": ["Yellow", "Red", "Blue"], "answer": "Red"}
]

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for i, q in enumerate(questions):
        user_answer = request.form.get(f'question{i+1}')
        if user_answer == q['answer']:
            score += 1
    return f'You got {score}/{len(questions)} correct.'

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
