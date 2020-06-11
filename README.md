# imonits
Search code and find "IMO" or "nits" level problem.

## Usage
```
python imonits.py -d /var/local/hoge/
```

When excude warning by PHPDoc. For example use egrep.
```
python imonits.py -d /var/local/hoge/ | egrep -v '0      \| 1' 
```

## Submodule
[kotaoue/clitable](https://github.com/kotaoue/clitable)