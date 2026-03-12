It's a Task Scheduler program! But currently it just read tasks from different sources and use duck typing to organize reading from this different sources.

# Project structure

 <pre>
    .
    ├── task_scheduler
    │   ├── .task_scheduler_log                # log folder
    │       ├── task_scheduler.log             # log file
    │   ├── src/                               # Source code
    │       ├── common/                        # config files
    │            ├──__init__.py                #
    │            ├──config.py                  # logger configuration
    │       ├── contracts/                     # contracts files
    │            ├── __init__.py               #
    │            ├──task_source.py             # task contract
    │       ├── infrastructure/                # infrastructure elements
    │            ├── __init__.py               #
    │            ├── constants.py              # contains constants
    │            ├── logger.py                 # logger initialization
    │       ├── models/                        # data models
    │            ├── __init__.py               #
    │            ├── task.py                   # task dataclass
    |       ├── services/                      # actual services
    │            ├── __init__.py               #
    │            ├── task_receiver.py          # service for receiving and displaying tasks
    |       ├── sources/                       # functions for processing task sources
    │            ├── __init__.py               #
    │            ├── api_sources.py            # functions for processing API task sources
    │            ├── file_sources.py           # functions for processing file task sources
    │            ├── generate_sources.py       # functions for generating task sources
    |       ├── __init__.py                    #
    |       ├── main.py                        # It's a main file!
    │   ├── tasks_sources/                     # folder for task source files
    │   ├── tests/                             # unit tests
    │   ├── .gitignore                         # git ignore files
    │   ├── .pre-commit-config.yaml            # code-style check
    │   ├── pyproject.toml                     # project configuration
    │   ├── README.md                          # report with a project description
</pre>

# Set up
To use this project you need to download it. Then you can run it from the project root with your terminal with:
```
python -m src.main
```

## Tests
To ran tests you need to have pytest, pytest-cov.
To activate tests use:
```
python -m pytest
```

# How it works
Service 'task_receiver.py' use duck typing to handle different task sources. This sources are:
- API sources
- File sources
- Generated sources
They are described and stored in a separate folder. All of them have get_tasks() method, that is called by the task_receiver service to retrieve tasks without thinking about how it will do it.

All tasks are stored in the same format that is determined by the task dataclass. And contract determine how this tasks will be processed.
