import hashlib
import time
import shelve

from . import helpers, monit, monitor, DATABASE, TITLE

def main():
    helpers.hello(TITLE)

    files = {}

    try:
        while True:
            for file in monit.getFiles(monitor):
                hash = hashlib.sha256()
                try:
                    with open(file, "rb") as f:
                        for chunk in iter(lambda: f.read(2048), b""):
                            hash.update(chunk)
                    sha256 = hash.hexdigest()

                    if file in files and sha256 != files[file]:
                        print(f'{file} has been changed! {time.strftime("%Y-%m-%d %H:%M:%S")}')

                    files[file] = sha256
                    with shelve.open(DATABASE) as s:
                        s[file] = files[file]

                except Exception as e:
                    print(f"Error reading {file}: {e}")

            time.sleep(1)

    except KeyboardInterrupt:
        helpers.bye(TITLE)

if __name__ == "__main__":
    main()
