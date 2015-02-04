# QuickRequire

Sublime Text plugin for generating CommonJS-style require() calls.

## Usage

### 1. Type something

```js
var foo
```

### 2. Type the keyboard shortcut

* OSX: cmd + shift + o
* Windows/Linux: ctrl + shift + o

### 3. require() is inserted

```js
var foo = require("foo")
```

## Supported variable names

QuickRequire looks at the text to the left of the cursor to generate the module name.

```
foo    -> require("foo")
Foo    -> require("foo")
fooBar -> require("foo-bar")
```

If a variable name isn't found, it generates `require("")`

## Settings

Go to `Preferences | Package Settings | QuickRequire` to modify these.

### quote_style

What kind of quotes to use in generated require() call.

Expected values: `"double"` or `"single"`

## Install

???