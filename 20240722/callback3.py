from dash import Dash,html,dcc,Input,Output,callback

externam_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# print(externam_stylesheets)

app = Dash(__name__,external_stylesheets=externam_stylesheets)
app.layout=html.Div([
    dcc.Input(
        id='num-multi',
        type='number',
        value=5
    ),
    html.Table([
        html.Tr([html.Td(['x',html.Sup(2)]),
                 html.Td(id='square')]), #Sup為對數
        html.Tr([html.Td(['x',html.Sup(3)]),
                 html.Td(id='cube')]),
        html.Tr([html.Td(['2',html.Sup('x')]),
                 html.Td(id='twos')]),
        html.Tr([html.Td(['3',html.Sup(3)]),
                 html.Td(id='three')]),
        html.Tr([html.Td(['x',html.Sup('x')]),
                 html.Td(id='x^x')])
    ])])

@callback(
    Output('square','children'),
    Output('cube','children'),
    Output('twos','children'),
    Output('three','children'),
    Output('x^x','children'),
    Input('num-multi','value')
)
def whatevername(x:int) -> tuple:
    return x**2,x**3,2**2,3**3,x**x




if __name__=="__main__":
    app.run(debug=True)