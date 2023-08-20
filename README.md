# List of tasks from Hacker Rank
To access the website, click in this [link](https://www.hackerrank.com/dashboard)

## To create a python virtual environment and execute it
```sh
python -m venv .venv --upgrade-deps && source .venv/bin/activate
```

## Testing in local environment 
```sh
python -m doctest -f <directory_name>/<file_name>
```

## Example
```
    - name: Welcome
      if: always()
      run: |
        python -m doctest -f welcome.py 
```
```sh
python -m doctest -f week_1/time_conversion.py
```
