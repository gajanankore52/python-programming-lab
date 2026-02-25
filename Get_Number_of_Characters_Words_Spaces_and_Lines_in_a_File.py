# Get Number of Characters, Words, Spaces and Lines in a File - Python

import re

def get_file_stats(file_path):
    stats = {
        "lines" : 0,
        "words" : 0,
        "chars" : 0,
        "spaces": 0,
    }
    
    try:
        with open(file_path,'r',encoding = 'utf-8') as file:
            for line in file:
                stats['lines'] += 1
                stats['chars'] += len(line)
                stats['spaces'] += line.count(' ')
                
                # Using regex to handle words separated by commas/punctuation
                words = re.findall(r'\w+',line)
                stats['words'] += len(words)
        
        return stats

    except FileNotFoundError:
        return 'Error: File not found.'


# Usage
results = get_file_stats('fruits.txt')

if isinstance(results, dict):
    print(f"{'Metric':<15} | {'Count':<10}")
    print('-' * 28)
    
    for metric,count in results.items():
        print(f'{metric.capitalize():<15} | {count:<10}')