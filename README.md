# Inhuman-insurance-inc-ais-robot

Status of Last Deployment: 
[![Inhuman-insurance-inc-ais-robot-actions](https://github.com/linksysadmin/inhuman-insurance-inc-ais-robot-RPA-3/actions/workflows/learn-github-actions.yml/badge.svg)](https://github.com/linksysadmin/inhuman-insurance-inc-ais-robot-RPA-3/actions/workflows/learn-github-actions.yml)

```
┌──────────┐   ┌────────────┐   ┌──────────┐
│ Producer │ → │ Work items │ → │ Consumer │ → 💰
└──────────┘   └────────────┘   └──────────┘
```


## Work Item management in the Control Room


Tasks -> Add Task Package:
    - Enter Task Package name
    - Enter Public Git

Processes -> New process:
    - Add Task Produce Data
    - Add variables






## Create a new robot
### RCC workflow
RCC installation instructions - https://robocorp.com/docs/rcc/installation
RCC toolchain - https://robocorp.com/docs/rcc/overview

```
rcc create
```
or
```
rcc robot initialize -d my-robot
```
```
cd my-robot
```
Test run your robot locally in a clean environment
Before pushing your robot to Control Room, you can test your robot using the rcc task testrun command.
```rcc task testrun```



### Conda Environment
How to? - https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-20-04

**Install Miniconda**:

Скачайте установщик Miniconda с официального сайта и следуйте инструкциям по установке.
```bash
curl https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh --output anaconda.sh
```
**Updating conda**:
```bash 
conda env update --file conda.yaml
```

**Uninstalling conda**:
Open a terminal window.
Remove the entire conda install directory with (this may differ depending on your installation location)
```bash
rm -rf ~/conda
rm -rf ~/miniconda3
```

Optional: ```run conda init --reverse --all``` to undo changes to shell initialization scripts
Optional: remove the following hidden file and folders that may have been created in the home directory:
- .condarc file
- .conda directory
- .continuum directory

By running:
```bash
rm -rf ~/.condarc ~/.conda ~/.continuum
```



**Tools**:

Create environments
```conda create --name rpa-3-level```

Activate
``` conda activate rpa-3-level```

Update
```conda env update --file conda.yaml --prune```
```conda activate rpa-3-level```

Check available variables in environment
```printenv```

Remove an environment named "myenv"
```conda env remove --name myenv```

List of environments
```conda env list```



```bash
export RC_WORKITEM_INPUT_PATH=/home/inside/PycharmProjects/RPA3/output/work-items-out/workitems.json
```


