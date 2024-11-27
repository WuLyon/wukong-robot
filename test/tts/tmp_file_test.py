import tempfile
from time import sleep

message = "Hello, Lyon!"
with tempfile.NamedTemporaryFile(delete=True, mode='w', suffix='.txt') as f:
    f.write(message)
    file_path = f.name
    print(file_path)
    sleep(10)

