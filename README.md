# FoXYiZ - Automation Made Simple

**FoXYiZ** is a powerful, user-friendly automation framework that lets you automate tasks and tests without writing code. Whether you're testing websites, APIs, or performing calculations, FoXYiZ makes automation accessible to everyone - from business users to technical teams.

## What is FoXYiZ?

FoXYiZ is a **low-code/no-code automation framework** that follows a simple formula: **f(x, y) = z**

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

### Step 2: Verify Installation

1. Open a command prompt or terminal
2. Navigate to the FoXYiZ folder
3. Run: `Foxyiz.exe --help`

If you see the help message, you're ready to go!

## Quick Start Guide

### Running Your First Automation

1. **Open the example configuration file** (`fStart.json`) in any text editor
2. **Run FoXYiZ** with the default configuration:
   ```
   Foxyiz.exe --config fStart.json
   ```
3. **View your results** in the `z` folder - you'll find:
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

4. **Run your automation**:
   ```
   Foxyiz.exe --config your-config.json
   ```

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

## Understanding Your Files

### Plans File (y1Plans)

Defines **what** you want to automate. Each row is a plan that describes:
- Plan name and ID
- Which data sets to use
- Whether to run it or not

**Example:**
```
PlanId,PlanName,DesignId,Run
LoginTest,Verify_Login_Process,D1,Y
SearchTest,Verify_Search_Functionality,D1;D2,Y
```

### Actions File (y2Actions)

Defines **how** to perform each step. Specifies:
- Action type (web, API, math, etc.)
- What action to perform
- Input data
- Expected results

**Example:**
```
PlanId,StepId,ActionType,ActionName,Input,Expected
LoginTest,1,xUI,xNavigate,login_url,
LoginTest,2,xUI,xClick,username_field,
LoginTest,3,xUI,xType,username_field;myuser,
```

### Designs File (y3Designs)

Contains **data** used by your actions. Provides:
- Variable names
- Different data sets (D1, D2, D3, etc.)
- Test data values

**Example:**
```
Type,DataName,D1,D2
UI,login_url,https://example.com/login,https://test.example.com/login
UI,username_field,css==input[name="username"],css==input[id="user"]
```

## Viewing Results

After running FoXYiZ, check the `z` folder for your results:

📊 **Results CSV** - Detailed execution results in spreadsheet format  
📈 **HTML Dashboard** - Interactive visual dashboard showing pass/fail status  
📝 **Log File** - Detailed execution logs for troubleshooting  

## Configuration Options

You can customize FoXYiZ behavior through the configuration file:

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

### Using Tags to Filter Plans

The **tags** feature allows you to run only specific plans that match certain tags. This is useful when you have many plans but only want to execute a subset.

**How it works:**
1. In your `y1Plans` file, add a `Tags` column and assign tags to each plan
2. In `fStart.json`, add a `tags` array with the tags you want to run
3. Only plans with matching tags will be executed

**Example:**

In `y1Plans.csv`:
```
PlanId,PlanName,DesignId,Run,Tags
Math_Addition,Verify_Math_Addition,D1,Y,Math
UI_Login,Verify_Login_Process,D1,Y,UI
API_Weather,Get_Weather_Data,D1,Y,Weather
```

In `fStart.json`:
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

