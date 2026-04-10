# FoXYiZ - Automation Made Simple

**FoXYiZ** is a powerful, user-friendly automation framework that lets you automate tasks and tests without writing code. Whether you're testing websites, APIs, or performing calculations, FoXYiZ makes automation accessible to everyone - from business users to technical teams.

## What is FoXYiZ?

FoXYiZ is a **low-code/no-code automation framework(LCNC)** that follows a simple formula: **f(x, y) = z**

- **f** = The Engine that binds configs, Plans, Actions and Designs to power your Automation.
- **x** = Built-in automation capabilities (UI, API, Math, AI, and more)
- **y** = Your automation plans, actions, and data (defined in simple files)
- **z** = Results, dashboards, and insights

**No coding required!** You define your automation tasks using simple file formats (CSV, TXT, JSON, or Excel) that work with any editor you're comfortable with.

## Key Benefits

✅ **No Programming Needed** - Use Excel, Notepad, or any text editor to create automation tasks  
✅ **Multiple File Formats** - Work with CSV, TXT, JSON, or Excel files - choose what you prefer  
✅ **Visual Results** - Get beautiful dashboards and detailed reports  
✅ **Easy to Use** - Simple file-based configuration, no complex setup  
✅ **Powerful Features** - Automate web browsers, APIs, databases, calculations, and more  
✅ **Portable** - Single executable file, runs anywhere  

## Download & Installation

### Step 1: Download FoXYiZ

