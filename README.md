# pyse - An quite easy Python Stream Editor

## Motivation
`sed` is a famous stream editor. But I'm not familiar with it. You need to remember some detail of it. Or, you couldn't use it.
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

### Pre-script and Post-script
```
cat something | pyse --pre print \'Start!!\' --each print no, line --post print \'Num:\',no-1
```

### Function Mode
```
#Script file (named 'test')

def pre():
    print 'Start'

def each(line, no):
    print no, line

def post(no):
    print 'Num:', no-1
```

```
cat something | pyse -Ff test
```
