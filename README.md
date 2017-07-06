# Demo dash app using gdocrevisions

## Dependencies
* [dash](https://github.com/plotly/dash)
* [gdocrevisions](https://github.com/harvard-vpal/gdocrevisions)

## Setup

### Create google service account credentials
Guide: https://developers.google.com/identity/protocols/OAuth2ServiceAccount

### Clone app and setup environment

```
git clone https://github.com/kunanit/dash-gdoc
# set location to json credentials as envrionment variable
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json
# run the dash app
python gdoc_slider.py
```
Then open `localhost:8050` in a browser to see the app.
