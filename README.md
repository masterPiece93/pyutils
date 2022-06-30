# pyutils

### Read Only Dict

This is a dict wrapper , used when you want to declare a FINAL dict 

Key Points :
- can only add key-value pairs on declaration
- can't delete key-value pairs
- can't modify key-value pairs
- can make a copy of the dict object
- 
Usage :

```d = DictWrapper({"a":2,"b":[1,2]})```

now 'd' will behave as a normal dict

