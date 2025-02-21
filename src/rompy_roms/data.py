"""ROMS Rompy data."""

import logging
from pathlib import Path
from typing import Literal
from pydantic import Field

from rompy.core.data import DataBlob, DataGrid


logger = logging.getLogger(__name__)

HERE = Path(__file__).parent


class Data(DataGrid):
    """Roms data class.

    This is a placeholder for a Roms specific data class. You do not need to
    implement this class if the existing functionality in one of the existing core
    rompy data classes (e.g., DataBlob, DataGrid) is sufficient.

    """

    model_type: Literal["roms"] = Field(
        default="roms",
        description="Model type discriminator",
    )
