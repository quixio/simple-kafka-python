import logging
from quixstreams import Application
from uuid import uuid4
from datetime import timedelta
import pygsheets


def initializer_fn(msg):
    temperature = msg["current"]["temperature_2m"]

    return {
        "open": temperature,
        "high": temperature,
        "low": temperature,
        "close": temperature,
    }


def reducer_fn(summary, msg):
    temperature = msg["current"]["temperature_2m"]

    return {
        "open": summary["open"],
        "high": max(summary["high"], temperature),
        "low": min(summary["low"], temperature),
        "close": temperature,
    }


def main():
    app = Application(
        broker_address="localhost:9092",
        loglevel="DEBUG",
        consumer_group="weather_to_google",
        auto_offset_reset="earliest",
    )

    input_topic = app.topic("weather_data_demo")

    sdf = app.dataframe(input_topic)

    # sdf = sdf.group_into_hourly_batches(...)
    sdf = sdf.tumbling_window(duration_ms=timedelta(hours=1))

    # sdf = sdf.summarize_that_hour(...)
    sdf = sdf.reduce(
        initializer=initializer_fn,
        reducer=reducer_fn,
    )
    sdf = sdf.final()

    sdf = sdf.update(lambda msg: logging.debug("Got: %s", msg))

    google_api = pygsheets.authorize()
    workspace = google_api.open("Weather Sheet")
    sheet = workspace[0]
    sheet.update_values(
        "A1",
        [
            [
                "Start",
                "End",
                "Open",
                "High",
                "Low",
                "Close",
                "Date",
            ]
        ],
    )

    def to_google(msg):
        sheet.insert_rows(
            1,
            values=[
                msg["start"],
                msg["end"],
                msg["value"]["open"],
                msg["value"]["high"],
                msg["value"]["low"],
                msg["value"]["close"],
                "=EPOCHTODATE(A2 / 1000)",
            ],
        )

    sdf = sdf.apply(to_google)

    app.run(sdf)


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    main()
