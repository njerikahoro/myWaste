import dash
import pickle
from dash import html, dcc, Input, Output, State


#loading the model
with open('model/waste_predictor.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


#initializing the dash app
app = dash.Dash(__name__)
server = app.server

# Defining the layout of the Dash ap
app.layout = html.Div([
    html.H1("Waste Prediction App", style={'color': 'blue', 'textAlign': 'center'}),
        html.H2("Enter values to predict waste",style={'color': 'blue'}),
    html.Div([
        html.Div([
            html.Label("Population:", style={'textAlign': 'center'}),
             html.Br(),
            dcc.Input(id='pop-input', type='number', placeholder='Population',  style={'height': '25px'})
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
            html.Label("Area:"),
             html.Br(),
            dcc.Input(id='area-input', type='number', placeholder='Area',  style={'height': '25px'})
        ], style={'margin-bottom': '10px'}),

        html.Div([
            html.Label("Population Density:"),
             html.Br(),
            dcc.Input(id='pden-input', type='number', placeholder='Population Density',  style={'height': '25px'})
        ], style={'margin-bottom': '10px'}),

        html.Div([
            html.Label("Weight per km2:"),
             html.Br(),
            dcc.Input(id='wden-input', type='number', placeholder='Weight per km2',  style={'height': '25px'})
        ], style={'margin-bottom': '10px'}),

        html.Div([
            html.Label("Urbanization Index:"),
             html.Br(),
            dcc.Input(id='urb-input', type='number', placeholder='Urbanization Index', style={'height': '25px'})
        ], style={'margin-bottom': '10px'}),

        html.Div([
            html.Label("Geographical Location:"),
             html.Br(),
            dcc.Input(id='geo-input', type='number', placeholder='Geographical Location',  style={'height': '25px'})
        ], style={'margin-bottom': '10px'}),

        html.Div([
            html.Label("Km of roads within the municipality:"),
             html.Br(),
            dcc.Input(id='roads-input', type='number', placeholder='Km of roads within the municipality',  style={'height': '25px'})
        ], style={'margin-bottom': '10px'}),

        html.Div([
            html.Label("Municipal Revenues:"),
             html.Br(),
            dcc.Input(id='gdp-input', type='number', placeholder='Municipal Revenues',  style={'height': '25px'})
        ], style={'margin-bottom': '10px'}),

        html.Div([
            html.Label("People per km of roads:"),
             html.Br(),
            dcc.Input(id='proads-input', type='number', placeholder='People per km of roads',  style={'height': '25px'})
        ], style={'margin-bottom': '10px'}),

        html.Div([
            html.Label("Taxable income:"),
             html.Br(),
            dcc.Input(id='wage-input', type='number', placeholder='Taxable income',  style={'height': '25px'})
        ], style={'margin-bottom': '10px'}),


        html.Div([
            html.Label("Municipal revenues:"),
             html.Br(),
            dcc.Input(id='finance-input', type='number', placeholder='Municipal revenues', style={'height': '25px'})
        ], style={'margin-bottom': '10px'}),
        
        html.Button('Predict', id='predict-btn', style={'height': '25px'}),
    ]),
    html.Div(id='prediction-output'),
    # Store component to hold input values
    dcc.Store(id='input-store', data={}),

],
        
                      style={'backgroundColor': '#2ac97f', 'padding': '20px'})


# Define=ining a callback function to predict waste
@app.callback(
    Output('prediction-output', 'children'),
    [Input('predict-btn', 'n_clicks')],
    [Input('pop-input', 'value'),
     Input('area-input', 'value'),
     Input('pden-input', 'value'),
     Input('wden-input', 'value'),
     Input('urb-input', 'value'),
     Input('geo-input', 'value'),
     Input('roads-input', 'value'),
     Input('gdp-input', 'value'),
     Input('proads-input', 'value'),
     Input('wage-input', 'value'),
     Input('finance-input', 'value')]
)
def predict_waste(n_clicks, pop, area, pden, wden, urb, geo, roads, gdp, proads, wage, finance):
    if n_clicks is None:
        return "Enter values to predict waste"
    
    # Including all variables in order
    input_features = [[pop, area, pden, wden, urb, geo, roads, gdp, proads, wage, finance]]
    prediction = model.predict(input_features)
    
    return f'Predicted Waste: {prediction[0]}'


# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)
