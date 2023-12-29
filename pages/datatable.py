import pyodbc 
import pandas as pd
import dash
from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='Table')

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-HIMARY\SQLEXPRESS;'
                       'Database=SbonDB;'
                      'Trusted_Connection=yes;')

df = pd.read_sql_query('SELECT ACTION_CODE, PROC_CODE_ID, NAME FROM dbo.RB_CLASSIFIER', conn)

layout = dash_table.DataTable(df.to_dict('records'),
                                  [{"name": i, "id": i} for i in df.columns],
                                  filter_action="native",
                                  fixed_rows={ 'headers': True, 'data': 0 },
                                  style_cell={'textAlign': 'left'},
                                  #style_as_list_view=True,
                                  style_header={'fontWeight': 'bold',
                                                'backgroundColor': 'rgb(133, 20, 75)',
                                                'color': 'white'}, 
                                  style_data={'color': 'white',
                                              'backgroundColor': 'rgb(50, 50, 50)'
                                             }                                                                                                
                                  )

