"""Desktop presentation by sphinx-revealjs."""

from jinja2 import Template
from sphinx.application import Sphinx
from sphinx_revealjs.builders import RevealjsHTMLBuilder  # type: ignore

__version__ = "0.0.0"

ENTRYPOINT = Template(
    """
import webview

window = webview.create_window(
    title="sphinx-revealjs presentation",
    url="contents/index.html",
    width={{ window_width }},
    height={{ window_height }},
)
webview.start()
""".strip()
)


class RevealjsDesktopBuilder(RevealjsHTMLBuilder):  # noqa: D101
    name = "revealjsdesktop"


def prepare_outdir(app: Sphinx):
    """Override outdir of Sphinx."""
    ctx = {
        "window_width": app.config.revealjs_desktop_width,
        "window_height": app.config.revealjs_desktop_height,
    }
    entrypoint = app.outdir / "main.py"
    entrypoint.write_text(ENTRYPOINT.render(ctx), encoding="utf8")
    app.outdir = app.outdir / "contents"
    app.builder.outdir = app.outdir


def setup(app: Sphinx):  # noqa: D103
    app.setup_extension("sphinx_revealjs")
    app.add_config_value("revealjs_desktop_width", 960, "env", int)
    app.add_config_value("revealjs_desktop_height", 720, "env", int)
    app.add_builder(RevealjsDesktopBuilder)
    app.connect("builder-inited", prepare_outdir)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
