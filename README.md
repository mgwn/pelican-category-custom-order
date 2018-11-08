# Control Category Display Order
By default, you can only set the order categories (and tags) alphabetically. And there is a plugin [category_order](https://github.com/jhshi/pelican.plugins.category_order) offers to sort them by the number of articles.  
This plugin offers to sort them by a given list

# Settings
- ``CATEGORIES_CUSTOM_ORDER``: the list of categories

```Python
CATEGORIES_CUSTOM_ORDER = [
    'Get Start',
    'Tutorials',
    'API Reference'
]
```

- ``CATEGORIES_DEFAULT_ORDER`:(optional, default=100) the default value of those not in the list. They will order alphabetically.