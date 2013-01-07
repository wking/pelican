from blinker import signal

# Run-level signals:

initialized = signal('pelican_initialized')
get_generators = signal('get_generators')
finalized = signal('pelican_finalized')

# Generator-level signals

generator_init = signal('generator_init')

article_generator_init = signal('article_generator_init')
article_generator_finalized = signal('article_generate_finalized')

page_generator_init = signal('page_generator_init')
page_generator_finalized = signal('page_generate_finalized')

static_generator_init = signal('static_generator_init')
static_generator_finalized = signal('static_generate_finalized')

# Page-level signals

article_generator_preread = signal('article_generator_preread')
article_generator_context = signal('article_generator_context')

page_generator_preread = signal('page_generator_preread')
page_generator_context = signal('page_generator_context')

static_generator_preread = signal('static_generator_preread')
static_generator_context = signal('static_generator_context')

content_object_init = signal('content_object_init')
