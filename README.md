# QuickRequire

Sublime Text plugin for generating CommonJS-style require() calls.

## Usage

### 1. Type something

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

Note: equals sign is added in front of require()

## Supported variable names

QuickRequire looks at the text on the left of the cursor to generate the module name.

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