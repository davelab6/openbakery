from openbakery.callable import check
from openbakery.status import PASS, FAIL
from openbakery.message import Message

# used to inform get_module_profile whether and how to create a profile
from openbakery.fonts_profile import (
    profile_factory,
)  # NOQA pylint: disable=unused-import

profile_imports = ((".", ("shared_conditions",)),)


@check(
    id="com.google.fonts/check/loca/maxp_num_glyphs",
    conditions=["is_ttf"],
    proposal="legacy:check/180",
)
def com_google_fonts_check_loca_maxp_num_glyphs(ttFont):
    """Does the number of glyphs in the loca table match the maxp table?"""
    if len(ttFont["loca"]) < (ttFont["maxp"].numGlyphs + 1):
        yield FAIL, Message(
            "corrupt", 'Corrupt "loca" table or wrong numGlyphs in "maxp" table.'
        )
    else:
        yield PASS, "'loca' table matches numGlyphs in 'maxp' table."
