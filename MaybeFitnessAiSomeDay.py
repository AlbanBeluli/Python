import tensorflow as tf
from flask import Flask, render_template, jsonify, request
import pandas as pd
import numpy as np
import json
import os
import time
import datetime


workout_data = [
    {"exercise": "Pull-ups", "repetitions": 25, "time": 300},
    {"exercise": "Push-ups", "repetitions": 25, "time": 180},
    {"exercise": "Sit-ups", "repetitions": 50, "time": 120},
    {"exercise": "Squats", "repetitions": 25, "time": 150},
    {"exercise": "Lunge Walk", "repetitions": 25, "time": 240},
    {"exercise": "Climbers", "repetitions": 25, "time": 200}
]

#ask daily for the bmi add a bmi calculator

#add a bmi calculator
height = float(input("Enter your height in CM:\n "))
weight = float(input("Enter your weight in KG:\n "))
age = int(input("Enter your age:\n "))
bmi = int(weight / (height/100)**2)
print("Your BMI is: ", round(bmi, 2))
if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print("You are normal.")
elif bmi >= 25 and bmi < 30:
    print("You are overweight.")
elif bmi >= 30:
    print("You are obese.")
#save bmi to a csv file and append each day column BMI, Date, Age
bmi = pd.DataFrame({'BMI': bmi, 'Date': datetime.date.today(), 'Age': age}, index=[0])
bmi.to_csv('bmi.csv', mode='a', header=True)

#use the bmi to determine the fitness level
fitness_levels = ['beginner', 'intermediate', 'advanced', 'expert', 'elite']
if bmi < 18.5: 
    fitness_level = fitness_levels[0]
elif bmi >= 18.5 and bmi < 25:
    fitness_level = fitness_levels[2]
    if age < 30:
        fitness_level = fitness_levels[3]
    elif age >= 20 and age < 30:
        fitness_level = fitness_levels[2, 3, 4]
    elif age >= 30 and age < 40:
        fitness_level = fitness_levels[2, 3, 4]
    elif age >= 40 and age < 50:
        fitness_level = fitness_levels[1, 2, 3, 4]
    elif age >= 50 and age < 60:
        fitness_level = fitness_levels[0, 1, 2, 3]
    elif age >= 60:
        fitness_level = fitness_levels[0, 1, 2]
elif bmi >= 25 and bmi < 30:
    fitness_level = fitness_levels[1]
elif bmi >= 30:
    fitness_level = fitness_levels[0]
    
#save fitness level to a csv file and append each day column Fitness Level, Date, Age
fitness_level = pd.DataFrame({'Fitness Level': fitness_level, 'Date': datetime.date.today(), 'Age': age})
fitness_level.to_csv('fitness_level.csv', mode='a', header=True)

#use the fitness level to determine the workout routine
workout_routines = ['workout_1', 'workout_2', 'workout_3']
if fitness_level == fitness_levels[0]:
    workout_routine = workout_routines[0]
elif fitness_level == fitness_levels[1]:
    workout_routine = workout_routines[1]
elif fitness_level == fitness_levels[2]:
    workout_routine = workout_routines[2]
elif fitness_level == fitness_levels[3]:
    workout_routine = workout_routines[2]
elif fitness_level == fitness_levels[4]:
    workout_routine = workout_routines[2]
#save workout routine to a csv file and append each day column Workout Routine, Date, Age
workout_routine = pd.DataFrame({'Workout Routine': workout_routine, 'Date': datetime.date.today(), 'Age': age})
workout_routine.to_csv('workout_routine.csv', mode='a', header=True)

#use the workout routine to determine the exercises
exercises = ['Pull-ups', 'Push-ups', 'Sit-ups', 'Squats', 'Lunge Walk', 'Climbers']
if workout_routine == workout_routines[0]:
    exercise = exercises[0]
elif workout_routine == workout_routines[1]:
    exercise = exercises[1]
elif workout_routine == workout_routines[2]:
    exercise = exercises[2]
#save exercises to a csv file and append each day column Exercises, Date, Age
exercise = pd.DataFrame({'Exercises': exercise, 'Date': datetime.date.today(), 'Age': age})
exercise.to_csv('exercise.csv', mode='a', header=True)

#use the exercises to determine the repetitions and time
repetitions = []
time = []
if exercise == exercises[0]:
    repetitions = workout_data[0]['repetitions']
    time = workout_data[0]['time']
elif exercise == exercises[1]:
    repetitions = workout_data[1]['repetitions']
    time = workout_data[1]['time']
