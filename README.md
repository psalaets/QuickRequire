# QuickRequire

Sublime Text 2 and 3 plugin for generating node-style require() calls.

## Example

![screenshots](demo.gif)

## Usage

### 1. Type a variable name

```js
var foo
```

### 2. Type the keyboard shortcut

* OS X: `cmd + shift + o`
* Windows: `ctrl + shift + o`
* Linux: `ctrl + shift + o`

### 3. QuickRequire inserts the require() call

```js
var foo = require("foo")
```

Note: an equals sign is also added in front of require()

## Supported variable names

QuickRequire looks at the text on the left of the cursor to generate the module name.

```
foo    -> = require("foo")
Foo    -> = require("foo")
fooBar -> = require("foo-bar")
```

If a variable name isn't found, it generates `require("")`

## Requiring internal modules

QuickRequire doesn't have support for requiring a file relative to the current file. Pairing QuickRequire with [AutoFileName](https://packagecontrol.io/packages/AutoFileName) will get you something decent.

## Settings

Go to `Preferences | Package Settings | QuickRequire` to modify these.

### quote_style

What kind of quotes to use in generated require() call. Defaults to `"double"`.

Expected values: `"double"` or `"single"`

## Installation

### Manually

1. `cd` into the [Packages directory](http://docs.sublimetext.info/en/latest/basic_concepts.html#the-packages-directory) of your Sublime Text
2. `git clone https://github.com/psalaets/QuickRequire.git`

### Using Package Control

Package Control support is pending