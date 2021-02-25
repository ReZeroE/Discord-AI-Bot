# DiscordAIBot
This is a deep-learning AI bot programmed in python with the categorical feature of one-hot encoding.

# General Info
 - Name: Milim
 - Language: python
 - Control Prefix: `//`
 - Latest Version: 1.5 (Beta Testing)
 - Current Status: active
 - Activate Discord: [Link](https://discord.gg/RxahGwTGmG)
 
 # Primary Functions
 There are two types of primary functions - one set accessable by all members within the server and the other set is only accessable by the admin. Admin functions are all password gated and would require the admin to enter the passcode in the back-end terminal before the function would excute.
 
**Public Functions**

- [x] Next Episode Countdown Timer
- [x] Auto Chat
- [x] Japanese to English Translation
- [x] Anime Info (author, studio, OP, ED, etc.)
- [x] Episode List
- [ ] Character List
- [ ] Mini Games

**Admin Functions - Back-end password required**

- [x] Message Purge (Controlled)
- [x] Various Discord Embeds (Controlled)
- [x] Message Scan
- [ ] Translation Report

# Bot Detail
The bot is programmed in python with its learning model based on the categorical feature of One-Hot encoding. Learning data are from WEP json file.

**Deep-Learning**
- Deep-learning Method: One-Hot Encoded
- Built-in Neuron Layers: 3 (only two are active)
- Neurons Each Layer: 16
- Output Neuron Layer with Softmax
- Neural Network Type: DNN
- Training Epoch: 2000
- Training Batch-size: 15

I've also tried the multi-regression models that are generally used for data evalution/prediction and it did not work very well in this case. 

There are three neuron layers written in the program but only two of which are active at the moment. I've ran multiple tests calibrating the following values for the best accuracy and efficiency with the given input (json):
 1. Neuron Layers
 2. Neuron Each Layer
 3. Epoch + Batch-size
 
 The values I've implements are of the best accuracy and efficiency as of right now.

- Neuron number can be changed on: `net = tflearn.fully_connected(net, 16)`
- Epoch and batch-size can be edited on: `model.fit(training, output, n_epoch=2000, batch_size=10, show_metric=True)`

**Following modules are used for deep-learning**
- numpy (version==1.19.5)
- Tensorflow (version==1.13.2) -> Required
- tflearn (verions==0.5.0)
- nltk (veriosn==3.5)
- pickle

Note: Program will not re-learn unless the previous learning data has been erased.

# Function Details
## Public Functions
Most of the following functions utilized the deep-learning feature to understand user inputs.
- Countdown Timer
   - The program will evaluate the time until the next episode based on current time and pre-entered anime dates. The program will automatically scan and calculate which episode has already been out and what is the next episode.
   - Example command: `//when's the next ep?`
- Auto Chat
   - Auto replies with the data in the json file.
   - A reply accuracy threshold has been set for database replies: `results[results_index] > 0.999` (99.9%)
   - Example command: `//hello!`, `//how are you?`, `//what are your functionalities?`, etc.
- JP to EN Translation (Passive Function)
   - Scans user input to make sure no English alphabet is contained in the message: `re.search('[a-z][A-Z]', user_input) == None`
   - Translations including English alphabets are generally very inaccurate.
   - Used the `google_trans_new` module.
   - Example commands: `がうるぐら` -> "Gwra Gura"
- Anime Info
   - Very Similar to Auto Chat. Respond with pre-programmed answers.
   - Example commands: `//Who is the author?`, `//whats the op?`, `//where can i watch this anime?`, etc.
- Episode List
   - Evaluate the user input to see if the user is asking about an past episode or an upcoming episode.
   - Output the date of the episode based on whether if the episode exist, has been out, or is yet to come out.
   - Example command: `//when did ep 5 come out?`, `//when was ep 99999 released?`, etc.
- Future Implementations
   - Character List
   - Mini Games

## Private Admin Functions

All of the following functions does not require deep-learning and only takes in pre-specified commands. A password will be auto generated when these functions are called upon and the admin has 10 seconds to enter the password in the terminal before a time-out occurrs. All of the following functions are password gated.
- Message Purge
   - Erase a given number of messages after a certain number of seconds.
   - Example command: `//purge 50`
- Discord Embeds
   - Sends discord embeds based on the function that it's been called upon. This allows admin to change embeds faster than any other bots.
   - Example command: `//update rules`, `//update staff embed`, etc.
- Message Scan (Passive Function)
   - Scans messages in the active channel and make sure "nothing bad happens."
- Future Implementations
   - Translation Report
