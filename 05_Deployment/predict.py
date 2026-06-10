
# Loading tha model

# In[ ]:


import pickle


# In[ ]:


model_file = 'model_C=1.0.bin'


# In[ ]:


with open(model_file, 'rb') as f_in:
    dv,model = pickle.load(f_in)


# In[ ]:


dv,model


# In[ ]:


# Using a new customer data 
customer = {
    'gender': 'Female',
    'seniorcitizen': 0,
    'partner': 'Yes',
    'dependents': 'No',
    'phoneservice': 'No',
    'multiplelines': 'No phone service',
    'internetservice': 'DSL',
    'onlinesecurity': 'No',
    'onlinebackup': 'Yes',
    'deviceprotection': 'No',
    'techsupport': 'No',
    'streamingtv': 'No',
    'streamingmovies': 'No',
    'contract': 'Month-to-month',
    'paperlessbilling': 'Yes',
    'paymentmethod': 'Electronic check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 29.85
}


# In[ ]:


X = dv.transform([customer])


# In[ ]:


model.predict_proba(X)[0,1]


# In[ ]:





