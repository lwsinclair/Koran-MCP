import requests

# Kuran API Base URL
QURAN_API_BASE = "https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1"

def get_editions():
    """
    Mevcut tüm Kuran sürümlerini güzelleştirilmiş JSON biçiminde listeler.
    """
    try:
        response = requests.get(f"{QURAN_API_BASE}/editions.json")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve editions. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_editions_min():
    """
    Mevcut tüm Kuran sürümlerinin küçültülmüş versiyonunu getirir.
    """
    try:
        response = requests.get(f"{QURAN_API_BASE}/editions.min.json")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve editions (min). Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_full_quran(edition_name: str, script_type: str = ""):
    """
    Tüm Kuran'ı/Kuran tercümesini getirir.

    Args:
        edition_name: Sürüm adı (örn: "ben-muhiuddinkhan")
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli)
    """
    try:
        suffix = f"-{script_type}" if script_type else ""
        url = f"{QURAN_API_BASE}/editions/{edition_name}{suffix}.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve full Quran. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_chapter(edition_name: str, chapter_no: int, script_type: str = "", minified: bool = False):
    """
    Belirtilen bölümün tamamını getirir.

    Args:
        edition_name: Sürüm adı
        chapter_no: Bölüm numarası (1-114)
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli)
        minified: Küçültülmüş format isteniyor mu
    """
    try:
        suffix = f"-{script_type}" if script_type else ""
        min_suffix = ".min" if minified else ""
        url = f"{QURAN_API_BASE}/editions/{edition_name}{suffix}/{chapter_no}{min_suffix}.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve chapter. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_verse(edition_name: str, chapter_no: int, verse_no: int, script_type: str = ""):
    """
    Belirtilen ayeti getirir.

    Args:
        edition_name: Sürüm adı
        chapter_no: Bölüm numarası (1-114)
        verse_no: Ayet numarası
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli)
    """
    try:
        suffix = f"-{script_type}" if script_type else ""
        url = f"{QURAN_API_BASE}/editions/{edition_name}{suffix}/{chapter_no}/{verse_no}.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve verse. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_juz(edition_name: str, juz_no: int, script_type: str = ""):
    """
    Belirtilen cüzü getirir.

    Args:
        edition_name: Sürüm adı
        juz_no: Cüz numarası (1-30)
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli)
    """
    try:
        suffix = f"-{script_type}" if script_type else ""
        url = f"{QURAN_API_BASE}/editions/{edition_name}{suffix}/juzs/{juz_no}.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve juz. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_ruku(edition_name: str, ruku_no: int, script_type: str = ""):
    """
    Belirtilen rükuyu getirir.

    Args:
        edition_name: Sürüm adı
        ruku_no: Rüku numarası
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli)
    """
    try:
        suffix = f"-{script_type}" if script_type else ""
        url = f"{QURAN_API_BASE}/editions/{edition_name}{suffix}/rukus/{ruku_no}.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve ruku. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_page(edition_name: str, page_no: int, script_type: str = ""):
    """
    Belirtilen sayfayı getirir.

    Args:
        edition_name: Sürüm adı
        page_no: Sayfa numarası
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli)
    """
    try:
        suffix = f"-{script_type}" if script_type else ""
        url = f"{QURAN_API_BASE}/editions/{edition_name}{suffix}/pages/{page_no}.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve page. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_manzil(edition_name: str, manzil_no: int, script_type: str = ""):
    """
    Belirtilen menzili getirir.

    Args:
        edition_name: Sürüm adı
        manzil_no: Menzil numarası (1-7)
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli)
    """
    try:
        suffix = f"-{script_type}" if script_type else ""
        url = f"{QURAN_API_BASE}/editions/{edition_name}{suffix}/manzils/{manzil_no}.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve manzil. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_maqra(edition_name: str, maqra_no: int, script_type: str = ""):
    """
    Belirtilen makrayı getirir.

    Args:
        edition_name: Sürüm adı
        maqra_no: Makra numarası
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli)
    """
    try:
        suffix = f"-{script_type}" if script_type else ""
        url = f"{QURAN_API_BASE}/editions/{edition_name}{suffix}/maqras/{maqra_no}.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve maqra. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_quran_info():
    """
    Kuran'daki cüz sayısı, secdeler, rükular vb. gibi Kuran hakkında tüm ayrıntıları getirir.
    """
    try:
        response = requests.get(f"{QURAN_API_BASE}/info.json")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve Quran info. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_fonts():
    """
    Mevcut Arapça yazı tiplerini listeler.
    """
    try:
        response = requests.get(f"{QURAN_API_BASE}/fonts.json")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve fonts. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}
