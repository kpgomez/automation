import os
import shutil

from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table


# automate the creation of a folder <- this is os mkdir
def create_folder(folder_name):
    current_dir = os.listdir(".")  # list of strings
    if folder_name in current_dir:
        console.print("Please enter a [bold red]different[/bold red] name as the folder "
                      "you specified already exists")
        return
    else:
        os.mkdir(folder_name)
        console.print(f"[bold underline green]{folder_name}[/bold underline green] successfully created")


def show_users(display: str):
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
    console.print(f"List of [bold]CURRENT[/bold] {display}s", user_table)
    return current_users


# handle a deleted user by moving user documents into a temporary folder <- this is shutil move
def delete_user(user_name):
    # create temporary folder
    os.makedirs("inactive-users", exist_ok=True)

    # get path
    current_dir = os.getcwd()
    path = "assets/user-docs/"
    full_path = os.path.join(current_dir, path, user_name)

    # move deleted_user to folder
    shutil.move(full_path, "inactive-users")
    show_users()


# sort documents into appropriate folder according to their file type (ext) <- os.path.splitext()
# shutil (shell utilities) lets you move copy, move, rename, and delete files
def sort_documents(folder: str):
    # find directory by folder name, example is root/assets/user-docs/folder
    current_dir = os.getcwd()
    path = "assets/user-docs/"
    root_dir = os.path.join(current_dir, path, folder)
    print('root_dir', root_dir)

    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            # print("subdir", subdir)
            # print("dirs", dirs)
            # print("file", file)
            # name_of_file = file.find(".")
            # print(os.path.join(subdir, file))
            root, ext = os.path.splitext(file)
            if ext == ".log":
                print("cwd", os.getcwd())
                # os.makedirs("logs", exist_ok=True)
                # new_folder = os.path.join(root_dir, file)
                # shutil.move(new_folder, "logs")
            elif ext == ".mail":
                pass
            elif ext == ".txt":
                pass
            print(f"Root of the file path: {root}")
            print(f"Ext of the file path: {ext}")

            # make folders for each file type/ext specifically move log files into logs folder and
            # email files in mail folder
            # iterate through the folders
            # move folders to corresponding file type


# parse a log file for errors and warnings, create new log file, separated by type in target directory <- use re
def organize_files():
    ...


def rename_file():
    ...


# main entry-point, application driver
def main():
    # create a menu-driven application
    while True:
        console.print(
            "\n----- [bold underline]MAIN MENU[/bold underline] ------"
            "\n1. [bold gold3]Create[/bold gold3] a new folder"
            "\n2. [bold red]Delete[/bold red] a user"
            "\n3. [bold blue]Sort[/bold blue] documents"
            "\n4. [bold magenta]Organize[/bold magenta] log files"
            "\n5. [bold dark_orange]Rename[/bold dark_orange] file"
            "\n6. [bold yellow]Exit[/bold yellow] system"
        )
        choice = Prompt.ask(
            "\n[bold violet]Selection[/bold violet]",
            choices=["1", "2", "3", "4", "5", "6"],
            default="6",
            show_choices=False,
            show_default=False,
        )

        if choice == "1":
            while True:
                folder_name = Prompt.ask("Enter [bold green]NAME[/bold green] of new folder [italic]or "
                                         "[bold green](r)[/bold green]eturn to main menu[/italic]")
                if folder_name == "r":
                    break
                else:
                    confirmation = Prompt.ask(f"You entered [bold underline green]{folder_name}[/bold underline green]."
                                              f"\nIs this correct? Enter (y)es or (n)o or (r)eturn to main menu")
                    if confirmation == "y":
                        create_folder(folder_name)
                        break
                    elif confirmation == "n":
                        continue
                    else:
                        break

        elif choice == "2":
            current_users = show_users("user")
            # select user
            while True:
                user_name = Prompt.ask("[bold red]NAME[/bold red] of user to be [bold red]deleted[/bold red]"
                                       "[italic] or [bold green](r)[/bold green]eturn to main menu[/italic]")
                if user_name == "r":
                    break
                elif user_name not in current_users:
                    console.print("Please try again")
                    continue
                elif user_name in current_users:
                    delete_user(user_name)
                else:
                    break

        elif choice == "3":
            current_folders = show_users("folder")
            print(current_folders)
            # select folder
            while True:
                folder = Prompt.ask("[bold blue]NAME[/bold blue] of folder to be [bold blue]sorted[/bold blue]"
                                    "[italic] or [bold green](r)[/bold green]eturn to main menu[/italic]")
                if folder == "r":
                    break
                elif folder not in current_folders:
                    console.print("Please try again")
                    continue
                elif folder in current_folders:
                    # print('folder', folder)
                    sort_documents(folder)
                else:
                    break

        elif choice == "4":
            organize_files()

        elif choice == "5":
            rename_file()

        else:
            break


if __name__ == "__main__":
    console = Console()
    main()
