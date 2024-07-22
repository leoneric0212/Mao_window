from dash import Dash, dcc , html, Input, Output, callback

externam_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app=Dash(__name__,external_stylesheets=externam_stylesheets)

all_options={
    '美國':['New York City','San Fransico', 'Cincinnati'],
    '加拿大':['Montreal','Toronto','Ottawa']
}

app.layout=html.Div([
    dcc.RadioItems(
        list(all_options.keys()),
        '美國',
        id='countries-radio'
    ),
    html.Hr(),      #畫橫線
    dcc.RadioItems(id='cities-radio'),
    html.Div(id='display_selected_value')
])

@callback(
    Output('cities-radio','options'),
    Input('countries-radio','value')
)
def city_selected (selected_country:str):
    return [{'label':i,'value':i} for i in all_options[selected_country]]

@callback(
        Output('cities-radio','value'),
        Input('cities-radio','options')
)
def set_cities_value(available_options):
    return available_options[0]['value']

@callback(
    Output('display_selected_value','children'),
    Input('countries-radio','value'),
    Input('cities-radio','value')
)    

def set_display_children(selected_country,selected_city):
    return f'所選擇的是{selected_country}的{selected_city}城'


if __name__=='__main__':
    app.run(debug=True)