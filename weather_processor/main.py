import logging
from quixstreams import Application


def main():
    logging.info("START")
    app = Application(
        broker_address="localhost:9092",
        loglevel="DEBUG",
        auto_offset_reset="earliest",
        consumer_group="weather_processor",
    )

    input_topic = app.topic("weather_data_demo")
    output_topic = app.topic("weather_i18n")

    def i18n_weather(msg):
        celcius = msg["current"]["temperature_2m"]
        fahrenheit = (celcius * 9 / 5) + 32
        kelvin = celcius + 273.15

        new_msg = {
            "celcius": celcius,
            "fahrenheit": round(fahrenheit, 2),
            "kelvin": round(kelvin, 2),
        }

        logging.debug("Returning: %s", new_msg)

        return new_msg

    sdf = app.dataframe(input_topic)
    sdf = sdf.apply(i18n_weather)
    sdf = sdf.to_topic(output_topic)

    app.run(sdf)


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    main()
