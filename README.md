# Family Tree CLI

This is a command-line tool for adding people, adding and removing relations, connecting people, and performing various queries on the family tree.



## Installation

To install the Family Tree CLI, use the following command:

```sh
pip install .
```
If you're using Python 3, you might need to use pip3 instead of pip:

```
pip3 install .
```

## Usage
After installing the CLI, you can use the following command to connect people in the family tree:




### Adding a Person
You can add a person to the family tree using the following command:

```
family-tree add person <name>
```
For example:

```
family-tree add person Amit Dhakad
```

### Adding a Relationship
You can add a new relationship type using the following command:

```
family-tree add relationship <name>
```
For example:

```
family-tree add relationship father
```

### Connecting People and Adding Relationships
You can connect people and specify their relationship using the following command:

```
family-tree connect <name1> as <relationship> of <name2>
```
For example:

```
family-tree connect Amit Dhakad as son of KK Dhakad
```

### Queries
You can make queries based on the relationships created:

Count sons of a person:


```
family-tree count sons of <name>
```
Count daughters of a person:

```
family-tree count daughters of <name>
```
Count wives of a person:

```
family-tree count wives of <name>
```
Find father of a person:

```
family-tree father of <name>
```
## Adding Current Path to PATH Variable (Mac)
If you're using Mac, you can add the current path to the PATH variable using the following command:

```
export PATH=/Library/Frameworks/Python.framework/Versions/3.11/bin:$PATH
```
This ensures that you can execute the family-tree command from any directory without specifying the full path.
