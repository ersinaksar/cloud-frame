import solara
import requests

clicks = solara.reactive(0)
day = solara.reactive("")
month = solara.reactive("")
year = solara.reactive("")
hour = solara.reactive("")
minute = solara.reactive("")
location = solara.reactive("")


@solara.component
def Page():
    color = "green"
    if clicks.value >= 5:
        color = "red"

    def increment():
        clicks.value += 1
        print("clicks", clicks)  # noqa

    def reset():
        clicks.value = 0
        print("clicks reset")  # noqa

    def submit():
        data = {
            "day": day.value,
            "month": month.value,
            "year": year.value,
            "hour": hour.value,
            "minute": minute.value,
            "location": location.value
        }
        response = requests.post("http://localhost:8000/submit", json=data)
        print("Response:", response.json())

    label = "Not clicked yet" if clicks.value == 0 else f"Clicked: {clicks.value}"

    with solara.Column():
        solara.Button(label=label, on_click=increment, color=color)
        solara.Button(label="Reset", on_click=reset, color="blue")
        solara.Text(f"Click count: {clicks.value}")
    with solara.Column():
        solara.InputText(label="Day", value=day)
        solara.InputText(label="Month", value=month)
        solara.InputText(label="Year", value=year)
        solara.InputText(label="Hour", value=hour)
        solara.InputText(label="Minute", value=minute)
        solara.InputText(label="Location", value=location)
        solara.Button(label="Submit", on_click=submit, color="green")
