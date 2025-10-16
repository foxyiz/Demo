# FoXYiZ - Multi-Purpose Task & Test Automation Framework

FoXYiZ is a **Python-based, low-code/no-code (LCNC) framework** designed for **multi-purpose task and test automation**. Built on principles of "What You See Is What You Get" (WYSIWYG) and Explainable AI (XAI), FoXYiZ **simplifies automation for a wide range of users, from domain experts to technical developers**. It **eliminates the need for complex Integrated Development Environments (IDEs) and direct coding** for non-technical users, allowing them to automate via simple CSV editors. FoXYiZ delivers powerful automation and analytics capabilities across various industries and human needs, extending beyond traditional software testing to capture wider industry automation needs.

FoXYiZ breaks automation into a simple formula: **f(x, y) = z**

*   **fEngine**: The **core engine** entry point is `fEngine.py`.
*   **fStart.json**: The root configuration file is `fStart.json` and no longer contains a 'drivers' section; drivers must be in your system PATH.
*   **Foxyiz.spec**: The build spec is `Foxyiz.spec`.
*   Files are organized under `x/`, `y/`, and `z/` folders as resources.
*   **xAutomation**: Built-in automation capabilities including UI, API, DB, SAP, IoT, and AI integrations.
*   **yTodo PADs**: Human-readable inputs for your automation tasks, including Plans, Actions, and Designs, defined in CSV format.
*   **zAnalytics**: Comprehensive outputs such as results, dashboards, and logs for actionable insights.

## Key Features

*   **No IDE Needed**: Automate tasks using simple CSV editors (e.g., Excel, Notepad) without writing code.
*   **Flexible for All Users**: Designed to simplify automation for various roles, allowing teams to focus on their specific skills.
*   **Human-Readable Inputs**: Define your automation tasks in intuitive CSV files (e.g., `y1Plans.csv`, `y2Actions.csv`, `y3Designs.csv`).
*   **Comprehensive Outputs**: Get detailed results in `zResults.csv`, visual dashboards in `zDash.html`, and debug logs in `zLog.txt`.
*   **AI-Powered (Optional & Governed)**: Features AI integration for advanced capabilities such as generating automation plans (yPADs), mind mapping, auto-running, auto-fixing, auto-healing, and predictive analysis.
*   **Portable**: The core framework is delivered as a single executable (`Foxyiz.exe`).
*   **Scalable**: Capable of running locally, on the cloud, or in containers.
*   **Parallel Processing**: Built-in multiprocessing support for concurrent execution of test plans, significantly improving performance.
*   **Robust Error Handling**: Advanced variable resolution with regex-based replacement, preventing partial matches and URL corruption.
*   **Comprehensive UI Automation**: Extensive web automation capabilities including drag-and-drop, context menus, key presses, hover actions, and dynamic element handling.

## Folder Structure

```
FoXYiZ/
├── Foxyiz.exe # Framework executable
├── fEngine.py # Core Framework engine (for developers)
├── fStart.json # Root configuration file (no 'drivers' section)
├── Foxyiz.spec # PyInstaller spec file
├── x/ # Automation scripts (bundled)
│   └── xActions.py # Reusable automation actions (for developers)
├── y/ # Input automation tasks (yPADs)
│   ├── Mix.json # Example yPAD configuration
│   ├── Mix/ # Example yPAD directory
│   │   ├── y1Plans.csv
│   │   ├── y2Actions.csv
│   │   └── y3Designs.csv
│   ├── FoXYiZ.json # FoXYiZ website testing yPAD
│   ├── FoXYiZ/ # FoXYiZ website testing directory
│   │   ├── y1Plans.csv
│   │   ├── y2Actions.csv
│   │   └── y3Designs.csv
├── z/ # Output, logs, and dashboards (keep this folder; clean up old files as needed)
│   ├── zDash_template.html # Dashboard template
│   └── 20241201_1430_Mix/ # Results directory (timestamped)
│       ├── Mix_zResults.csv
│       ├── Mix_zDash.html
│       └── _errors.csv
└── _others/ # Documentation and utilities
    └── Readme.txt # This documentation file
```

