from .command import CommandBlock
from .delete import DeleteBlock
from .embed import EmbedBlock
from .silent import SilentBlock
from .require_blacklist import RequireBlock, BlacklistBlock

stable_blocks = [
    CommandBlock(),
    DeleteBlock(),
    EmbedBlock(),
    SilentBlock(),
    RequireBlock(),
    BlacklistBlock(),
]
