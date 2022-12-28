#!/usr/bin/env python
# coding: utf-8

# In[23]:


#Install Packages
#!pip install dash==1.19.0
#!pip install jupyter dash
#!pip install pandas

#Import required libraries
import pandas as pd
import numpy as np
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px
from jupyter_dash import JupyterDash
import plotly.graph_objects as go
from dash import no_update

#Create a dash application
#app = dash.Dash(__name__)
#Further you need to change app=dash.Dash(__name__)
app = JupyterDash(__name__)
#app.layout = html.Div([...])
#app.run_server(mode='inline')

#Change your last line if __name__ == '__main__'
if __name__ == '__main__':
    app.run_server(mode='jupyterlab', port = 8050 ,dev_tools_ui=True, dev_tools_hot_reload =True, threaded=True)#debug=True

#Read the airline data into pandas dataframe
spacex_df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
#TASK 1: Add a dropdown list to enable Launch Site selection
#The default select value is for ALL sites
# dcc.Dropdown(id='site-dropdown',...)
dcc.Dropdown(id='site-dropdown',
             options=[
                 {'label': 'All Sites', 'value': 'ALL'},
                 {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                 {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                 {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                 {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
                ],
            value='ALL',
            placeholder='Select a Launch Site here',
            searchable=True,
            style={'width':'80%','padding':'3px','font-size':'20px','text-align-last':'center'}
             ),
                                                                
html.Br()
                                
#TASK 2: Add a callback function to render success-pie-chart basead on selected site dropdown
                                
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
                                
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(data, values='class',
        names='pie chart names',
        title='title')
        return fig
    else:
        # return the outcomes piechart for a selected site
        df_site_filtered=spacex_df[spacex_df['Launch Site'] == site]
        filtered_df = spacex_df['Launch Site'] == site_dropdown]
        df1=filtered_df.goupby(['Launch Site', 'class']).size().reset_indindex(name='class count')
        fig=px.pie(df1, values='class',names='Launch Sites', title='Success Count For' + site)
        return fig
                           
             
    
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
#                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])



# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output


# Run the app
if __name__ == '__main__':
    app.run_server()


# In[ ]:




