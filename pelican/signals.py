from blinker import signal

# Run-level signals:

initialized = signal('pelican_initialized')
get_generators = signal('get_generators')
finalized = signal('pelican_finalized')

# Generator-level signals

generator_init = signal('generator_init')

article_generator_init = signal('article_generator_init')
article_generator_finalized = signal('article_generate_finalized')

pages_generator_init = signal('pages_generator_init')
pages_generator_finalized = signal('pages_generate_finalized')

static_generator_init = signal('static_generator_init')
static_generator_finalized = signal('static_generate_finalized')

# Page-level signals

article_generator_preread = signal('article_generator_preread')
article_generator_context = signal('article_generator_context')

pages_generator_preread = signal('pages_generator_preread')
pages_generator_context = signal('pages_generator_context')

static_generator_preread = signal('static_generator_preread')
static_generator_context = signal('static_generator_context')

content_object_init = signal('content_object_init')
