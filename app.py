#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Let's load the model from week 4


# In[2]:


import pickle


# In[3]:


# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


# In[4]:


model


# In[5]:


#Our model is loaded successfully!


# In[6]:


#Now let's use the Flask API to deploy the model


# In[7]:


#pip install Flask


# In[9]:


from flask import Flask, request, jsonify


# In[10]:


app = Flask(__name__)


# In[11]:


app


# In[12]:


import numpy as np


# In[13]:


# API route for model predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    input_data = np.array(data['input']).reshape(1, -1)
    prediction = model.predict(input_data)
    return jsonify({'prediction': int(prediction[0])})


# In[14]:


# Main entry point to run the app
if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




