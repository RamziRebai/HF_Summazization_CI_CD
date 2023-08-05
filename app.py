from transformers import pipeline
import gradio as gr

summarizer = pipeline(
    "summarization", model="facebook/bart-large-cnn", framework="tf", truncation=True
)


def summarize(text):
    result = summarizer(text, min_length=10, max_length=100, truncation=True)
    return result[0]["summary_text"]


iface = gr.Interface(
    fn=summarize,
    inputs=gr.inputs.Textbox(lines=5, placeholder="Please put your text here..."),
    outputs="text",
)
iface.launch()
Manchester United bounced back from their defeats to Real Madrid and Borussia Dortmund with a 3-1 triumph over RC Lens at Old Trafford on Saturday afternoon.

After finding themselves 1-0 down at half-time, United turned the game on its head in dramatic fashion following the restart, scoring three goals in just 11 second half minutes to lead 3-1 by the hour-mark.

Marcus Rashford brought them level, latching onto a clever pass from Antony, before the Brazilian got in on the act himself to net his second goal in as many games. Casemiro then turned home United's third goal six minutes later after Rashford's header bounced off him and in.

United were dominant for long spells in the contest, producing some slick and eye-catching football at times. Alejandro Garnahco was particularly impressive on the left-wing.

Meanwhile, new signing Rasmus Hojlund was unveiled to the crowd ahead of kick-off. He has joined United on a five-year deal, featuring the option of an additional year.

The Reds, who face Wolves in their Premier League opener at Old Trafford a-week-on-Monday, face Spanish outfit Athletic Bilbao in Dublin tomorrow afternoon in what will be their eighth and final friendly of the summer.Manchester United bounced back from their defeats to Real Madrid and Borussia Dortmund with a 3-1 triumph over RC Lens at Old Trafford on Saturday afternoon.

After finding themselves 1-0 down at half-time, United turned the game on its head in dramatic fashion following the restart, scoring three goals in just 11 second half minutes to lead 3-1 by the hour-mark.

Marcus Rashford brought them level, latching onto a clever pass from Antony, before the Brazilian got in on the act himself to net his second goal in as many games. Casemiro then turned home United's third goal six minutes later after Rashford's header bounced off him and in.

United were dominant for long spells in the contest, producing some slick and eye-catching football at times. Alejandro Garnahco was particularly impressive on the left-wing.

Meanwhile, new signing Rasmus Hojlund was unveiled to the crowd ahead of kick-off. He has joined United on a five-year deal, featuring the option of an additional year.

The Reds, who face Wolves in their Premier League opener at Old Trafford a-week-on-Monday, face Spanish outfit Athletic Bilbao in Dublin tomorrow afternoon in what will be their eighth and final friendly of the summer.Manchester United bounced back from their defeats to Real Madrid and Borussia Dortmund with a 3-1 triumph over RC Lens at Old Trafford on Saturday afternoon.

After finding themselves 1-0 down at half-time, United turned the game on its head in dramatic fashion following the restart, scoring three goals in just 11 second half minutes to lead 3-1 by the hour-mark.

Marcus Rashford brought them level, latching onto a clever pass from Antony, before the Brazilian got in on the act himself to net his second goal in as many games. Casemiro then turned home United's third goal six minutes later after Rashford's header bounced off him and in.

United were dominant for long spells in the contest, producing some slick and eye-catching football at times. Alejandro Garnahco was particularly impressive on the left-wing.

Meanwhile, new signing Rasmus Hojlund was unveiled to the crowd ahead of kick-off. He has joined United on a five-year deal, featuring the option of an additional year.

The Reds, who face Wolves in their Premier League opener at Old Trafford a-week-on-Monday, face Spanish outfit Athletic Bilbao in Dublin tomorrow afternoon in what will be their eighth and final friendly of the summer.