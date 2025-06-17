[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/celalkhalilov-koran-mcp-badge.png)](https://mseep.ai/app/celalkhalilov-koran-mcp)

# Kuran-ı Kerim MCP Server

Bu proje, Model Context Protocol (MCP) kullanarak Kuran-ı Kerim API'lerini sağlayan bir server'dır.

## Özellikler

### Kuran API'leri
- **Sürümler**: Mevcut tüm Kuran sürümlerini listeler
- **Tam Kuran**: Herhangi bir sürümün tamamını getirir
- **Bölüm**: Belirtilen bölümü getirir (1-114)
- **Ayet**: Belirtilen ayeti getirir
- **Cüz**: Belirtilen cüzü getirir (1-30)
- **Rüku**: Belirtilen rükuyu getirir
- **Sayfa**: Belirtilen sayfayı getirir
- **Menzil**: Belirtilen menzili getirir (1-7)
- **Makra**: Belirtilen makrayı getirir
- **Kuran Bilgileri**: Cüz sayısı, secdeler, rükular vb. bilgiler
- **Yazı Tipleri**: Mevcut Arapça yazı tiplerini listeler

## Yazı Tipi Seçenekleri
- **Normal**: Varsayılan yazı tipi
- **Latin (la)**: Latin harfleriyle yazılmış
- **Latin Diakritikli (lad)**: Diakritik işaretli latin harfleri

## Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

2. Server'ı çalıştırın:
```bash
python server.py
```

## Kullanım Örnekleri

### Kuran Sürümlerini Listele
```python
get_quran_editions()
```

### Fatiha Suresini Getir
```python
get_quran_chapter("ben-muhiuddinkhan", 1)
```

### Belirli Bir Ayeti Getir
```python
get_quran_verse("ben-muhiuddinkhan", 2, 255)  # Ayetel Kürsi
```

### Cüz Getir
```python
get_quran_juz("ben-muhiuddinkhan", 1)  # 1. Cüz
```

## API Kaynağı
Kuran API'leri [fawazahmed0/quran-api](https://github.com/fawazahmed0/quran-api) projesinden sağlanmaktadır.

## Lisans
Bu proje açık kaynak kodludur.
