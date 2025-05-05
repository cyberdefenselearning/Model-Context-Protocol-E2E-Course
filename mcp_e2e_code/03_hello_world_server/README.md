
# MCP Basic Project

This repository contains a basic implementation of the MCP (Model Context Protocol). This guide will walk you through the steps to clone the repository, set up a virtual environment, and run the MCP project.

## Steps to Set Up the Project

Follow these steps to get the project running on your local machine.

### 1. Navigate to the Project Directory

Change into the `02_hello_world_server` directory:

```bash
cd 02_hello_world_server
```

### 2. Create a Virtual Environment

Create a new virtual environment using `uv`:
* **uv**: A command-line tool to simplify project setup and management in Python.
 #### UV Installation Guide

 Install **uv** using our official standalone installer :-

 * Windows

 ```bash
 powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
* macOS/Linux
```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
```
#### Initialize uv
```bash
uv init
```
#### create a virtual environment
```bash
uv venv
```

### 3. Activate the Virtual Environment

Activate the virtual environment:

#### On Windows:

```bash
.venv\Scripts\activate
```

#### On macOS/Linux:

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

Install the necessary dependencies for the project:

```bash
uv add mcp[cli] httpx
```

### 5. Run the Project

Finally, run the main script in development mode:

```bash
mcp dev main.py
```

This will start the project in development mode.




