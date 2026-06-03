import os
import json
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

# Import modules
from pages import get_page_info
from posts import list_posts, create_post, delete_post
from comments import get_comments, reply_comment, delete_comment
from insights import get_page_summary

console = Console()

SETTINGS_FILE = "settings.json"


# =========================
# Load Settings
# =========================
def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        console.print("[red]settings.json not found![/red]")
        return {}

    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)


def save_settings(data):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f, indent=4)


# =========================
# UI
# =========================
def clear():
    os.system("clear")


def banner():
    console.print(
        Panel.fit(
            "[bold cyan]FACEBOOK PAGE TERMINAL TOOL[/bold cyan]\n"
            "[green]Full Manager System[/green]"
        )
    )


# =========================
# SETTINGS EDITOR
# =========================
def settings_menu():
    settings = load_settings()

    console.print("\n[bold yellow]CURRENT SETTINGS[/bold yellow]")
    console.print(settings)

    page_id = Prompt.ask("Enter Page ID", default=settings["facebook"]["page_id"])
    token = Prompt.ask("Enter Access Token", default=settings["facebook"]["access_token"])

    settings["facebook"]["page_id"] = page_id
    settings["facebook"]["access_token"] = token

    save_settings(settings)

    console.print("[green]Settings Updated![/green]")


# =========================
# MAIN MENU
# =========================
def main():
    while True:
        clear()
        banner()

        console.print("""
[1] Page Info
[2] List Posts
[3] Create Post
[4] Delete Post
[5] View Comments
[6] Reply Comment
[7] Delete Comment
[8] Page Insights
[9] Settings
[0] Exit
""")

        choice = Prompt.ask("Select Option")

        if choice == "1":
            get_page_info()

        elif choice == "2":
            list_posts()

        elif choice == "3":
            msg = Prompt.ask("Enter post message")
            create_post(msg)

        elif choice == "4":
            pid = Prompt.ask("Enter Post ID")
            delete_post(pid)

        elif choice == "5":
            post_id = Prompt.ask("Enter Post ID")
            get_comments(post_id)

        elif choice == "6":
            cid = Prompt.ask("Enter Comment ID")
            msg = Prompt.ask("Reply message")
            reply_comment(cid, msg)

        elif choice == "7":
            cid = Prompt.ask("Enter Comment ID")
            delete_comment(cid)

        elif choice == "8":
            get_page_summary()

        elif choice == "9":
            settings_menu()

        elif choice == "0":
            console.print("[bold red]Exiting...[/bold red]")
            break

        else:
            console.print("[red]Invalid Option![/red]")

        input("\nPress Enter to continue...")


# =========================
# RUN
# =========================
if __name__ == "__main__":
    main()