1. Download the latest `Foxyiz.exe` from the [Releases](https://github.com/foxyiz/Code/releases) section
2. Extract the files to a folder of your choice (e.g., `C:\FoXYiZ\` or `C:\Users\YourName\Desktop\FoXYiZ\`)

**That's it!** No additional installation or setup required. The executable is self-contained and includes everything you need.

**Typical layout:** The executable and main config live in the **`f`** folder. Your automation data (**`y/`**), results (**`z/`**), and this README sit in the **installation root** (the parent of **`f`**):

```
YourFoXYiZFolder/          ← installation root (README, y/, z/, …)
  f/
    Foxyiz.exe
    fStart.json
    .env                     ← optional; see secrets section below
  y/
  …
```

Place your **`.env`** file in **`f/`** (next to `Foxyiz.exe` and `fStart.json`)—see [Sensitive values (`.env`)](#sensitive-values-env).

### Step 2: Verify Installation

1. Open a command prompt or terminal
2. Navigate to your **FoXYiZ installation root** (the folder that contains the **`f`** folder)
3. Run: `f\Foxyiz.exe --help` (on Windows) or `f/Foxyiz.exe --help` (on macOS/Linux)

Alternatively, `cd` into **`f`** and run `Foxyiz.exe --help`.

If you see the help message, you're ready to go!

## Quick Start Guide

### Running Your First Automation

1. **Open the example configuration file** **`f/fStart.json`** (inside the **`f`** folder) in any text editor
2. **Run FoXYiZ** from your **installation root** with the default configuration (FoXYiZ finds `fStart.json` next to the executable):
   ```
   f\Foxyiz.exe
   ```
   Or, after `cd f`: `Foxyiz.exe` (same default). To pass the config explicitly: `f\Foxyiz.exe --config fStart.json` (paths are resolved from the **`f`** folder first).
3. **View your results** in the **`z`** folder at the installation root (next to **`y/`**)—you'll find:
   - Results in CSV format
   - Interactive HTML dashboard
   - Detailed execution logs

### Creating Your Own Automation

1. **Create your automation files** using any of these formats:
   - **CSV files** (`.csv`) - Great for Excel users
   - **Text files** (`.txt`) - Simple and universal
   - **JSON files** (`.json`) - For structured data
   - **Excel files** (`.xlsx`) - Advanced formatting

2. **Define three types of files**:
   - **Plans** (`y1Plans.*`) - What you want to automate
   - **Actions** (`y2Actions.*`) - The steps to perform
   - **Designs** (`y3Designs.*`) - The data to use

3. **Create a configuration file** (`.json`) that points to your files

4. **Run your automation** from the installation root, for example:
   ```
   f\Foxyiz.exe --config your-config.json
   ```
   Put custom main configs (JSON) in **`f/`** unless you use an absolute path.

### Storing passwords, API keys, and email addresses

Put sensitive values—**email addresses**, **passwords**, **API keys**, tokens, and similar—in a **`.env`** file in the **`f`** folder—**the same folder as `Foxyiz.exe` and `fStart.json`**. FoXYiZ also looks for `.env` in the **current working directory** if you run the exe from elsewhere, but the recommended location is **`f/.env`**.

Do **not** put secrets in your Plans, Actions, or Designs files if those files are shared, backed up to the cloud, or checked into source control.

FoXYiZ loads `.env` into the environment so your automation can use those values (for example when resolving variables in **y3Designs** or when actions read environment variables). Keep `.env` private and do not share it. See [Sensitive values (`.env`)](#sensitive-values-env) under Configuration Options for more detail.

## File Formats Supported

FoXYiZ supports multiple file formats so you can work with what you're comfortable with:

| Format | Extension | Best For |
|--------|-----------|----------|
| CSV | `.csv` | Excel users, simple data entry |
| Text | `.txt` | Simple editing, universal compatibility |
| JSON | `.json` | Structured data, programmatic generation |
| Excel | `.xlsx` | Complex formatting, formulas |

**You can mix formats!** Use CSV for one file, TXT for another - FoXYiZ automatically detects the format.

## What Can You Automate?

FoXYiZ supports a wide range of automation capabilities:

🌐 **Web Automation** - Navigate websites, fill forms, click buttons, verify content  
📡 **API Testing** - Test REST APIs, send requests, validate responses  
🔢 **Math Operations** - Perform calculations, verify results  
🤖 **AI Integration** - Leverage AI for advanced automation tasks  
📧 **Email Automation** - Send and receive emails  
💾 **Database Operations** - Query databases, verify data  
☁️ **Cloud Storage** - Upload/download files from cloud services  
📱 **IoT Devices** - Interact with IoT devices and sensors  

## Understanding Your Files (YPAD)

Each YPAD (your automation data) uses three file types. The **exact column names** must match those below.

### Plans File (y1Plans)

Defines **what** you want to automate. Each row is a plan.

**Columns (exact):** `PlanId`, `PlanName`, `DesignId`, `Run`, `Tags`, `Output`

| Column    | Description |
|-----------|-------------|
| PlanId    | Unique plan identifier (e.g. PLoginTest, PMath_Addition). |
| PlanName  | Human-readable name. |
| DesignId  | One or more design IDs separated by `;` (e.g. D1 or D1;D2). Variables from y3Designs are chosen by this. |
| Run       | Y = run this plan, N = skip. |
| Tags      | Optional; used with `tags` in **`f/fStart.json`** to filter which plans run. |
| Output    | Optional description. |

**Example (y1Plans.csv):**
```
PlanId,PlanName,DesignId,Run,Tags,Output
PLoginTest,Verify_Login_Process,D1,Y,UI,login_success
PMath_Addition,Verify_Math_Addition,D1;D2,Y,Math,addition_result
PAPI_PetGet,Verify_API_PetGet,D1,Y,petstore,pet_status
```

### Actions File (y2Actions)

Defines **how** to perform each step. One row per step.

**Columns (exact):** `PlanId`, `StepId`, `StepInfo`, `ActionType`, `ActionName`, `Input`, `Output`, `Expected`, `Critical`

| Column     | Description |
|------------|-------------|
| PlanId     | Must match a PlanId in y1Plans. |
| StepId     | Step number (e.g. 1, 2, 3). |
| StepInfo   | Short description of the step. |
| ActionType | e.g. xUI, xMath, xAPI, xReuse, xCustom. |
| ActionName | e.g. xOpenBrowser, xAdd, xGet, or a PlanId for xReuse. |
| Input      | Semicolon-separated parameters; can use variable names from y3Designs (e.g. url;locator). |
| Output     | Optional output variable name. |
| Expected   | Optional expected value for pass/fail. |
| Critical   | Y = stop plan if this step fails; N = continue. |

**Example (y2Actions.csv):**
```
PlanId,StepId,StepInfo,ActionType,ActionName,Input,Output,Expected,Critical
PLoginTest,1,Open login page,xUI,xOpenBrowser,,,Y
PLoginTest,2,Go to URL,xUI,xNavigate,login_url,,,Y
PMath_Addition,1,Add numbers,xMath,xAdd,v1;v2,sum,,Y
PMath_Addition,2,Check result,xMath,xCompare,sum;expected,Pass/Fail,Pass,Y
```

### Designs File (y3Designs)

Contains **data** (variables) used in Input and Expected in y2Actions. One row per variable.

**Columns (exact):** `Type`, `DataName`, `D1`, `D2`, `D3`

| Column   | Description |
|----------|-------------|
| Type     | Category (e.g. UI, Math, API). |
| DataName | Variable name used in Input/Expected in y2Actions (e.g. login_url, v1, base_url). |
| D1       | Value when DesignId is D1. |
| D2       | Value when DesignId is D2. |
| D3       | Value when DesignId is D3. (Add D4, D5, … as needed.) |

**Example (y3Designs.csv):**
```
Type,DataName,D1,D2,D3
UI,login_url,https://example.com/login,https://test.example.com/login,https://staging.example.com/login
UI,username_field,css=#username,css=#user,css=#login
Math,v1,10,20,5
Math,v2,5,10,2
Math,expected,15,30,7
API,base_url,https://api.example.com,https://api.test.com,
```

## Viewing Results

After running FoXYiZ, check the **`z`** folder (usually at your **installation root**, beside **`y/`**) for your results:

📊 **Results CSV** - Detailed execution results in spreadsheet format  
📈 **HTML Dashboard** - Interactive visual dashboard showing pass/fail status  
📝 **Log File** - Detailed execution logs for troubleshooting  

## Configuration Options

You can customize FoXYiZ behavior through the main configuration file **`f/fStart.json`**:

```json
{
  "configs": ["y/MyAutomation.json"],
  "thread_count": 4,
  "timeout": 10,
  "headless": false,
  "debug": false,
  "tags": ["Math", "UI"]
}
```

- **configs**: List of automation configurations to run
- **thread_count**: Number of parallel executions (1-4)
- **timeout**: Default timeout in seconds for actions
- **headless**: Run browser in background (true/false)
- **debug**: Enable detailed debugging (true/false)
- **tags**: Filter plans by tags - only run plans with matching tags (optional)

### Sensitive values (`.env`)

Store **email IDs**, **passwords**, **API keys**, and other secrets in a **`.env`** file inside the **`f`** folder—**next to `Foxyiz.exe` and `fStart.json`**. That is the first place FoXYiZ looks. It then checks the **folder you run the command from** (current working directory), so you can use a root-level `.env` only if you always launch FoXYiZ from that directory; the reliable choice is **`f/.env`**.

Do **not** put `.env` under **`y/`** unless you have a deliberate layout and understand path resolution.

Use one variable per line in the usual form `NAME=value` (no spaces around `=` unless your tool requires quotes for values with spaces). FoXYiZ loads this file into the environment so values can be used in your Designs and by actions that expect environment variables.

**Do not** paste secrets into CSV, JSON, or Excel design files that you email, commit to git, or publish. Treat **`.env`** like a private key file: keep it on your machine, exclude it from backups you share, and never commit it to a repository.

### Using Tags to Filter Plans

The **tags** feature allows you to run only specific plans that match certain tags. This is useful when you have many plans but only want to execute a subset.

**How it works:**
1. In your `y1Plans` file, add a `Tags` column and assign tags to each plan
2. In **`f/fStart.json`**, add a `tags` array with the tags you want to run
3. Only plans with matching tags will be executed

**Example:**

In `y1Plans.csv`:
```
PlanId,PlanName,DesignId,Run,Tags,Output
PMath_Addition,Verify_Math_Addition,D1,Y,Math,addition_result
PUI_Login,Verify_Login_Process,D1,Y,UI,login_success
PAPI_Weather,Get_Weather_Data,D1,Y,Weather,weather_ok
```

In **`f/fStart.json`**:
```json
{
  "configs": ["y/Math.json"],
  "tags": ["Math"]
}
```

This will run only the `Math_Addition` plan, skipping `UI_Login` and `API_Weather`.

**Multiple Tags:**
You can specify multiple tags to run plans matching any of them:
```json
{
  "tags": ["Math", "UI"]
}
```

**Run All Plans:**
To run all plans regardless of tags, either:
- Omit the `tags` field entirely, or
- Use `"tags": ["All"]`

**Note:** Tag matching is case-insensitive. If you specify tags but your plans don't have a `Tags` column, all plans will run with a warning message.

## Tips for Success

💡 **Start Simple** - Begin with basic plans and gradually add complexity  
💡 **Use Examples** - Check the included examples to learn the format  
💡 **Test Incrementally** - Test one plan at a time before running everything  
💡 **Check Logs** - Review log files if something doesn't work as expected  
💡 **Use Tags** - Organize your plans with tags for easy filtering  
💡 **Protect Secrets** - Keep email addresses, passwords, and API keys in **`f/.env`** (next to the executable), not in shared automation files  

## Getting Help

📖 **Documentation** - Check the `_others` folder for detailed documentation  
🐛 **Troubleshooting** - Review the log files in the `z` folder for error details  
💬 **Support** - Visit the GitHub repository for issues and discussions  

## System Requirements

- **Windows**: Windows 7 or later
- **macOS**: macOS 10.12 or later  
- **Linux**: Most modern distributions
- **Memory**: 2GB RAM minimum (4GB recommended)
- **Disk Space**: 100MB for the executable and results

**Note**: No Python installation required! The executable is self-contained.

## License

FoXYiZ is provided as-is for automation and testing purposes. Please refer to the license file in the repository for details.

---

**FoXYiZ: Automation Simplified**  
**f(x, y) = z**

*Make automation accessible to everyone.*

## Example Prompts for an LLM Agent

Use this README as context. Here are sample prompts an end user can ask an LLM agent to understand and work with FoXYiZ:

- "Give me a one-paragraph summary of FoXYiZ and its key capabilities."
- "Step-by-step: how do I run the included example automation using `f/fStart.json`?"
- "Create a minimal `y1Plans`, `y2Actions`, and `y3Designs` set that logs into https://example.com and verifies the dashboard."
- "Explain the difference between Plans, Actions, and Designs with a short example for each."
- "How do I run only plans tagged `Math`? Show a sample `f/fStart.json` and a `y1Plans` row."
- "A run failed with 'element not found' in the logs — what troubleshooting steps should I try?"
- "How can I run the browser headless and increase timeout? Show the config changes."
- "Convert this Designs example (Excel) into CSV and JSON equivalents."
- "Which command-line flags are available and what do they do? Provide concise examples."
- "How would I add a custom action type that calls an external script? Outline required files and config changes."
- "What are recommended practices for storing API keys and secrets when using FoXYiZ?"
- "Give three small example automations I can run now (Math addition, API weather check, UI login) with brief plan/action/design snippets."

Tips for prompting the agent:
- Provide relevant file content (e.g., `f/fStart.json`, a snippet of `y2Actions`) when asking for edits or debugging.
- Ask for "step-by-step" or "diff" if you want exact file changes to apply.
- Mention the target OS or runtime (Windows, headless, etc.) when asking about execution details.
