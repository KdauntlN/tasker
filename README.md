# TASKER

A simple, fast, plain-text todo list manager for your terminal.

## Features

- ✅ Add tasks quickly from the command line  
- 📋 View pending, completed, or all tasks  
- ✏️ Edit or delete tasks  
- 💾 Saves to a local plain-text file (`~/.tasker/tasks.txt`)  
- 🔒 No accounts, no cloud, no tracking — ever  

## Install

Clone the repo and make it executable:

```bash
git clone https://github.com/kdauntln/tasker.git
cd tasker
chmod +x tasker.py
```

Then run it like:

```bash
./tasker.py add "Buy duct tape"
./tasker.py list
```

Or symlink it for global use:

```bash
ln -s /full/path/to/tasker.py /usr/local/bin/tasker
```

## Usage

```bash
tasker add "Do the laundry"
tasker list
tasker done 2
tasker delete 3
tasker list --done
tasker list --all
```

## File Format

Tasks are stored as plain text in `~/.tasker/tasks.txt`.  
Each line is one task. Completed tasks are marked internally.  
You can version it with git, sync it with Dropbox, or just back it up.

## Philosophy

- No sync. No bloat. No web UI.
- Your tasks are yours.
- Fast enough to replace sticky notes.

## License

Zero-Clause BSD (0BSD)  
See [LICENSE](./LICENSE) for full text.  
You can use, modify, fork, redistribute, or sell this software freely.

## Author

Henry Knight  
[GitHub](https://github.com/kdauntln)
