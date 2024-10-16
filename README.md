# Personal To-Do List Application

## Overview
The Personal To-Do List Application is a command-line tool for managing tasks. Users can add tasks, view them, mark them as completed, or delete them. Tasks are categorized (e.g., Work, Personal, Urgent) and saved to a local JSON file, ensuring progress is saved between sessions.

## Features
- **Add Tasks**: Create a new task with a title, description, and category.
- **View Tasks**: Display all tasks, including their status (completed/incomplete).
- **Mark Tasks as Completed**: Update the status of a task to completed.
- **Delete Tasks**: Remove a task from the list.
- **File Persistence**: Tasks are stored in `tasks.json` for saving between sessions.

## How to Install and Run

### Prerequisites
- Ensure you have **Python 3.x** installed. You can download it from the official [Python website](https://www.python.org/downloads/).

### Installation Instructions
1. **Clone the repository**:
   ```bash
   git clone <https://github.com/rohith460/voc>
2. run the voc.py code

# ADDING A TASK:

Choose an option (1-5): 1
Task title: Finish project
Task description: Complete the final project report
Task category (e.g., Work, Personal, Urgent): Work
Task 'Finish project' added successfully!

# VIWEING A TASK:

Choose an option (1-5): 2
^^^^Task List^^^^^
1. Finish project - Work [Incomplete]
    Complete the final project report

# MARKING A TASK AS COMPLETED:

Choose an option (1-5): 3
Enter the task number to mark as completed: 1
Task 'Finish project' marked as completed.

# DELETING A TASK:

Choose an option (1-5): 4
Enter the task number to delete: 1
Task 'Finish project' deleted.

# EXITING:

Choose an option (1-5): 5
Goodbye! Your tasks have been saved.
