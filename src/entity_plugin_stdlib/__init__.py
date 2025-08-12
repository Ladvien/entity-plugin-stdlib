"""Entity Plugin Standard Library - Core plugins for Entity Framework.

This package provides the standard library of plugins that ship with Entity Framework,
including input/output adapters, prompts, tools, and the pass-through plugin.
"""

from .defaults import PassThroughPlugin
from .input_adapter import InputAdapterPlugin
from .output_adapter import OutputAdapterPlugin
from .prompt import PromptPlugin
from .smart_selector import SmartToolSelectorPlugin
from .tool import ToolPlugin

__all__ = [
    "PassThroughPlugin",
    "InputAdapterPlugin",
    "OutputAdapterPlugin",
    "PromptPlugin",
    "SmartToolSelectorPlugin",
    "ToolPlugin",
]

__version__ = "0.1.0"