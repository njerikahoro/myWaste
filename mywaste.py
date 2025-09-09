import dash
import pickle
from dash import html, dcc, Input, Output, State

# Initializing the dash app
app = dash.Dash(__name__)

# Loading the model
with open('waste_predictor.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Assigning the server attribute
server = app.server

# Defining the layout of the Dash app
app.layout = html.Div([
    html.H1("Waste Prediction App", style={'color': 'blue', 'textAlign': 'center'}),
        html.H2("Enter values to predict waste",style={'color': 'blue'}),
    html.Div([
        # Input fields...
    ]),
    html.Div(id='prediction-output'),
    # Store component to hold input values
    dcc.Store(id='input-store', data={}),
],
        
style={'backgroundColor': '#2ac97f', 'padding': '20px'})

# Callback function to predict waste
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
    app.run_server(debug=True)
