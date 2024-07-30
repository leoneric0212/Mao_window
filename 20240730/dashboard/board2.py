from dash import Dash, dcc, html, Input, Output, callback,dash_table
import pandas as pd
import data

app2=Dash(__name__,requests_pathname_prefix='/dashboard/app2/')
app2.title="U敗"

areas=[tup[0] for tup in data.get_areas()]
app2.layout=html.Div([
        dcc.Dropdown(
            options=areas,
            value=areas[0],
            id='areas'),
        html.Hr(),
        dash_table.DataTable(id='sites_table')
    ])
@callback(
    Output('sites_table','data'),
    Input('areas','value')
)
def area_select(areas_value):
    content=data.get_snaOfArea(area=areas_value)
    df=pd.DataFrame(content)
    df.columns=['站點名稱','總數','可借','可還','資料時間']
    return df.to_dict('records')
    