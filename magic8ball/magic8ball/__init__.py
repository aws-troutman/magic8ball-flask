from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap
import random
import boto.utils

app = Flask(__name__)
Bootstrap(app)

def get_fortunte():
  responses = [
    'It is certain',
    'It is decidedly so',
    'Without a doubt',
    'Yes definitely',
    'You may rely on it',
    'As I see it, yes',
    'Most likely',
    'Outlook good',
    'Yes',
    'Signs point to yes',
    'Reply hazy try again',
    'Ask again later',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again',
    'Don\'t count on it',
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Very doubtful'];

  return random.choice(responses)

@app.route('/_get_new_fortune')
def get_new_fortune():
  random_choice = get_fortune()
  instance_id = boto.utils.get_instance_metadata()['instance-id']
    
  return jsonify([random_choice, instance_id])

@app.route('/magic')
def index():
  instance_id = boto.utils.get_instance_metadata()['instance-id']
  random_choice = get_fortune()

  return render_template('magic.html', instance_id=instance_id, random_choice=random_choice)

if __name__ == '__main__':
    app.run() #'0.0.0.0', 5000 debug=True)
