from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import random
import boto.utils

app = Flask(__name__)
Bootstrap(app)

@app.route('/magic')
def index():
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
  instance_id = boto.utils.get_instance_metadata()['instance-id']
  random_choice = random.choice(responses)
  
  return render_template('magic.html', instance_id=instance_id, random_choice=random_choice)

if __name__ == '__main__':
    app.run() #'0.0.0.0', 5000 debug=True)
