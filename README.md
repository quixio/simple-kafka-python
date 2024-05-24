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

[youtube-producer]: https://youtu.be/D2NYvGlbK0M
[youtube-consumer]: https://youtu.be/eCsSAzTy5cE
[youtube-processor]: https://youtu.be/5sqegy_EPa0
[youtube-playlist]: https://www.youtube.com/playlist?list=PL5gMntduShmyJd2fsflN1jwLW9XtDMFAX

