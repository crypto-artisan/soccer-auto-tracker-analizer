
# Leagues

* Premier League (England)
* Premiership (Scotland)
* Bundesliga I (Germany)
* Serie A (Italy)
* La Liga (Spain)
* Ligue I (Franch)
* Eredivisie (Netherlands)
* Jupiler Pro League (Belgium)
* Liga I (Portugal)
* Super Lig (Turkey)
* Super League (Greece)
* Serie A (Brazil)
* Allsvenskan (Sweden)

# Requirements

A `requirements.txt` file has been added to the project directory. However, the following table also presents the required libraries. Check the `requirements.txt` file for library versions.

| Library/Module  | Download Url | Installation |
| ------------- | ------------- | -------------
| Python Language | https://www.python.org/ | Download from website |
| Numpy  | https://numpy.org/ | `pip install numpy` |
| Pandas  | https://pandas.pydata.org/ | `pip install pandas` |
| Matplotlib  | https://matplotlib.org/ | `pip install matplotlib` |
| Seaborn  | https://seaborn.pydata.org/ | `pip install seaborn` |
| Scikit-Learn  | https://scikit-learn.org/stable/ | `pip install scikit-learn` |
| Imbalanced-Learn  | https://imbalanced-learn.org/stable/ | `pip install imbalanced-learn` |
| XGBoost  | https://xgboost.readthedocs.io/en/stable/ | `pip install xgboost` |
| Tensorflow  | https://www.tensorflow.org/ | `pip install tensorflow` |
| Tensorflow-Addons  | https://www.tensorflow.org/addons | `pip install tensorflow_addons` |
| TKinter  | https://docs.python.org/3/library/tkinter.html | `pip install tk ` |
| Optuna | https://optuna.org/ | `pip install optuna` |
| Fuzzy-Wuzzy | https://pypi.org/project/py-stringmatching (https://pypi.org/project/fuzzywuzzy/) | `pip install fuzzywuzzy` |

To run `pip` commands, open CMD (windows) using Window Key + R or by typing cmd on the search. In linux, You can use the linux terminal.

# Instructions (How to Run)

1. Download & Install python. During the installation, you should choose  **add to "Path"** It is recommended to download python 3.9.
2. After you download & install python, you can Download the above libraries using pip module (e.g. `pip install numpy`). These modules can be installed via the cmd (in windows) or terminal (in linux). **IMPORTANT**: To download the correct versions, just add "==" after pip install to specify version, as described on requirements.txt file. For example, to install `tensorlfow 2.9.1`, you can use: `pip install tensorflow==2.9.1`.
3. On windows, you can double click the main.py file. Alternatively (Both Windows & Linux), You can open the cmd on the project directory and run: `python main.py`. 

# Common Errors
1. `Cannot install tensorflow.` In case this happens, email me the error. Sometimes it also requires visual studio to be installed. Download the community edition which is free here:  [https://pypi.org/project/py-stringmatching](https://visualstudio.microsoft.com/downloads/)
2. `pip command was not found` in terminal. In this case, you forgot to choose **add to Path** option during the the installation of python. Delete python and repeat download instructions 1-3.
3. `File main.py was not found`. This is because when you open command line (cmd) tool on windows, or terminal on linux, the default directory that cmd is looking at is the home directory, not prophitbet directory. You need to navigate to prophitbet directory, where the main.py file exists. To do that, you can use the `cd` command. e.g. if prophitbit is downloaded on "Downloads" folder, then type `cd Downloads/ProphitBet-Soccer-Bets-Predictor` and then type `python main.py`
4. `python command not found` on linux. This is because python command is `python3` on linux systems
5. `Parsing date is wrong` when trying to parse fixtures from the html file. The html file has many fixtures. Each fixture has a date. You need to specify the correct date of the fixture you are requesting, so the parser identifies the fixtures from the given date and grab the matches. You need to specify the date before importing the fixture file into program.

# Supported Platforms
1. Windows
2. Linux
3. Mac
