import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import gdocrevisions
from gdocrevisions.replay import RevisionReplayer
import os

# # Specify the service account credentials file
try:
    CREDENTIAL_FILE = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
except KeyError:
    raise Exception("GOOGLE_APPLICATION_CREDENTIALS environment variable was not detected")


# load the Doc Revisions data for the specified doc

FILE_ID = '1aSAA-ZA8bGvJSpgFhVgJu89EDMPMRm5IrcdeV85JmJE' # spark grant
gdoc = gdocrevisions.GoogleDoc(FILE_ID,keyfile=CREDENTIAL_FILE)
replayer = RevisionReplayer(gdoc)

app = dash.Dash()

app.layout = html.Div([
    dcc.Slider(
        id='revision-slider',
        min=1,
        max=len(gdoc.revisions), # updated on document change
        value=1, # updated on slider change
        step=1,
    ),
    dcc.Markdown(id='text-window', children='Loading document...'),
])


@app.callback(
    dash.dependencies.Output('text-window', 'children'),
    [dash.dependencies.Input('revision-slider', 'value')])
def update_text(revision_id):
    replayer.to_revision(revision_id)
    return replayer.content.render()


if __name__ == '__main__':
    app.run_server(host='0.0.0.0')
