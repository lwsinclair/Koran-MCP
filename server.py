from mcp.server.fastmcp import FastMCP
from app import (
    get_editions, get_editions_min, get_full_quran,
    get_chapter, get_verse, get_juz, get_ruku, get_page,
    get_manzil, get_maqra, get_quran_info, get_fonts
)

# Initialize MCP server
mcp = FastMCP("quran-mcp")

@mcp.tool()
async def get_quran_editions() -> dict:
    """
    Mevcut tüm Kuran sürümlerini güzelleştirilmiş JSON biçiminde listeler.
    """
    result = get_editions()
    return result

@mcp.tool()
async def get_quran_editions_min() -> dict:
    """
    Mevcut tüm Kuran sürümlerinin küçültülmüş versiyonunu getirir.
    """
    result = get_editions_min()
    return result

@mcp.tool()
async def get_quran_full(edition_name: str, script_type: str = "") -> dict:
    """
    Tüm Kuran'ı/Kuran tercümesini getirir.

    Args:
        edition_name: Sürüm adı (örn: "ben-muhiuddinkhan")
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli)
    """
    result = get_full_quran(edition_name, script_type)
    return result

@mcp.tool()
async def get_quran_chapter(edition_name: str, chapter_no: int, script_type: str = "", minified: bool = False) -> dict:
    """
    Belirtilen bölümün tamamını getirir.

    Args:
        edition_name: Sürüm adı
        chapter_no: Bölüm numarası (1-114)
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli)
        minified: Küçültülmüş format isteniyor mu
    """
    result = get_chapter(edition_name, chapter_no, script_type, minified)
    return result

@mcp.tool()
async def get_quran_verse(edition_name: str, chapter_no: int, verse_no: int, script_type: str = "") -> dict:
    """
    Belirtilen ayeti getirir.

    Args:
        edition_name: Sürüm adı
        chapter_no: Bölüm numarası (1-114)
        verse_no: Ayet numarası
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli)
    """
    result = get_verse(edition_name, chapter_no, verse_no, script_type)
    return result

@mcp.tool()
async def get_quran_juz(edition_name: str, juz_no: int, script_type: str = "") -> dict:
    """
    Belirtilen cüzü getirir.

    Args:
        edition_name: Sürüm adı
        juz_no: Cüz numarası (1-30)
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli)
    """
    result = get_juz(edition_name, juz_no, script_type)
    return result

@mcp.tool()
async def get_quran_ruku(edition_name: str, ruku_no: int, script_type: str = "") -> dict:
    """
    Belirtilen rükuyu getirir.

    Args:
        edition_name: Sürüm adı
        ruku_no: Rüku numarası
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli)
    """
    result = get_ruku(edition_name, ruku_no, script_type)
    return result

@mcp.tool()
async def get_quran_page(edition_name: str, page_no: int, script_type: str = "") -> dict:
    """
    Belirtilen sayfayı getirir.

    Args:
        edition_name: Sürüm adı
        page_no: Sayfa numarası
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli)
    """
    result = get_page(edition_name, page_no, script_type)
    return result

@mcp.tool()
async def get_quran_manzil(edition_name: str, manzil_no: int, script_type: str = "") -> dict:
    """
    Belirtilen menzili getirir.

    Args:
        edition_name: Sürüm adı
        manzil_no: Menzil numarası (1-7)
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli)
    """
    result = get_manzil(edition_name, manzil_no, script_type)
    return result

@mcp.tool()
async def get_quran_maqra(edition_name: str, maqra_no: int, script_type: str = "") -> dict:
    """
    Belirtilen makrayı getirir.

    Args:
        edition_name: Sürüm adı
        maqra_no: Makra numarası
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli)
    """
    result = get_maqra(edition_name, maqra_no, script_type)
    return result

@mcp.tool()
async def get_quran_info() -> dict:
    """
    Kuran'daki cüz sayısı, secdeler, rükular vb. gibi Kuran hakkında tüm ayrıntıları getirir.
    """
    result = get_quran_info()
    return result

@mcp.tool()
async def get_quran_fonts() -> dict:
    """
    Mevcut Arapça yazı tiplerini listeler.
    """
    result = get_fonts()
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio")