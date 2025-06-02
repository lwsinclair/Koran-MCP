#!/usr/bin/env python3
"""
Kuran-ı Kerim MCP Server Test Dosyası
"""

import sys
from app import (
    get_editions_min, get_quran_info,
    get_fonts, get_verse, get_chapter
)

def test_quran_editions():
    """Kuran sürümlerini test eder"""
    print("\n📖 Kuran Sürümleri Testi...")
    try:
        result = get_editions_min()
        if "error" in result:
            print(f"❌ Hata: {result['error']}")
            return False
        else:
            print(f"✅ Başarılı! {len(result)} sürüm bulundu")
            return True
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

def test_quran_info():
    """Kuran bilgilerini test eder"""
    print("\n📚 Kuran Bilgileri Testi...")
    try:
        result = get_quran_info()
        if "error" in result:
            print(f"❌ Hata: {result['error']}")
            return False
        else:
            print("✅ Başarılı! Kuran bilgileri alındı")
            if "chapters" in result:
                print(f"   📄 Toplam bölüm sayısı: {len(result['chapters'])}")
            return True
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

def test_fonts():
    """Yazı tiplerini test eder"""
    print("\n🔤 Yazı Tipleri Testi...")
    try:
        result = get_fonts()
        if "error" in result:
            print(f"❌ Hata: {result['error']}")
            return False
        else:
            print(f"✅ Başarılı! Yazı tipleri alındı")
            return True
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

def test_verse():
    """Ayet testi"""
    print("\n📜 Ayet Testi...")
    try:
        # Fatiha'nın ilk ayeti
        result = get_verse("ben-muhiuddinkhan", 1, 1)
        if "error" in result:
            print(f"❌ Hata: {result['error']}")
            return False
        else:
            print("✅ Başarılı! Fatiha'nın ilk ayeti alındı")
            return True
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

def test_chapter():
    """Bölüm testi"""
    print("\n📖 Bölüm Testi...")
    try:
        # Fatiha suresi
        result = get_chapter("ben-muhiuddinkhan", 1, "", True)  # minified
        if "error" in result:
            print(f"❌ Hata: {result['error']}")
            return False
        else:
            print("✅ Başarılı! Fatiha suresi alındı")
            return True
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

def main():
    """Ana test fonksiyonu"""
    print("🚀 Kuran-ı Kerim MCP Server Test Başlıyor...\n")

    tests = [
        test_quran_editions,
        test_quran_info,
        test_fonts,
        test_verse,
        test_chapter
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n📊 Test Sonuçları: {passed}/{total} test başarılı")
    
    if passed == total:
        print("🎉 Tüm testler başarılı!")
        return 0
    else:
        print("⚠️  Bazı testler başarısız!")
        return 1

if __name__ == "__main__":
    sys.exit(main())
