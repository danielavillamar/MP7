import math
import turtle
import random
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


MIDFIELD_X = 315
MIDFIELD_Y = 221
PENALTY = 255
AREA = 225

screen = turtle.getscreen()
# Midfield: 315 x 221
screen.bgpic("field.png")
turtle.hideturtle()

# Create player
player = turtle.Turtle()
player.hideturtle()
player.shapesize(2, 2)
player.penup()

# Create ball
ball = turtle.Turtle()
ball.hideturtle()
ball.penup()
ball.shape('circle')

# Set random positions
player_x = random.randint(0, MIDFIELD_X)
player_y = random.randint(-MIDFIELD_Y, MIDFIELD_Y)
player_r = random.randint(0, 359)
player.goto(player_x, player_y)
player.left(player_r)

ball_x = random.randint(0, MIDFIELD_X)
ball_y = random.randint(-MIDFIELD_Y, MIDFIELD_Y)
ball.goto(ball_x, ball_y)

# Show positions
player.showturtle()
ball.showturtle()


# ==================
# Fuzzy logic
# ==================

# Crear variables linguisticas
distance = ctrl.Antecedent(np.arange(0, 11, 1), 'distance')
direction = ctrl.Antecedent(np.arange(0, 359, 1), 'direction')
run = ctrl.Consequent(np.arange(0, 11, 1), 'run')
rotate = ctrl.Consequent(np.arange(0, 359, 1), 'rotate')

# Membership functions
distance['short'] = fuzz.trimf(distance.universe, [0, 0, 5])
distance['medium'] = fuzz.trimf(distance.universe, [0, 5, 10])
distance['long'] = fuzz.trimf(distance.universe, [5, 10, 10])

direction['right'] = fuzz.trimf(direction.universe, [0, 0, 90])
direction['stright'] = fuzz.trimf(direction.universe, [0, 90, 180])
direction['left'] = fuzz.trimf(direction.universe, [90, 180, 180])

run['short'] = fuzz.trimf(distance.universe, [0, 0, 5])
run['medium'] = fuzz.trimf(distance.universe, [0, 5, 10])
run['long'] = fuzz.trimf(distance.universe, [5, 10, 10])

rotate['left'] = fuzz.trimf(rotate.universe, [0, 0, 90])
rotate['stright'] = fuzz.trimf(rotate.universe, [0, 90, 180])
rotate['right'] = fuzz.trimf(rotate.universe, [90, 180, 180])

# Horn rules
rule1 = ctrl.Rule(distance['short'], run['short'])
rule2 = ctrl.Rule(distance['medium'], run['medium'])
rule3 = ctrl.Rule(distance['long'], run['long'])
rule4 = ctrl.Rule(direction['right'], rotate['left'])
rule5 = ctrl.Rule(direction['stright'], rotate['stright'])
rule6 = ctrl.Rule(direction['left'], rotate['right'])

# Control Running
run_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
running = ctrl.ControlSystemSimulation(run_ctrl)

# Compute Running
running.input['distance'] = abs(player_x-ball_x) * 10 / MIDFIELD_X
running.compute()
move_x = MIDFIELD_X*running.output['run']/10

running.input['distance'] = abs(player_y-ball_y) * 10 / MIDFIELD_Y
running.compute()
move_y = MIDFIELD_Y*running.output['run']/10

player.setheading(player.towards(ball_x, ball_y))
player.forward(math.sqrt((move_x**2)+(move_y**2)))

# Kick ball
# Control Kick
kick_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
kicking = ctrl.ControlSystemSimulation(kick_ctrl)

# Compute Kick
kicking.input['distance'] = abs(ball_x-MIDFIELD_X) * 10 / MIDFIELD_X
kicking.compute()
kick_x = MIDFIELD_X*kicking.output['run']/10

kicking.input['distance'] = abs(ball_y-0) * 10 / MIDFIELD_Y
kicking.compute()
kick_y = MIDFIELD_Y*kicking.output['run']/10

ball.setheading(ball.towards(MIDFIELD_X, 0))
ball.forward(math.sqrt((kick_x**2)+(kick_y**2)))

input()
