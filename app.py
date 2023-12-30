import dash
from dash import dcc, html, Input, Output, State


app = dash.Dash(
    __name__,
    external_stylesheets=[
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css",
        ]
)

app.layout = html.Div(
    [
        html.Div(
            html.Div(
                id='chat-output',
                children=[]
            ),
            className='outer'
            # ^^ this is for showing the latest answer on the bottom
        ),
        html.Div(
            dcc.Input(
                id='user-input',
                type='text',
                placeholder='Type your message...'
            ),
            style={
                "position": "absolute",
                "bottom": "0",
                "height": "20vh"
            }
        ),
    ]
)


@app.callback(
    Output('chat-output', 'children'),
    Input('user-input', 'n_submit'),
    State('user-input', 'value'),
    State('chat-output', 'children')
)
def chatbot_response(n_submit, user_input, chat_history):
    if user_input:
        chat_history.append(
            html.Div(
                children="You: " + user_input,
                className='usr message'
            )
        )

        # You can implement your chatbot logic here
        bot_response = "Bot: You said, '" + user_input
        chat_history.append(
            html.Div(
                bot_response,
                className='bot message'
            )
        )

    return chat_history


if __name__ == '__main__':
    app.run_server(debug=True)
