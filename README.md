# clean-gurk
I made this work-around to eliminate the messages and files from [gurk](https://github.com/boxdot/gurk-rs) until the feature of [Disappearing Messages](https://github.com/boxdot/gurk-rs/issues/79] is ready

# Installation

### Bring the script to somewhere your PATH, i will use ~/.local/bin

    wget https://raw.githubusercontent.com/nothingbutlucas/clean-gurk/main/clean_gurk.py -P ${HOME}/.local/bin/

### Create a crontask to execute the script every x time. I will use 1 hour.

    crontab -e 
    
    0 */1 * * * ${HOME}/.local/bin/clean_gurk.py
    
