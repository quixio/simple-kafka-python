# Python and Kakfa with QuixStreams

Supporting code for our [step-by-step coding walkthroughs][youtube-playlist].

# A Simple Producer

[![YouTube Producer Video Thumbnail](producer_thumbnail.png?raw=true)][youtube-producer]
There's a complete [walkthrough video here][youtube-producer]. To run the code in this repo:

```sh
# Set up an environment.
cd send_to_kafka
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# Run the producer.
python3 main.py
```

# A Simple Consumer

[![YouTube Consumer Video Thumbnail](consumer_thumbnail.jpg?raw=true)][youtube-consumer]
There's a complete [walkthrough video here][youtube-consumer]. To run the code in this repo:

```sh
# Set up an environment.
cd read_from_kafka
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# Run the consumer.
python3 main.py
```

# A Simple Processor

[![YouTube Processor Video Thumbnail](processor_thumbnail.png?raw=true)][youtube-processor]
There's a complete [walkthrough video here][youtube-processor]. To run the code in this repo:

```sh
# Set up an environment.
cd weather_processor
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# Run the stream processor.
python3 main.py
```

# Stream Processing to Google Spreadsheets

[![YouTube Kafka To Google Video
Thumbnail](kafka_to_google_thumbnail.jpg?raw=true)][youtube-kafka-to-google]There's
a complete [walkthrough video here][youtube-kafka-to-google].

To run the code in this repo, you'll first need to  create a Google Developer
client API key file, using the [Google Developer
Console][google-developer-console]. Copy that `client_secret.json` file it
gives you into the `weather_to_google` directory. Then:

```sh
# Set up an environment.
cd weather_to_google
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# Run the stream processor.
python3 main.py
```

[youtube-producer]: https://youtu.be/D2NYvGlbK0M
[youtube-consumer]: https://youtu.be/eCsSAzTy5cE
[youtube-processor]: https://youtu.be/5sqegy_EPa0
[youtube-kafka-to-google]: https://youtu.be/Haeub0XvuBU
[youtube-playlist]: https://www.youtube.com/playlist?list=PL5gMntduShmyJd2fsflN1jwLW9XtDMFAX
[google-developer-console]: https://console.cloud.google.com/
