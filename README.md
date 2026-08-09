
# Welcome to SeaKrait! 🐟
### What is SeaKrait 🐟
SeaKrait is the official rebundle and successor to `Looprlib` and `Looprlib-Mit`. \
All future updates and new features will be released exclusively under the SeaKrait name.\
SeaKrait was made to change the cofusing name "Looprlib" to something more friendly like Seakrait (Maybe this is a bad example ¯\_(ツ)_/¯)\
Everything from the originals are still here.\
This is the only version that will continue to update

## Features

- **Simplified Math Utilities:** Quick logical and evaluation helper functions.
- **Friendly API:** Clear, descriptive function names replacing the older `Looprlib` syntax.
- **Lightweight & Fast:** Zero heavy third-party dependencies.





### Use Cases
You could use this to test positivity of an number and get a result with this:

Here is the positivity function.

    def positivity(i,pos,neg,zero):
        if i > 0:
            return pos
        elif i < 0:
            return neg
        else:
            return zero

### Example
    
    import seakr
    print(seakr.seamath.positivity(100,21,32,123))

#### if 100 is positive the result is 21
#### if 100 is negative the result is 32
#### if 100 is equal to 0  the result is 123

#### in this case the function will print 21 to the terminal!

## Installation

Install SeaKrait instantly via `pip`:

```
pip install SeaKrait
```


### Other Material
 to see `Test releases` go to: https://test.pypi.org/project/Looprlib/ \
 And `Original releases` go to: https://pypi.org/project/Looprlib/ \
 Releases on Anaconda are also planed in the future
