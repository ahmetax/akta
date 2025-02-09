import json
from typing import List, Dict, Any
import argparse
from pathlib import Path
from rich.console import Console
from rich.table import Table

class MetadataSearcher:
    def __init__(self, metadata_file: str):
        self.console = Console()
        self.metadata = self.load_metadata(metadata_file)
        
    def load_metadata(self, file_path: str) -> List[Dict[str, Any]]:
        """Metadata dosyasını yükler."""
        entries = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                entries.append(json.loads(line))
        return entries

    def search(self, query: str, field: str = None) -> List[Dict[str, Any]]:
        """Metadata'da arama yapar."""
        query = query.lower()
        results = []
        
        for entry in self.metadata:
            if field:
                # Belirli bir alanda ara
                if field in entry and str(entry[field]).lower().find(query) != -1:
                    results.append(entry)
            else:
                # Tüm alanlarda ara
                for value in entry.values():
                    if isinstance(value, (str, int)) and str(value).lower().find(query) != -1:
                        results.append(entry)
                        break
                    elif isinstance(value, list) and any(query in str(item).lower() for item in value):
                        results.append(entry)
                        break
                        
        return results

    def display_results(self, results: List[Dict[str, Any]]):
        """Arama sonuçlarını tablo olarak gösterir."""
        if not results:
            self.console.print("[yellow]Sonuç bulunamadı.[/yellow]")
            return

        table = Table(show_header=True)
        table.add_column("Türkçe Başlık")
        table.add_column("Orijinal Başlık")
        table.add_column("Yazar")
        table.add_column("Çevirmen")
        table.add_column("Yıl")
        table.add_column("Dosya")
        table.add_column("Durum")

        for entry in results:
            table.add_row(
                entry.get('turkish_title', ''),
                entry.get('original_title', ''),
                entry.get('author', ''),
                entry.get('translator', ''),
                str(entry.get('year', '')),
                entry.get('file_path', ''),
                entry.get('status', '')
            )

        self.console.print(table)
        self.console.print(f"\n[green]Toplam {len(results)} sonuç bulundu.[/green]")

def main():
    parser = argparse.ArgumentParser(description='AKTA Metadata Arama Aracı')
    parser.add_argument('query', help='Arama terimi')
    parser.add_argument('--metadata', default='metadata.jsonl',
                      help='Metadata dosyası (varsayılan: metadata.jsonl)')
    parser.add_argument('--field', choices=['author', 'translator', 'turkish_title', 
                                          'original_title', 'categories'],
                      help='Aranacak alan (opsiyonel)')
    
    args = parser.parse_args()
    
    searcher = MetadataSearcher(args.metadata)
    results = searcher.search(args.query, args.field)
    searcher.display_results(results)

if __name__ == "__main__":
    main()
