# -*- coding: utf-8 -*-
"""Week 8 Practice Notebook: Connecting to Redis - Breakout 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14G2NeluW7HLydFmDX2JcujkjU0f8vlwQ

# Practice Notebook: Connecting to Redis
"""





"""## Challenge

Write a Python function connect_redis that takes in three arguments - hostname, port_number, and password and returns a Redis object that is connected to a Redis instance hosted on Redis Labs using the given arguments.

Hints:
* Use the redis module to import the Redis class.
* Use the Redis() class constructor to create a Redis object and pass the hostname, port_number, and password arguments to the constructor.
* Use return statement to return the Redis object.
"""

!pip install redis

# Your code goes here

# import redis
import redis

# define the function
def connect_redis(host, port, password):
  r = redis.Redis(
  host=host,
  port=port,
  password= password)
  return r

host='redis-15919.c91.us-east-1-3.ec2.cloud.redislabs.com'
port=15919
password='nVmHZlngfY9h61SwlkrcIsk8VF4ukWe4'

connect_redis(host, port, password)

first_name = 'Kemboi'
last_name = 'Allan'

print('')

"""### Sample Solution"""

import redis

def connect_redis(hostname, port_number, password):
    r = redis.Redis(host=hostname, port=port_number, password=password)
    return r

return message_string