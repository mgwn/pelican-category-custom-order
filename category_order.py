from pelican import signals

CATEGORIES_ATTR = 'categories'
 
def categoryIndex(key, order, default):
  try:
    return str(order.index(key))
  except:
    return str(default) + key

def set_category_order(generator):
  category_custom_order = generator.settings.get('CATEGORIES_CUSTOM_ORDER', None)
  category_default_order = generator.settings.get('CATEGORIES_DEFAULT_ORDER', 100)
  raw = generator.context.get(CATEGORIES_ATTR, [])

  if category_custom_order:
    new = sorted(raw, key=lambda t: categoryIndex(t[0], category_custom_order, category_default_order))
    generator.context[CATEGORIES_ATTR] = new


def register():
  signals.article_generator_finalized.connect(set_category_order)
