from datetime import datetime


def test_calls_correct_function():
    task_template = {
        "name": "convert_date",
        "function": {
            "name": "datetime.datetime.strptime",
            "default_args": {"format": "%Y-%m-%d"}
        },
        "input": [{"name": "date_str"}],
        "output": [{"name": "input_date"}]
    }
    #
    # task = create_task(task_template)
    #
    # assert task("2021-02-01") == datetime(year=2021, month=2, day=1)
