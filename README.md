# pyse - An quite Python Stream Editor

## Motivation
sed` are famous stream editor. But I'm not familiar with it. You need to remember some detail of it. Or, you couldn't use it.
And I write Python many years, I think if I could use Python to process text-stream I will be happy.

## Usage
### Basic Example
```
    cat something | pyse print no, line
```
### Read script from file
```
    #Script file (named 'test')

    print no, line
```

```
    cat something | pyse -f test
```
