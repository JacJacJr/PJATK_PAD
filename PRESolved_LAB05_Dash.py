from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

df_row=pd.read_excel('winequelity.xlsx')
df= df_row.drop(columns = df_row.columns[0::])

col_list= []
for i in df.columns:
    col_list.append(str(i))
    
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app = Dash(__name__)

app.layout = html.Div([
    html.Div(
        html.H4(children="Data_set"),
        generate_table(df)),
    html.H4('Choose the plot type:')
    dcc.RadioItems(
            ['Regression', 'Classification'], 'Regression',
            id='proces_type',
            inline=True
        ),
    dcc.Dropdown(
        col_list, 
        'Choose column for processing', 
        id='y_column'),
   dcc.Graph(id='plot')
])

#tego niestety bez wizualizacji nie jestem w stanie odgadnąć
#wiem że muszę skorzystać z poniższych i wskazać odpowiedni wykres
@app.callback(
    Output('graph', 'figure'),
    Input('y_column', 'value'),
    Input('proces_type', 'value'),
 
def print_graph(y_column, proces_type):
    if proces_type == 'Regression':
        fig = px.scatter(x=df['pH'], y=df[y_column])
        return fig
    elif proces_type == 'Classification':
        #bez wizualizacji niestety też najprostszy klasyfkator knn 
        # byłby bezcelowy, więc to też muszę oddać walkowerem
        pass
if __name__ == '__main__':
    app.run_server(debug=True)