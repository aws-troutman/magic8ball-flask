from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap
import random
import boto.utils
import boto.regioninfo
import boto.ec2

app = Flask(__name__)
Bootstrap(app)


def get_title():
  return 'Hello Trainers (made of carbon).'

def get_fortune():
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

@app.route('/_get_lb_info')
def get_lb_state():
  elb_region = boto.regioninfo.RegionInfo(
      name='us-west-2', 
      endpoint='elasticloadbalancing.us-west-2.amazonaws.com')

  elb_connection = boto.connect_elb(region=elb_region)
  state = elb_connection.describe_instance_health('magic-eight-ball-python')
  return_value = {}
  for instance in state:
    return_value[instance.instance_id] = instance.state
  return jsonify(return_value)

@app.route('/_get_new_fortune')
def get_new_fortune():
  random_choice = get_fortune()
  instance_id = boto.utils.get_instance_metadata()['instance-id']
  return jsonify({('random_choice',random_choice),('instance_id',instance_id)})  

@app.route('/_get_title')
def get_new_title():
  return jsonify({'title': get_title()})

@app.route('/magic')
def index():
  instance_id = boto.utils.get_instance_metadata()['instance-id']
  random_choice = get_fortune()

  return render_template('magic.html', instance_id=instance_id, random_choice=random_choice)

if __name__ == '__main__':
    app.run() #'0.0.0.0', 5000 debug=True)