## Getting Started

### 1. Setup

*   **Download**: Get the FoXYiZ zip file (typically <50 MB).
*   **Unpack**: Extract the contents to a directory of your choice, e.g., `C:\Users\Desktop\FoXYiZ\`.
*   **Requirements**: Python 3.8+ is used by `Foxyiz.exe`, but no direct Python setup is needed for end-users as it's packaged.

### 2. Run the Demo

*   Open a command prompt or terminal in the `FoXYiZ` directory.
*   Execute the main executable with a configuration file:
    ```
    Foxyiz.exe --config fStart.json
    ```
    Or run specific yPAD configurations:
    ```
    Foxyiz.exe --config y/Mix.json
    ```
*   **Output**:
    *   The engine will load the specified yPADs (e.g., `y1Plans.csv`, `y2Actions.csv`, `y3Designs.csv`).
    *   Results will be generated in a timestamped folder within `z/` (e.g., `z/20241201_1430_Mix/`).
    *   You will find `zResults.csv` (test results), `zDash.html` (visual dashboard), and `zLog.txt` (debug logs).
*   **Comprehensive Demo**: The Mix yPAD includes a comprehensive `UI_HerokuComprehensive` plan that demonstrates 50 automation steps across 8 different web pages, showcasing the full capabilities of the framework.

### 3. Customize yPADs

*   Edit the CSV files located in `y/Mix/` using any CSV editor (e.g., Excel, Notepad).
*   Update `y1Plans.csv` (automation plans), `y2Actions.csv` (individual steps), and `y3Designs.csv` (data used by the steps).
*   **Important**: Use complete URLs in `y3Designs.csv` for navigation actions (e.g., `hk_add_remove_elements_url`) instead of semicolon-separated base URLs and selectors.
*   Re-run the executable with the same command to see your changes in action.

### 4. Create a New yPAD

1.  **Copy Template**: Duplicate the `y/Mix/` directory to a new folder, e.g., `y/MyNewPAD/`. Also, copy `y/Mix.json` and rename it to `y/MyNewPAD.json`.
2.  **Update Configuration** (`y/MyNewPAD.json`): Modify the JSON file to point to your new CSVs.

    ```json
    {
      "input_files": {
        "yPlans": ["y/MyNewPAD/y1Plans.csv"],
        "yActions": ["y/MyNewPAD/y2Actions.csv"],
        "yDesigns": ["y/MyNewPAD/y3Designs.csv"]
      }
    }
    ```
3.  **Edit CSVs**: Populate your new CSVs with desired automation plans, actions, and data.
4.  **Update `fStart.json`**: This central configuration file lists all yPAD configurations that the engine can run. Add your new `y/MyNewPAD.json` to the "configs" array. There is no 'drivers' section; drivers must be in your system PATH.
5.  **Run**: Execute your new yPAD configuration.
    ```
    Foxyiz.exe --config fStart.json
    ```

### 5. Integrate & Extend

*   **Migrate Existing Tasks**: Convert your current manual or automated tasks into the FoXYiZ CSV format for streamlined execution.
*   **Export Results**: Utilize the `zResults.csv` output to integrate with other tools like Jira, xRay, or Jenkins for reporting and tracking.
*   **Extend Capabilities**: For advanced automation needs, developers can customize `xActions.py` to add new functionalities or integrate with specific systems.

## File Formats

### 1. `fStart.json`

This file configures the overall execution of FoXYiZ, specifying which yPAD configurations to use and performance settings. **No 'drivers' key is needed.**

```json
{
  "configs": ["y/Mix.json", "y/FoXYiZ.json"],
  "thread_count": 4,
  "timeout": 6,
  "debug": false
}
```

**Key Configuration Options:**
- `thread_count`: Number of parallel processes for concurrent plan execution (default: CPU cores, max: 4)
- `timeout`: Default timeout in seconds for individual actions (default: 6)
- `debug`: Enable verbose logging and error artifacts (default: false)

### 2. yPAD JSON (e.g., `y/Mix.json`)

This JSON file links to the specific CSV files that define a set of automation tasks. **Only yPlans, yActions, and yDesigns are needed. Do not include zPlans or zActions.**

```json
{
  "input_files": {
    "yPlans": ["y/Mix/y1Plans.csv"],
    "yActions": ["y/Mix/y2Actions.csv"],
    "yDesigns": ["y/Mix/y3Designs.csv"]
  }
}
```

### 3. `y1Plans.csv`

Defines your top-level automation plans. Each row represents a plan, specifying its ID, associated design(s), and whether it should be run.

```
PlanId,PlanName,DesignId,Run,Tags,Output
LoginTest,Verify_Login_Process,D1,Y,UI,login_success
UI_AddContact,Verify_UI_AddContact,D1,Y,UI,contact_added
UI_HerokuComprehensive,Verify_Heroku_Comprehensive_Flow,D1,Y,UI,heroku_comprehensive_success
Math_Addition,Verify_Math_Addition,D1;D2,Y,Math,addition_result
```

**Key Columns:**
- `PlanId`: Unique identifier for the plan (automatically prefixed with 'P' if not present)
- `PlanName`: Human-readable name for the plan
- `DesignId`: Associated design data (can be multiple designs separated by semicolons)
- `Run`: Whether to execute this plan (Y/N)
- `Tags`: Categorization tags for filtering
- `Output`: Expected output description

### 4. `y2Actions.csv`

Specifies the individual steps or actions within each plan. It defines the action type (e.g., xUI, xAPI, xMath), the specific action to perform, and any inputs or expected outputs.

```
PlanId,StepId,StepInfo,ActionType,ActionName,Input,Output,Expected,Critical
UI_HerokuComprehensive,1,Open Browser,xUI,xOpenBrowser,chrome,,,y
UI_HerokuComprehensive,2,Navigate to Add/Remove Elements,xUI,xNavigate,hk_add_remove_elements_url,,,y
UI_HerokuComprehensive,3,Click Add Element,xUI,xClick,hk_add_element_button,,,y
UI_HerokuComprehensive,4,Verify Delete Button Appears,xUI,xWaitFor,hk_delete_button,,,y
LoginTest,1,Reuse UI_HerokuComprehensive,xReuse,UI_HerokuComprehensive,,,y
Math_Addition,1,Add Numbers,xMath,xAdd,5;10;15,30,30,n
```

**Key Columns:**
- `PlanId`: Links to the plan in y1Plans.csv
- `StepId`: Sequential step number within the plan
- `StepInfo`: Human-readable description of the step
- `ActionType`: Type of action (xUI, xAPI, xMath, xAI, xJSON)
- `ActionName`: Specific action method to call
- `Input`: Input data (can reference variables from y3Designs.csv)
- `Output`: Expected output value
- `Expected`: Expected result for validation
- `Critical`: Whether step failure should stop plan execution (y/n)

### 5. `y3Designs.csv`

Provides the test data or design configurations that will be used by your actions. Data can be parameterized using different design IDs.

```
Type,DataName,D1,D2,D3
UI,hk_base_url,https://the-internet.herokuapp.com/,https://the-internet.herokuapp.com/,https://the-internet.herokuapp.com/
UI,hk_add_remove_elements_url,https://the-internet.herokuapp.com/add_remove_elements/,https://the-internet.herokuapp.com/add_remove_elements/,https://the-internet.herokuapp.com/add_remove_elements/
UI,hk_add_element_button,"css==button[onclick=""addElement()""]","css==button[onclick=""addElement()""]","css==button[onclick=""addElement()""]"
UI,email,kkarthikqe@gmail.com,,
UI,password,Test123$,,
API,base_url_pet,https://petstore.swagger.io/v2,https://petstore.swagger.io/v2,https://petstore.swagger.io/v2
Math,number1,10,20,30
```

**Key Columns:**
- `Type`: Category of data (UI, API, Math, AI, etc.)
- `DataName`: Variable name referenced in y2Actions.csv Input field
- `D1, D2, D3`: Different data sets for various test scenarios
- **Important**: Use complete URLs for navigation actions instead of semicolon-separated base URLs and selectors

### 6. Outputs

After execution, FoXYiZ generates detailed outputs to help you analyze results.

*   **zResults.csv**: Provides a summary of the execution results for each plan and action, including pass/fail status.
*   **zDash.html**: An interactive HTML dashboard for a visual overview of your automation run, indicating what passed, failed, and why.
*   **zLog.txt**: Contains detailed debug logs for troubleshooting and in-depth analysis of the execution process.

## Recent Improvements & Fixes

### Version Updates (December 2024)

**Performance Enhancements:**
- ✅ **Parallel Processing**: Implemented true multiprocessing support for concurrent plan execution, significantly improving performance
- ✅ **Smart Resource Management**: Conditional folder creation - results directories are only created when needed (for file outputs, screenshots, errors)
- ✅ **Optimized Execution**: Enhanced variable resolution with regex-based replacement to prevent partial matches and URL corruption

**Bug Fixes:**
- ✅ **Variable Resolution**: Fixed critical bug where variable names like `email` were incorrectly matching within `email_xpath` due to simple string replacement
- ✅ **URL Construction**: Resolved issues with malformed URLs caused by semicolon-separated base URLs and selectors in navigation actions
- ✅ **CSV Design**: Updated all navigation actions to use complete URLs instead of concatenated base URL + selector combinations
- ✅ **XPath Syntax**: Fixed XPath syntax errors and comma escaping issues in selectors
- ✅ **Plan Reuse**: Corrected plan ID prefixing to ensure proper plan reuse functionality

**New Features:**
- ✅ **Comprehensive Demo Plan**: Added `UI_HerokuComprehensive` plan showcasing 50 automation steps across 8 web pages
- ✅ **Enhanced UI Actions**: Improved support for drag-and-drop, context menus, key presses, hover actions, and dynamic elements
- ✅ **Better Error Handling**: Enhanced error artifacts with screenshots, page source, and detailed error logs
- ✅ **PyInstaller Compatibility**: Fixed multiprocessing issues in executable builds

## AI/LLM Integration

FoXYiZ leverages AI/LLMs to enhance your automation process:

*   **Automation Generation**: AI can assist in generating new yPAD CSVs (plans, actions, designs) based on your natural language prompts, accelerating test creation.
*   **Self-Healing**: AI can analyze `zResults.csv` failures and suggest or even automatically adjust `y2Actions.csv` to fix issues, leading to more resilient automation.
*   **A/B Testing & Exploratory Automation**: Easily introduce new design variations in `y3Designs.csv` or expand `y1Plans.csv` with AI-generated scenarios for comprehensive testing and exploration.

## Support

*   **Debug**: Review `zLog.txt` for detailed information on any issues encountered during execution.
*   **Extend**: Developers can modify `f/fEngine.py` or `xActions.py` to add custom functionalities or integrate with specific systems.
*   **Contact**: For further assistance or inquiries, reach out to the FoXYiZ team.

---

**FoXYiZ: Automation Simplified**
**f(x, y) = z**

## Requirements & Installation

FoXYiZ (IoT project) requires the following Python packages (for developer use):

```
pandas
requests
selenium
```

To install all dependencies, run:

```
pip install -r requirements.txt
```

End-users running Foxyiz.exe do not need to install Python or these packages.