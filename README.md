# To Buy or Not to Buy
A playful tool to help you figure out if you’re better off buying a home or renting and saving.


## Getting Started

### Install Bazelisk
Install Bazelisk by following the instructions on the [Bazelisk GitHub page](https://github.com/bazelbuild/bazelisk).


#### Bazelisk on macOS
```
brew install bazelisk.
```

#### Bazelisk on Ubuntu
If you do not have curl, install it using sudo apt-get install curl then
```
curl -LO "https://github.com/bazelbuild/bazelisk/releases/latest/download/bazelisk-linux-amd64"
```
Make bazelisk executable
```
chmod +x bazelisk-linux-amd64
```
Move bazelisk to the appropriate directory
```
sudo mv bazelisk-linux-amd64 /usr/local/bin/bazel
```
Check the bazel version, which will first install bazel then output the version 
```
bazel --version
```

### To Run Examples
From the root directorty of the project run

```
bazel run //src/to_buy_or_not_to_buy
```
to execute `src/to_buy_or_not_to_buy/main.py`