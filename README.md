RabbitMQ-subprocess-client
=====================

RabbitMQ-subprocess-client is a RabbitMq client (based on `pika`) spawning tasks as subprocess, allowing handling segfault gracefully. 


# Install
```bash
pip install rabbitmq-subprocess-client
```

# usage
```python
import os
from concurrent.futures import TimeoutError
import traceback
from rabbitmq_subprocess_client import Runner, Consumer

class MyConsumer(Consumer):
    def consume_main(self, basic_deliver, msg):
        print(f'pre-processing message: {msg} in process: {os.getpid()}')
        try:
            args = []
            self.exec(msg, *args)  # This will run the consume_subprocess method in a subprocess
            self.acknowledge_message(basic_deliver.delivery_tag)
        except TimeoutError:
            self.nacknowledge_message(basic_deliver.delivery_tag)
        except BaseException:
            exc_msg = traceback.format_exc()
            print(exc_msg)
            self.nacknowledge_message(basic_deliver.delivery_tag)

    @staticmethod
    def consume_subprocess(msg, *args):
        print(f'processing message: {msg} in process: {os.getpid()}')

worker = Runner('my_queue', MyConsumer)
worker.run()
```

    
# develop
```bash
poetry shell
poetry install
pytest
pre-commit install
```

# Publish new version
```bash
poetry publish --build --username= --password=
```
