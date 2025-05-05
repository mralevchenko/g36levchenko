import logging
import typer
from rich.console import Console
from rich.table import Table
from pathlib import Path
from typing import Any, Annotated

from todo.model import Todo
from todo.todos import TodoList
from todo import __app_name__, __version__, TITLE, ERRORS
from todo import db, config, todos, helpers
from todo.helpers import add_your_task, hello, make_your_choice, bye, help_me, choose_category

# Налаштування логування
logging.basicConfig(
    filename="todo.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = typer.Typer()
console = Console()
header = Todo.make_header()

def show(tasks: Any) -> None:
    table = Table(show_header=True, header_style="bold blue")
    for item in header:
        table.add_column(item['name'], style=item['style'], width=item['width'], min_width=item['min_width'], justify=item['justify'])

    for index, task in enumerate(tasks, start=1):
        c = Todo.get_category_color(task['category'])
        is_done = Todo.DONE if task['status'] == 2 else Todo.PENDING
        table.add_row(str(index), task['task'], f'[{c}]{task["category"]}[/{c}]', is_done)

    console.print(table)

def get_todo_list() -> todos.TodoList:
    if config.CONFIG_FILE_PATH.exists():
        db_path = db.get_database_path(config.CONFIG_FILE_PATH)
    else:
        typer.secho('Config file not found. Please, run "todo init"', fg=typer.colors.RED)
        logger.error("Config file not found.")
        raise typer.Exit(1)

    if db_path.exists():
        return todos.TodoList(db_path)
    else:
        typer.secho('Database not found. Please, run "todo init"', fg=typer.colors.RED)
        logger.error("Database file not found.")
        raise typer.Exit(1)

@app.command()
def init(
    db_path: Annotated[str, typer.Option("--db-path", "-db", prompt="to-do database location?")] = str(db.DEFAULT_DB_FILE_PATH),
) -> None:
    app_init_error = config.init_app(db_path)

    if app_init_error:
        typer.secho(f"Creating config file failed with {ERRORS[app_init_error]}", fg=typer.colors.RED)
        logger.error(f"Creating config failed: {ERRORS[app_init_error]}")
        raise typer.Exit(1)

    db_init_error = db.init_database(Path(db_path))
    if db_init_error:
        typer.secho(f"Creating database failed with {ERRORS[db_init_error]}", fg=typer.colors.RED)
        logger.error(f"Creating database failed: {ERRORS[db_init_error]}")
        raise typer.Exit(1)

    typer.secho(f"The todo database is {db_path}", fg=typer.colors.GREEN)
    logger.info(f"Initialized todo database at {db_path}")

@app.command()
def run() -> None:
    hello()
    todo_list = get_todo_list()

    while True:
        match make_your_choice():
            case 'a':
                category = choose_category()
                task = add_your_task()
                current_todo, write_error = todo_list.add(task, category)

                if write_error:
                    typer.secho(f"Added task failed with {write_error}", fg=typer.colors.RED)
                    logger.error(f"Failed to add task '{task}' with error: {write_error}")
                    raise typer.Exit(1)

                typer.secho(f"Task {task} was added to todo database with {category}", fg=typer.colors.GREEN)
                logger.info(f"Task '{task}' was successfully added with category '{category}'")

            case 'l':
                tasks, error = todo_list.get_todo()
                if error:
                    typer.secho(f"Fetching tasks failed with {ERRORS[error]}", fg=typer.colors.RED)
                    logger.error(f"Failed to fetch tasks: {ERRORS[error]}")
                    raise typer.Exit(1)

                if len(tasks) == 0:
                    typer.secho("There are no tasks in the to-do list yet", fg=typer.colors.RED)
                    logger.info("Attempted to list tasks but list is empty")
                    raise typer.Exit()

                logger.info("Listed all tasks")
                show(tasks)

            case 'u':
                id = helpers.choose_id()
                tasks, error = todo_list.complete(id)
                if error:
                    logger.error(f"Failed to mark task {id} as complete: {ERRORS[error]}")
                else:
                    logger.info(f"Marked task {id} as complete")
                show(tasks)

            case 'r':
                id = helpers.choose_id()
                tasks, error = todo_list.delete(id)
                if error:
                    logger.error(f"Failed to delete task {id}: {ERRORS[error]}")
                else:
                    logger.info(f"Deleted task {id}")
                show(tasks)

            case 'q':
                logger.info("User exited application")
                bye(TITLE)
                break

            case _:
                help_me()
                logger.warning("User entered an unknown command")

