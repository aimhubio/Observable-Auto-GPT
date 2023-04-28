<div align="center">
  <img src="https://user-images.githubusercontent.com/13848158/225620298-9f9293e9-a138-41fd-bd77-21d53d0490b7.png">
  <h3>
    Autonomous GPT-4 Experiment with Aim.
  </h3>
  Observable Auto GPT logs all your Auto-GPT experiment metadata, enables a UI to observe them, and an SDK to query them programmatically.
  
  <p align="center">
    <strong>Learn more:</strong> </br>
    <a href="https://github.com/aimhubio/aim">Aim: An easy-to-use & supercharged open-source AI metadata tracker.</a> </br>
    <a href="https://github.com/Significant-Gravitas/Auto-GPT">Auto-GPT: An Autonomous GPT-4 Experiment</a>
  </p>
  
</div>


Observable Auto-GPT is an advanced tool that combines the power of two cutting-edge technologies: [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) and [Aim](https://github.com/aimhubio/aim). Auto-GPT is highly capable tool that can autonomously chain together LLM thoughts to achieve any goal set by the user. When integrated with Aim, the platform provides users with a seamless experience, allowing for efficient tracking of the model's prompts, commands, outputs and many more.

## Setting up

To install the latest version of Aim via pip, please use the following command:
```bash
pip install aim
```

The remaining steps are identical to those for Auto-GPT, and you can refer to the [Auto-GPT Documentation](https://significant-gravitas.github.io/Auto-GPT/setup/) for more information.

## Sample Usage

Let's try out an Auto-GPT example where we ask the model to recommend summer vacation spots. To set the Aim repository, you can use the `--aim-repo` command line argument. If it's not specified, the default directory will be used.

Let's execute the following command to start up the processes:
```bash
./run.sh --aim-repo vacation_planning
```

After which we can specify the basic configs:
- AI Name: Vacation planner
- Describe your AI's role: An AI-powered recommendation system for optimal summer vacation destinations.

Next, let's set 3 goals for our AI agent:
- Suggest budget-friendly locations
- Provide a list of places in the location to avoid.
- Suggest restaurants and locations that are popular among the locals

Auto-GPT will begin generating prompts for the LLM and executing commands. You can monitor all outputs from each run's Text page, or for more extensive searches, you can use Text Explorer.
