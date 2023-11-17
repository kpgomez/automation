import os
import shutil

from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table


# automate the creation of a folder <- this is os mkdir
def create_folder(folder_name):
    os.mkdir(folder_name)
    console.print(f"[bold underline green]{folder_name}[/bold underline green] successfully created")


# handle a deleted user by moving user documents into a temporary folder <- this is shutil move
def delete_user(user_name):
    pass
    # need name of user
    # create temp folder
    # move contents of deleted user


# sort documents into appropriate folder according to their document type (ext) <- os.path.splitext()
def sort_documents():
    pass


# parse a log file for errors and warnings, create new log file, separated by type in target directory <- use re
def organize_files():
    pass


# main entry-point, application driver
def main():
    # create a menu-driven application
    while True:
        console.print(
            "\n----- [bold underline]MAIN MENU[/bold underline] ------"
            "\n1. [bold green]Create[/bold green] a new folder"
            "\n2. [bold red]Delete[/bold red] a user"
            "\n3. [bold blue]Sort[/bold blue] documents"
            "\n4. [bold magenta]Organize[/bold magenta] log files"
            "\n5. [bold yellow]Exit[/bold yellow] system"
        )
        choice = Prompt.ask(
            "\n[bold violet]Selection[/bold violet]",
            choices=["1", "2", "3", "4", "5"],
            default="5",
            show_choices=False,
            show_default=False,
        )

        if choice == "1":
            while True:
                folder_name = Prompt.ask("Enter [bold green]NAME[/bold green] of new folder [italic]or [bold green](r)"
                                         "[/bold green]eturn to main menu[/italic]")
                if folder_name == "r":
                    break
                else:
                    confirmation = Prompt.ask(f"You entered [bold underline green]{folder_name}[/bold underline green]."
                                              f"\nIs this correct? Enter (y)es or (n)o.")
                    if confirmation == "y":
                        # check if folder already exists in current directory
                        current_dir = os.listdir(".")  # list of strings
                        if folder_name in current_dir:
                            console.print("Please enter a [bold red]different[/bold red] name as the folder "
                                          "you specified already exists")
                            continue
                        else:
                            create_folder(folder_name)
                            break
                    else:
                        continue

        elif choice == "2":
            # get path
            current_dir = os.getcwd()
            path = "assets/user-docs"
            full_path = os.path.join(current_dir, path)

            # list users
            current_users = os.listdir(full_path)  # need to locate absolute path for assets/user-docs
            user_table = Table(show_header=True, header_style="bold blue")
            user_table.add_column("Name", style="dim", width=20)
            user_table.add_column("Contents")

            # populate table
            for user in current_users:
                user_table.add_row(user, str(os.listdir(os.path.join(full_path, user))))

            # show table
            console.print(user_table)

            while True:
                # select user
                user_name = Prompt.ask("Which user would you like to [bold red]delete?[/bold red]")
                if user_name in current_users:
                    delete_user(user_name)
                else:
                    console.print("User not found")
                    continue

        elif choice == "3":
            sort_documents()

        elif choice == "4":
            organize_files()

        else:
            break


if __name__ == "__main__":
    console = Console()
    main()