elif exercise == exercises[2]:
    repetitions = workout_data[2]['repetitions']
    time = workout_data[2]['time']
elif exercise == exercises[3]:
    repetitions = workout_data[3]['repetitions']
    time = workout_data[3]['time']
elif exercise == exercises[4]:
    repetitions = workout_data[4]['repetitions']
    time = workout_data[4]['time']
elif exercise == exercises[5]:
    repetitions = workout_data[5]['repetitions']
    time = workout_data[5]['time']
#save repetitions and time to a csv file and append each day column Repetitions, Time, Date, Age
exercise = pd.DataFrame({'Repetitions': repetitions, 'Time': time, 'Date': datetime.date.today(), 'Age': age})
exercise.to_csv('exercise.csv', mode='a', header=True)


#use the repetitions and time to determine the workout
workout = []
if repetitions > 0:
    workout = repetitions
elif time > 0:
    workout = time
#save workout to a csv file and append each day column Workout, Date, Age
workout = pd.DataFrame({'Workout': workout, 'Date': datetime.date.today(), 'Age': age})
workout.to_csv('workout.csv', mode='a', header=True)


# Create a function to generate a workout routine
def generate_workout(fitness_level):
    #implement the reinforcement learning model
    model = tf.keras.models.load_model('model.h5')
    # Load the data
    data = pd.read_csv('data.csv')
    # Create the training data
    X = data.drop('workout', axis=1)
    y = data['workout']
    # Fit the model
    model.fit(X, y, epochs=100, verbose=0)
    # Save the model
    model.save('model.h5')
    # Create a list of exercises
    exercises = ['Pull-ups', 'Push-ups', 'Sit-ups', 'Squats', 'Lunge Walk', 'Climbers']
    # Create a list of fitness levels
    fitness_levels = ['beginner', 'intermediate', 'advanced', 'expert', 'elite']
    # Create a list of workout routines
    workout_routines = ['workout_1', 'workout_2', 'workout_3']
    # Create a list of repetitions
    repetitions = [25, 50, 75, 100, 125, 150]
    # Create a list of times
    times = [120, 180, 240, 300, 360, 420]
    # Create a list of dictionaries
    workout_data = []
    # Create a dictionary
    workout_dict = {}
    # Create a for loop to iterate through the exercises
    for exercise in exercises:
            
            # Create a for loop to iterate through the fitness levels
            for fitness_level in fitness_levels:
                # Create a for loop to iterate through the workout routines
                for workout_routine in workout_routines:
                    # Create a for loop to iterate through the repetitions
                    for repetition in repetitions:
                        # Create a for loop to iterate through the times
                        for time in times:
                            # Create a dictionary
                            workout_dict = {}
                            # Add the exercise to the dictionary
                            workout_dict['exercise'] = exercise
                            # Add the fitness level to the dictionary
                            workout_dict['fitness_level'] = fitness_level
                            # Add the workout routine to the dictionary
                            workout_dict['workout_routine'] = workout_routine
                            # Add the repetitions to the dictionary
                            workout_dict['repetitions'] = repetition
                            # Add the time to the dictionary
                            workout_dict['time'] = time
                            # Append the dictionary to the list
                            workout_data.append(workout_dict)
    # Create a dataframe
    workout_df = pd.DataFrame(workout_data)
    # Create a list of columns
    columns = ['exercise', 'fitness_level', 'workout_routine', 'repetitions', 'time']
    # Create a list of values
    values = [exercise, fitness_level, workout_routine, repetition, time]
    # Create a dictionary
    workout_dict = {}
    # Create a for loop to iterate through the columns
    for column in columns:
        # Create a for loop to iterate through the values
        for value in values:
            # Add the column to the dictionary
            workout_dict[column] = value
    # Create a dataframe
    workout_df = pd.DataFrame(workout_dict, index=[0])
    # Create a list of columns
    columns = ['exercise', 'fitness_level', 'workout_routine', 'repetitions', 'time']
    # Create a list of values
    values = [exercise, fitness_level, workout_routine, repetition, time]
    # Create a dictionary
    workout_dict = {}
    # Create a for loop to iterate through the columns
    for column in columns:
        # Create a for loop to iterate through the values
        for value in values:
            # Add the column to the dictionary
            workout_dict[column] = value

    # Return the workout routine as a list of dictionaries
    return workout_data

    pass

  
  


app = Flask(__name__)

@app.route("/home")
def index():
    return render_template('index.html')

@app.route('/workout' , methods=['POST'])

def get_workout():
    fitness_level = request.json['fitness_level']
    workout = generate_workout(fitness_level)
    return jsonify(workout)

    #return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
